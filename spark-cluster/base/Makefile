IMAGE_NAME=spark-base
PLATFORM=linux/amd64
ORGANIZATION=oneoffcoder
VERSION=0.0.1
VER_TAG := $(ORGANIZATION)/$(IMAGE_NAME):$(VERSION)
LAT_TAG := $(ORGANIZATION)/$(IMAGE_NAME):latest

build:
	docker build --platform=$(PLATFORM) -t $(IMAGE_NAME) .

push:
	docker tag $(IMAGE_NAME) $(VER_TAG)
	docker tag $(IMAGE_NAME) $(LAT_TAG)

	@echo "docker push $(VER_TAG)"
	@echo "docker push $(LAT_TAG)"

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
