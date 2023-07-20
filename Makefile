# ===========================================================

# Общие настройки и переменные
APPS_DIR=registry
ENVIRONMENT=.env
ENVIRONMENT_APPS=.setting

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
export EXT_NAME=$(shell date '+%Y-%m-%d-%H-%M-%S')
export TIMEZONE=$(shell timedatectl status | awk '$$1 == "Time" && $$2 == "zone:" { print $$3 }')
export USER_ID=$(shell id -u `whoami`)

# ===========================================================

ENVFILE_APPS=$(PWD_APP)/$(APPS_DIR)/${ENVIRONMENT_APPS}
ifneq ("$(wildcard $(ENVFILE_APPS))","")
    include ${ENVFILE_APPS}
    export ENVFILE_APPS=$(PWD_APP)/$(APPS_DIR)/${ENVIRONMENT_APPS}
endif

ENVFILE=$(PWD_APP)/${ENVIRONMENT}
ifneq ("$(wildcard $(ENVFILE))","")
    include ${ENVFILE}
    export ENVFILE=$(PWD_APP)/${ENVIRONMENT}
endif

# ===========================================================

# REGISTRY
ifneq ("$(wildcard $(PWD_APP)/${APPS_DIR}/${MAKEFILE})","")
   include ${APPS_DIR}/${MAKEFILE}
endif

# ===========================================================

# REGISTRY DOCKER
ifneq ("$(wildcard $(PWD_APP)/$(MAKEFILE_DOCKER))","")
    include ${MAKEFILE_DOCKER}
endif

# ===========================================================
