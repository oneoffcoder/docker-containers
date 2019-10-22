```bash
docker run -it \
    -p 8888:8888 \
    -v $HOME/git/docker-containers/java-jupyter/ubuntu/root/ipynb:/root/ipynb \
    java-jupyter:local
```