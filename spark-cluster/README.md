# Notes

On each worker/slave node.

```bash
sudo apt install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker $USER
newgrp docker
docker run hello-world
```

On master node.

```bash
docker pull oneoffcoder/spark-master:latest
```

On slave/worker nodes.

```bash
docker pull oneoffcoder/spark-slave:latest
```

On all nodes.

```bash
mkdir cluster \
    && cd cluster \
    && cp -R ~/git/docker-containers/spark-cluster/base/ubuntu/usr/local/hadoop . \
    && cp -R ~/git/docker-containers/spark-cluster/base/ubuntu/usr/local/spark . \
    && ll
```

On slave/worker nodes.

```bash
docker run \
    -it \
    --rm \
    -p 23:22 \
    -p 50010:50010 \
    -p 50020:50020 \
    -p 50075:50075 \
    -p 7078:7078 \
    -p 8081:8081 \
    -v $(pwd)/hadoop/etc/hadoop:/usr/local/hadoop/etc/hadoop/ \
    -v $(pwd)/spark/conf:/usr/local/spark/conf \
    oneoffcoder/spark-slave:latest
```

On master node.

```bash
docker run \
    -it \
    --rm \
    -p 23:22 \
    -p 9870:9870 \
    -p 8088:8088 \
    -p 8080:8080 \
    -p 18080:18080 \
    -p 9000:9000 \
    -p 9864:9864 \
    -p 50010:50010 \
    -p 50020:50020 \
    -p 50075:50075 \
    -p 7078:7078 \
    -p 8081:8081 \
    -v $(pwd)/hadoop/etc/hadoop:/usr/local/hadoop/etc/hadoop/ \
    -v $(pwd)/spark/conf:/usr/local/spark/conf \
    -e PYSPARK_MASTER=spark://localhost:7077 \
    oneoffcoder/spark-master:latest
```