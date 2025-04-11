# Name of the Docker image
IMAGE_NAME=spark-master
PLATFORM=linux/amd64

build:
	docker build --platform=$(PLATFORM) -t $(IMAGE_NAME) .

run:
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
		--platform=$(PLATFORM) \
		-e PYSPARK_MASTER=spark://localhost:7077 \
		$(IMAGE_NAME)

ssh:
	ssh root@localhost -p 23

purge: clean
	docker rmi $(IMAGE_NAME) || true
