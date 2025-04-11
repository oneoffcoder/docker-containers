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
		--platform=$(PLATFORM) \
		$(IMAGE_NAME)

ssh:
	ssh root@localhost -p 23

purge: clean
	docker rmi $(IMAGE_NAME) || true
