.PHONY: help build start stop log remove


#=============================================
# Общие настройки и переменные
DOCKER=$(shell which docker)
COMPOSE=$(shell which docker-compose)
VENV_NAME?=venv
VENV_BIN=${VENV_NAME}/bin
VENV_ACTIVATE=. ${VENV_BIN}/activate
PYTHON=${VENV_BIN}/python3
PIP=${VENV_BIN}/pip3
ARCHIVE=archive
DOCKERFILE=Dockerfile
MAKEFILE=Makefile
README=README.md
COMPOSE_FILE=docker-compose.yml
SETUP_FILE=setup.py
#
export REGISTRY=registry
export REGISTRY_HOST=192.168.62.148
export REGISTRY_PORT=5000
export REGISTRY_DIR=/var/data/registry

# ===========================================================
# ################## Установка приложения ##################
# ===========================================================
.PHONY: install
install:
	@printf "\033[0m"
	@printf "\033[32m"
	@echo "================================= INSTALL REGISTRY ================================="
	@[ -d $(VENV_NAME) ] || python3 -m $(VENV_NAME) $(VENV_NAME)
	@${PIP} install pip wheel -U
	@printf "\033[36m"
	@echo "============================== INSTALL REGISTRY OK! ================================"
	@printf "\033[0m"


# Активация виртуального окружения
.PHONY: venv
venv: ${VENV_NAME}/bin/activate
$(VENV_NAME)/bin/activate: ${SETUP}
	@[ -d $(VENV_NAME) ] || python3 -m $(VENV_NAME) $(VENV_NAME)
	@${PIP} install pip wheel -U
	@${PIP} install -e .
	@${VENV_ACTIVATE}

# Удаление виртуального окружения
.PHONY: uninstall
uninstall:
	@printf "\033[0m"
	@printf "\033[31m"
	@echo "=================================== UNINSTALL ======================================"
	@make clean
	@rm -fr ${VENV_NAME}
	@printf "\033[36m"
	@echo "================================= UNINSTALL OK! ===================================="
	@printf "\033[0m"

# Очистка мусора
.PHONY: clean
clean:
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "====================================== CLEAN ======================================="
	@[ -d ${ARCHIVE} ] || mkdir ${ARCHIVE}
	@find . '(' -path ${ARCHIVE} -o -path ${VENV_NAME} ')' -prune -o '(' -name '*.tar.xz' -o -name '*.zip' ')' -type f -exec mv -v -t "$(ARCHIVE)" {} +
	@find . '(' -path ${ARCHIVE} -o -path ${VENV_NAME} ')' -prune -o '(' -name '.eggs' -o -name '*~' -o -name '__pycache__' ')' -exec rm -fr {} +
	@find . '(' -path ${ARCHIVE} -o -path ${VENV_NAME} ')' -prune -o '(' -name '*.egg-info' -o -name '*.pyc' -o -name '*.pyo' -o -name '*.spec' ')' -type f -exec rm {} +
	@printf "\033[36m"
	@echo "==================================== CLEAN OK! ====================================="
	@printf "\033[0m"


# ===========================================================
# Старт Registry
start: ${DOCKER} ${COMPOSE_FILE}
	@${COMPOSE} -f ${COMPOSE_FILE} up -d


# Стop Registry
stop: ${DOCKER} ${COMPOSE_FILE}
	@${COMPOSE} -f ${COMPOSE_FILE} down


# Рестарт Registry
restart: ${DOCKER} ${COMPOSE} ${COMPOSE_FILE}
	@make stop
	@sleep 3
	@make start

# Удаление Registry
remove: ${DOCKER} ${COMPOSE_FILE}
#	@make stop
	${DOCKER} rmi registry


# Лог Portainer в Docker
log: ${DOCKER} ${COMPOSE_FILE}
	${COMPOSE} -f ${COMPOSE_FILE} logs --follow

# ===========================================================
