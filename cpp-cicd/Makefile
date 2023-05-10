.PHONY: build push
.DEFAULT_GOAL := build

ORGANIZATION = oneoffcoder
REPOSITORY = cpp-cicd
VERSION = 0.0.5
IMAGE_VERSION = $(ORGANIZATION)/$(REPOSITORY):$(VERSION)
IMAGE_LATEST = $(ORGANIZATION)/$(REPOSITORY):latest

build:
	docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t $(IMAGE_VERSION) .
	docker tag $(IMAGE_VERSION) ${IMAGE_LATEST}

push:
	docker push ${IMAGE_VERSION}
	docker push ${IMAGE_LATEST}