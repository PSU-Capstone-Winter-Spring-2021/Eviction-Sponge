# run react-scripts build
frontend_build: frontend_clean
	cd ../..; \
	docker run --rm \
		-v `pwd`/src/frontend:/src/frontend \
		-v evictionsponge_node_modules:/src/frontend/node_modules \
		node:14.16.0-alpine /bin/sh -c 'cd /src/frontend && npm i && npm run build'

# delete react built files
frontend_clean:
	rm -rf ../frontend/build/*

# build a docker image containing the backend Python environment
backend_env_build:
	cd ../backend; \
	docker build . -t evictionsponge/expungeservice:dev

# make sure RS_ENV is set and not 'dev'
env_check:
ifndef RS_ENV
	@echo error: RS_ENV value required 1>&2
	@exit 1
endif
ifeq ($(RS_ENV),dev)
	@echo error: RS_ENV can not be set to 'dev' 1>&2
	@exit 1
endif

# remove source from docker image context tree
clean:
	rm -rf docker/expungeservice/backend \
         docker/expungeservice/frontend

# synchronize source trees into docker context tree
rsync:
	rsync -rlptoD --delete --omit-dir-times ../backend docker/expungeservice
	rsync -rlptoD --delete --omit-dir-times ../frontend/build docker/expungeservice/frontend

# build an expungeservice image with the given RS_ENV tag ('staging', 'prod', etc)
image: rsync env_check
	cd docker/expungeservice; \
		docker build . -t evictionsponge/expungeservice:$(RS_ENV)

# build prod image
prod_image: clean
	@make frontend_build backend_env_build
	@make rsync image RS_ENV=prod