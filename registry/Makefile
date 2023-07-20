

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
install-dev: ${AMICLIENT_DEPEREGISTRY_DEPENDENCES_DEVNDENCES_DEV} install
	@printf "\033[0m"
	@printf "\033[32m"
	@echo "================================= INSTALL DEV ================================="
	@[ -d $(VENV_NAME) ] || ${PYTHON_VERSION} -m $(VENV_NAME) $(VENV_NAME)
	@${PIP} install pip wheel -U
	@${PIP} install -r ${REGISTRY_DEPENDENCES_DEV}
	@printf "\033[36m"
	@echo "============================== INSTALL DEV OK! ================================"
	@printf "\033[0m"


.PHONY: install-registry
install-registry: ${DEPENDENCES_REGISTRY} install
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "============================== INSTALL REGISTRY ==============================="
	@${PIP} install pip wheel -U
	@${PIP} install --editable ${REGISTRY}
	@printf "\033[36m"
	@echo "============================ INSTALL REGISTRY OK! ============================="
	@printf "\033[0m"


# Установка REGISTRY ALL
.PHONY: install-all
install-all:
	@make install-registry \
	&& make install-dev \


# Активация виртуального окружения
.PHONY: venv
venv: ${VENV_NAME}/bin/activate
$(VENV_NAME)/bin/activate: ${SETUP}
	@[ -d $(VENV_NAME) ] || ${PYTHON_VERSION} -m $(VENV_NAME) $(VENV_NAME)
	@${PIP} install pip wheel -U
	@${PIP} install -e .
	@${VENV_ACTIVATE}


# Удаление виртуального окружения
.PHONY: uninstall
uninstall:
	@printf "\033[0m"
	@printf "\033[31m"
	@echo "================================== UNINSTALL =================================="
	@make clean
	@rm -fr ${VENV_NAME}
	@printf "\033[36m"
	@echo "================================ UNINSTALL OK! ================================"
	@printf "\033[0m"


# Очистка мусора
.PHONY: clean
clean:
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "==================================== CLEAN ===================================="
	@[ -d $(RELEASE) ] || mkdir ${RELEASE}
	@[ -d $(ARCHIVE) ] || mkdir ${ARCHIVE}
	@[ -d $(DIST) ] || mkdir ${DIST}
	@rm -fr ${BUILD}
	@find . '(' -path ./$(ARCHIVE) -o -path ./${VENV_NAME} ')' \
		-prune -o '(' -name '*.tar.gz' -o -name '*.tar.xz' -o -name '*.zip' ')' \
		-type f -exec mv -v -t "$(ARCHIVE)" {} +
	@find . '(' -path ./$(ARCHIVE) -o -path ./${VENV_NAME} ')' \
		-prune -o '(' -name '*.egg-info' -o -name '.eggs' -o -name '*~' -o -name '__pycache__' ')' \
		-exec rm -fr {} +
	@find . '(' -path ./$(ARCHIVE) -o -path ./${VENV_NAME} ')' \
		-prune -o '(' -name '*.pyc' -o -name '*.pyo' -o -name '*.spec' ')' -type f -exec rm {} +
	@printf "\033[36m"
	@echo "================================== CLEAN OK! =================================="
	@printf "\033[0m"


# =============================================
# Проверка кода
.PHONY: check
check: ${PYCODESTYLE} ${PYFLAKES} ${REGISTRY}
	@printf "\033[0m"
	@printf "\033[32m"
	@echo "============================== CHECK SRC CODE ================================="
	@printf "\033[31m"
	@${PYCODESTYLE} ${REGISTRY}
	@${PYFLAKES} ${REGISTRY}
	@printf "\033[32m"
	@echo "============================ CHECK SRC CODE OK ================================"
	@printf "\033[0m"


# =============================================
# Создание релиза приложения
.PHONY: release
release: clean ${DIST} ${README}
	@printf "\033[0m"
	@printf "\033[34m"
	@echo "============================ CREATE RELEASE BIN ==============================="
	@cp -a ${DIST} ${RELEASE} \
	&& mv ${RELEASE}/${DIST} ${RELEASE}/${REGISTRY} \
	&& cp -a ${README} ${RELEASE}/${REGISTRY} \
	&& cd ${RELEASE} \
	&& tar -cvzf ${REGISTRY}-bin-${EXT_NAME}.tar.gz ${REGISTRY} \
	&& rm -fr ${REGISTRY} && cd ..
	@printf "\033[32m"
	@echo "============================ CREATE RELEASE BIN OK! ==========================="
	@printf "\033[0m"


# =============================================
# Создание релиза исходного кода REGISTRY
.PHONY: release-src
release-src: clean ${REGISTRY} ${MAKEFILE} ${MAKEFILE_DOCKER} \
			${README} ${COMPOSEFILE} ${ENVIRONMENT}
	@printf "\033[0m"
	@printf "\033[34m"
	@echo "============================ CREATE RELEASE SRC ==============================="
	@tar -cvzf ${RELEASE}/${REGISTRY}-src-${EXT_NAME}.tar.gz \
	${REGISTRY} ${MAKEFILE} ${MAKEFILE_DOCKER} ${README} ${COMPOSEFILE} \
	${REGISTRY_APPS} ${ENVIRONMENT}
	@printf "\033[32m"
	@echo "============================ CREATE RELEASE SRC OK! ==========================="
	@printf "\033[0m"


#===============================================
# Запуск приложения REGISTRY
.PHONY: list
list: ${REGISTRY} ${VENV_NAME}
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "================================ RUN REGISTRY ================================="
	@printf "\033[0m"
#	@${VENV_BIN}/${REGISTRY} list
#	@${PYTHON} -m ${REGISTRY} list
	@${PYTHON} ${REGISTRY_CLI} list
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "=============================== RUN REGISTRY OK ==============================="
	@printf "\033[0m"


# Запуск приложения REGISTRY
.PHONY: info
# info: repo?=
info: ${REGISTRY} ${VENV_NAME}
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "================================ RUN REGISTRY ================================="
	@printf "\033[0m"
#	@${VENV_BIN}/${REGISTRY} info
#	@${PYTHON} -m ${REGISTRY} info
#	@${PYTHON} ${REGISTRY_CLI} info --repo $(repo)
	@${PYTHON} ${REGISTRY_CLI} info
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "=============================== RUN REGISTRY OK ==============================="
	@printf "\033[0m"


# Запуск приложения REGISTRY
.PHONY: delete
delete: repo?=
delete: tag?=
delete: ${REGISTRY} ${VENV_NAME}
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "================================ RUN REGISTRY ================================="
#	@${VENV_BIN}/${REGISTRY} delete --repo $(repo) --tag $(tag)
#	@${PYTHON} -m ${REGISTRY} delete --repo $(repo) --tag $(tag)
	@${PYTHON} ${REGISTRY_CLI} delete --repo $(repo) --tag $(tag)
	@printf "\033[0m"
	@printf "\033[33m"
	@echo "=============================== RUN REGISTRY OK ==============================="
	@printf "\033[0m"


# Help REGISTRY
.PHONY: help
help:
	@printf "\033[0m"
	@printf "\033[36m"
	@echo "================================ HELP REGISTRY ================================"
	@echo "make list"
	@echo "make info"
	@echo "make delete repo=amiclient tag=2022-10-24-01"
	@echo "================================ HELP REGISTRY ================================"
	@printf "\033[0m"
	@exit 0


#===========================================================
# ################### Сборка приложения ####################
#===========================================================
# Сборка приложения REGISTRY непосредственно в директории проекта
.PHONY: build-apps
build-apps: ${REGISTRY} ${REGISTRY}/${REGISTRY_CLI}
	@make uninstall
	@make install-all
	@printf "\033[0m"
	@printf "\033[32m"
	@echo "================================== BUILD APP =================================="
	@${PYINSTALLER} \
		--onefile \
		--windowed \
		--name ${REGISTRY_APPS} ${REGISTRY}/${REGISTRY_CLI}
#	&& make clean \
#	&& make release \
#	&& make uninstall
	@printf "\033[36m"
	@echo "=============================== BUILD APP OK! ================================="
	@printf "\033[0m"

# ===========================================================
# Сборка приложения REGISTRY в Docker
# при таком варианте сборки вероятность не совпадения библиотекаи libc
.PHONY: build
build: ${REGISTRY} ${REGISTRY}/${REGISTRY_BUILD} ${REGISTRY}/${REGISTRY_CLI}
	@ ! [ -d $(REGISTRY_TEMP) ] || rm -fr ${REGISTRY_TEMP}
	@mkdir ${REGISTRY_TEMP} && cp ${PWD}/${REGISTRY}/${REGISTRY_BUILD} ${REGISTRY_TEMP} && \
	sed -i 's#default_user_id#${USER_ID}#' ${REGISTRY_TEMP}/${REGISTRY_BUILD} && \
	make release-src && cp -a $(RELEASE)/${REGISTRY}-*.tar.gz  $(REGISTRY_TEMP)/ && \
	cd $(REGISTRY_TEMP) && tar -xvzf ${REGISTRY}-*.tar.gz && \
	${DOCKER} run \
		--rm \
		--entrypoint /${PRE_PATH}/${REGISTRY_BUILD} \
		--volume ${REGISTRY_TEMP}:/${PRE_PATH} \
		${DOCKER_IMAGE} && \
	cp $(REGISTRY_TEMP)/${DIST}/* $(PWD)/${DIST}/ && \
	cd .. && rm -fr $(REGISTRY_TEMP)

# ===========================================================