.PHONY: build 

IMAGE_NAME=secret_messaging
CONTAINER_NAME=secret_messaging_svc

build:
	tag=$(shell cat VERSION | head -n 1) && \
	if [ -z "$$tag" ]; then echo "VERSION is empty"; exit 1; fi && \
	docker build -t $(IMAGE_NAME):$$tag .