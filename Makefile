APP=tiers-api
COMMIT=$(shell git rev-parse HEAD)
IMAGE=$(DOCKER_USER)/$(APP):$(COMMIT)

local: build local-docker

deploy: build upload

build:
	docker build -t $(IMAGE) .

local-docker:
	docker run -p5000:5000 $(IMAGE)

upload:
	docker login -u $(DOCKER_USER) -p $(DOCKER_PASSWORD)
	docker push $(IMAGE)