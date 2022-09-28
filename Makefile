.PHONY: help build start stop log remove


#=============================================
SOURCE=registry
RELEASE=release
DOCKER=$(shell which docker)
DOCKERFILE=Dockerfile
MAKEFILE=Makefile
README=README.md
REGISTRYDIR=/var/data/registry
COMPOSE=$(shell which docker-compose)
COMPOSE_FILE=docker-compose.yml

#=============================================
.DEFAULT: help

#=============================================

help:
	@echo "make build	- Building Registry"
	@echo "make start	- Start Registry"
	@echo "make stop	- Stopping Registry"
	@echo "make log	- Output of logs for Registry"
	@echo "make remove	- Deleting a Registry"

#=============================================
# Создание релиза приложения
release: clean
	mkdir ${RELEASE}
	zip -r ${RELEASE}/${SOURCE}-$(shell date '+%Y-%m-%d').zip \
	${COMPOSE_FILE} ${DOCKERFILE} ${MAKEFILE} ${README}


# Удаление старого релиза
clean:
	rm -fr ${RELEASE}

#=============================================
# # Сборка Registry в Docker
# build: ${DOCKER} ${COMPOSE_FILE}
# 	[ -d ${REGISTRYDIR} ] || sudo mkdir -p ${REGISTRYDIR}
# 	${COMPOSE} -f ${COMPOSE_FILE} build


# Старт Registry в Docker
start: ${DOCKER} ${COMPOSE_FILE}
	[ -d ${REGISTRYDIR} ] || sudo mkdir -p ${REGISTRYDIR}
	[ `${DOCKER} ps | grep ${SOURCE} | wc -l` -eq 1 ] || \
	${COMPOSE} -f ${COMPOSE_FILE} up -d


# Стop Registry в Docker
stop: ${DOCKER} ${COMPOSE_FILE}
	! [ `${DOCKER} ps | grep ${SOURCE} | wc -l` -eq 1 ] || \
	${COMPOSE} -f ${COMPOSE_FILE} down


# Рестарт Registry в Docker
restart: ${DOCKER} ${COMPOSE} ${COMPOSE_FILE}
	make stop
	sleep 3
	make start


# Удаление Registry в Docker
remove: ${DOCKER} ${COMPOSE_FILE}
	make stop
	${DOCKER} rmi registry


# Лог Portainer в Docker
log: ${DOCKER} ${COMPOSE_FILE}
	! [ `${DOCKER} ps | grep ${SOURCE} | wc -l` -eq 1 ] || \
	${COMPOSE} -f ${COMPOSE_FILE} logs --follow

#=============================================

