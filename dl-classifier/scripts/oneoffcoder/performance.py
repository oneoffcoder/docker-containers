import torch
import torch.nn.functional as F
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score
from scipy import interp
import numpy as np
from collections import namedtuple
import matplotlib.pyplot as plt
import seaborn as sns

PREDICTION = namedtuple('Prediction', 'P y')

def get_predictions(model, dataloaders, dataset_key='valid'):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    P = []

    was_training = model.training
    model.eval()

    with torch.no_grad():
        for _, (inputs, labels) in enumerate(dataloaders[dataset_key]):
            inputs = inputs.to(device)
            labels = labels.to(device)

            labels = labels.cpu().detach().numpy()
            outputs = model(inputs)
            probs = F.softmax(outputs, dim=0).cpu().detach().numpy()

            preds = np.hstack([probs, labels.reshape(-1, 1)])
            P.append(preds)


        model.train(mode=was_training)

    P = np.vstack(P)
    y = P[:,-1]
    y = label_binarize(y, classes=np.unique(y))
    return PREDICTION(P[:,:-1], y)

def get_roc_stats(V):
    n_classes = V.y.shape[1]
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    keys = []

    # individual ROC curves
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(V.y[:, i], V.P[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
        keys.append(i)
        
    # micro averaging
    fpr['micro'], tpr['micro'], _ = roc_curve(V.y.ravel(), V.P.ravel())
    roc_auc['micro'] = auc(fpr['micro'], tpr['micro'])
    keys.append('micro')

    # macro averaging
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= n_classes
    fpr['macro'] = all_fpr
    tpr['macro'] = mean_tpr
    roc_auc['macro'] = auc(fpr['macro'], tpr['macro'])
    keys.append('macro')
    
    return tpr, fpr, roc_auc, keys

def plot_rocs(tpr, fpr, roc_auc, keys, ax):
    n_classes = len(keys)

    colors = sns.color_palette('hls', n_classes)
    alphas = np.flip(np.linspace(0.4, 1.0, n_classes))

    for clazz, color, alpha in zip(keys, colors, alphas):
        linestyle, lw = ('solid', 1) if isinstance(clazz, int) else ('dotted', 4)
        ax.plot(fpr[clazz], tpr[clazz], alpha=alpha, color=color, linestyle=linestyle, lw=lw, 
                label='Class {}, AUC = {:.2f}'.format(clazz, roc_auc[clazz]))

    ax.plot([0, 1], [0, 1], alpha=0.25, color='red', lw=1, linestyle='--')
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('FPR')
    ax.set_ylabel('TPR')
    ax.set_title('ROC Curve')
    ax.legend(loc="lower right")
    
def get_pr_stats(V):
    n_classes = V.y.shape[1]
    precision = dict()
    recall = dict()
    average_precision = dict()
    baselines = dict()
    keys = []

    # individual ROC curves
    for i in range(n_classes):
        precision[i], recall[i], _ = precision_recall_curve(V.y[:, i], V.P[:, i])
        average_precision[i] = average_precision_score(V.y[:, i], V.P[:, i])
        baselines[i] = V.y[:,i].sum() / V.y.shape[0]
        keys.append(i)
        
    # micro averaging
    precision['micro'], recall['micro'], _ = precision_recall_curve(V.y.ravel(), V.P.ravel())
    average_precision['micro'] = average_precision_score(V.y, V.P, average='micro')
    baselines['micro'] = V.y.ravel().sum() / V.y.ravel().size
    keys.append('micro')
    
    return precision, recall, average_precision, baselines, keys

def plot_prs(precision, recall, average_precision, baselines, keys, ax):
    f_scores = np.linspace(0.2, 0.8, num=4)
    for f_score in f_scores:
        x = np.linspace(0.01, 1)
        y = f_score * x / (2 * x - f_score)
        l, = plt.plot(x[y >= 0], y[y >= 0], color='gray', alpha=0.2)
        ax.annotate('f1={0:0.1f}'.format(f_score), xy=(0.9, y[45] + 0.02))
    
    n_classes = len(keys)

    colors = sns.color_palette('hls', n_classes)
    alphas = np.flip(np.linspace(0.4, 1.0, n_classes))

    for clazz, color, alpha in zip(keys, colors, alphas):
        linestyle, lw = ('solid', 1) if isinstance(clazz, int) else ('dotted', 4)
        ax.plot(recall[clazz], precision[clazz], alpha=alpha, color=color, linestyle=linestyle, lw=lw, 
                label='Class {}, AUC = {:.2f}, b = {:.2f}'.format(clazz, average_precision[clazz], baselines[clazz]))
        # ax.plot((0, 1), (baselines[clazz], baselines[clazz]), color=color, alpha=0.3)

    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.05])
    ax.set_xlabel('recall')
    ax.set_ylabel('precision')
    ax.set_title('PR Curve')
    ax.legend(loc="upper right")