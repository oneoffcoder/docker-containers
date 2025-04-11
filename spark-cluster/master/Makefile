IMAGE_NAME=spark-master
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
		--platform=$(PLATFORM) \
		-e PYSPARK_MASTER=spark://localhost:7077 \
		$(IMAGE_NAME)

ssh:
	ssh root@localhost -p 23

purge: clean
	docker rmi $(IMAGE_NAME) || true
