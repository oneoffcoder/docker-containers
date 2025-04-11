# Name of the Docker image
IMAGE_NAME=spark-slave
PLATFORM=linux/amd64

build:
	docker build --platform=$(PLATFORM) -t $(IMAGE_NAME) .

run:
	docker run \
		-it \
		--rm \
		-p 23:22 \
		-p 50010:50010 \
		-p 50020:50020 \
		-p 50075:50075 \
		-p 7078:7078 \
		-p 8081:8081
		--platform=$(PLATFORM) \
		$(IMAGE_NAME)

ssh:
	ssh root@localhost -p 23

purge: clean
	docker rmi $(IMAGE_NAME) || true
