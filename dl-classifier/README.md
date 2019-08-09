
```bash
docker run -it \
    -v $HOME/git/docker-containers/dl-classifier/faces-small:/data \
    -v $HOME/git/docker-containers/dl-classifier/model:/model \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    dl-classifier:local

docker run -it \
    -v $HOME/git/docker-containers/dl-classifier/faces-small:/data \
    -v $HOME/git/docker-containers/dl-classifier/model:/model \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    dl-classifier:local -m inception_v3 -d /data -e 1 -o /model
```

```bash
docker run -it \
    -v $HOME/git/docker-containers/dl-classifier/faces:/data \
    -v $HOME/git/docker-containers/dl-classifier/model:/model \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    dl-classifier:local -m inception_v3 -d /data -e 25 -o /model
```