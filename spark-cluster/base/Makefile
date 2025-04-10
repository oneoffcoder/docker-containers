# Name of the Docker image
IMAGE_NAME=spark-base
PLATFORM=linux/amd64

build:
	docker build --platform=$(PLATFORM) -t $(IMAGE_NAME) .

interactive:
	docker run -it --rm --platform=$(PLATFORM) $(IMAGE_NAME)

purge: clean
	docker rmi $(IMAGE_NAME) || true
