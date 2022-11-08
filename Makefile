#=============================================
# Общие настройки и переменные
PYTHON_VERSION=python3
VENV_NAME?=venv
VENV_BIN=${VENV_NAME}/bin
VENV_ACTIVATE=. ${VENV_BIN}/activate
PYTHON=${VENV_BIN}/python3
PIP=${VENV_BIN}/pip3
PYINSTALLER=${VENV_BIN}/pyinstaller
PYCODESTYLE=${VENV_BIN}/pycodestyle
PYFLAKES=${VENV_BIN}/pyflakes
DOCKER=$(shell which docker)
COMPOSE=$(shell which docker-compose)
export PWD_APP=$(shell pwd)
export TIMEZONE=$(shell timedatectl status | awk '$$1 == "Time" && $$2 == "zone:" { print $$3 }')
export USER_ID=$(shell id -u `whoami`)
#
# =============================================
#

ENV=.env
export ENVFILE=$(PWD_APP)/${ENV}

ifneq ("$(wildcard $(PWD_APP)/${ENV})","")
    include ${ENVFILE}
    export ENVFILE=$(PWD_APP)/${ENV}
endif

# ===========================================================
# ################## Установка REGISTRY #####################
# ===========================================================
# Установка зависимостей
.PHONY: install
install:
	@printf "\033[0m"
	@printf "\033[32m"
	@echo "================================= INSTALL VENV ================================"
	@[ -d $(VENV_NAME) ] || ${PYTHON_VERSION} -m $(VENV_NAME) $(VENV_NAME)
	@${PIP} install pip wheel -U
	@printf "\033[36m"
	@echo "============================== INSTALL VENV OK! ==============================="
	@printf "\033[0m"


# Установка зависимостей для проверки кода
.PHONY: install-dev
install-dev: ${AMICLIENT_DEPEREGISTRY_DEPENDENCES_DEVNDENCES_DEV}
	@printf "\033[0m"
	@printf "\033[32m"
	@echo "================================= INSTALL DEV ================================="
	@[ -d $(VENV_NAME) ] || python3 -m $(VENV_NAME) $(VENV_NAME)
	@${PIP} install pip wheel -U
	@${PIP} install -r ${REGISTRY_DEPENDENCES_DEV}
	@printf "\033[36m"
	@echo "============================== INSTALL DEV OK! ================================"
	@printf "\033[0m"


.PHONY: install-registry
install-registry: ${DEPENDENCES_REGISTRY} install
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "============================== INSTALL REGISTRY =============================="
	@${PIP} install pip wheel -U
	@${PIP} install --editable ${REGISTRY}
	@printf "\033[36m"
	@echo "============================ INSTALL REGISTRY OK! ============================"
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


# =============================================
# Проверка кода
.PHONY: check
check: ${PYCODESTYLE} ${PYFLAKES} ${REGISTRY}
	@printf "\033[0m"
	@printf "\033[31m"
	@echo "============================== CHECK SRC CODE ================================="
	${PYCODESTYLE} ${REGISTRY} ${REGISTRY_CLI}
	${PYFLAKES} ${REGISTRY} ${REGISTRY_CLI}
	@printf "\033[32m"
	@echo "============================ CHECK SRC CODE OK ================================"
	@printf "\033[0m"



#===============================================
# Запуск приложения REGISTRY
.PHONY: run-registry-repo
run-registry-repo: ${REGISTRY} ${VENV_NAME}
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "================================ RUN REGISTRY ================================="
	@printf "\033[0m"
#	@${VENV_BIN}/${REGISTRY} repo
#	@${PYTHON} -m ${REGISTRY} repo
	@${PYTHON} ${REGISTRY_CLI} repo

# Запуск приложения REGISTRY
.PHONY: run-registry-info
run-registry-info: ${REGISTRY} ${VENV_NAME}
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "================================ RUN REGISTRY ================================="
	@printf "\033[0m"
#	@${VENV_BIN}/${REGISTRY} info
#	@${PYTHON} -m ${REGISTRY} info
	@${PYTHON} ${REGISTRY_CLI} info

# Запуск приложения REGISTRY
.PHONY: run-registry-delete
run-registry-delete: repo?=
run-registry-delete: tag?=
run-registry-delete: ${REGISTRY} ${VENV_NAME}
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "================================ RUN REGISTRY ================================="
	@printf "\033[0m"
#	@${VENV_BIN}/${REGISTRY} delete --repo $(repo) --tag $(tag)
#	@${PYTHON} -m ${REGISTRY} delete --repo $(repo) --tag $(tag)
	@${PYTHON} ${REGISTRY_CLI} delete --repo $(repo) --tag $(tag)


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
	@${DOCKER} rmi registry


# Лог Portainer в Docker
log: ${DOCKER} ${COMPOSE_FILE}
	@${COMPOSE} -f ${COMPOSE_FILE} logs --follow

# ===========================================================
