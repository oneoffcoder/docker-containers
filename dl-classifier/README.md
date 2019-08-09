
```bash
docker run -it \
    -v $HOME/git/docker-containers/dl-classifier/faces-small:/data \
    -v $HOME/git/docker-containers/dl-classifier/model:/model \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    dl-classifier:local
```