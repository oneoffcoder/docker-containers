.PHONY: build push
.DEFAULT_GOAL := build

ORGANIZATION = oneoffcoder
REPOSITORY = cpp-cicd
VERSION = 0.0.5
IMAGE_VERSION = $(ORGANIZATION)/$(REPOSITORY):$(VERSION)
IMAGE_LATEST = $(ORGANIZATION)/$(REPOSITORY):latest

build:
	docker buildx build --platform linux/amd64,linux/arm64 -t $(IMAGE_VERSION) --push .

push:
	docker push ${IMAGE_VERSION}