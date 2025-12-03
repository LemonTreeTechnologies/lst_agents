# Makefile

HOOKS_DIR = .git/hooks

.PHONY: clean
clean: clean-build clean-pyc clean-test clean-docs

.PHONY: clean-build
clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr deployments/build/
	rm -fr deployments/Dockerfiles/open_aea/packages
	rm -fr pip-wheel-metadata
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +
	find . -name '*.svn' -exec rm -fr {} +
	find . -name '*.db' -exec rm -fr {} +
	rm -fr .idea .history
	rm -fr venv

.PHONY: clean-docs
clean-docs:
	rm -fr site/

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test:
	rm -fr .tox/
	rm -f .coverage
	find . -name ".coverage*" -not -name ".coveragerc" -exec rm -fr "{}" \;
	rm -fr coverage.xml
	rm -fr htmlcov/
	rm -fr .hypothesis
	rm -fr .pytest_cache
	rm -fr .mypy_cache/
	find . -name 'log.txt' -exec rm -fr {} +
	find . -name 'log.*.txt' -exec rm -fr {} +

.PHONY: hashes
hashes: clean
	poetry run autonomy packages lock
	poetry run autonomy push-all

lint:
	poetry run adev -v -n 0 lint
	poetry run adev -v -n 0 lint -p scripts

fmt: 
	poetry run adev -n 0 fmt
	poetry run adev -v -n 0 fmt -p scripts

test: clean
	poetry run autonomy packages lock
	poetry run adev -n 1 -v test

install:
	@echo "Setting up Git hooks..."

	# Create symlinks for pre-commit and pre-push hooks
	cp scripts/pre_commit_hook.sh $(HOOKS_DIR)/pre-commit
	cp scripts/pre_push_hook.sh $(HOOKS_DIR)/pre-push
	chmod +x $(HOOKS_DIR)/pre-commit
	chmod +x $(HOOKS_DIR)/pre-push
	@echo "Git hooks have been installed."
	@echo "Installing dependencies..."
	bash install.sh
	@echo "Dependencies installed."
	@echo "Syncing packages..."
	poetry run autonomy packages sync
	@echo "Packages synced."

sync:
	git pull
	poetry run autonomy packages sync

contracts:
	poetry run scripts/generate_contracts.sh


metadata:

	adev metadata generate . contract/eightballer/amb_mainnet/0.1.0 03
	adev -v metadata validate mints/03.json

	adev metadata generate . contract/eightballer/amb_gnosis/0.1.0 04
	adev -v metadata validate mints/04.json

	adev metadata generate . contract/eightballer/amb_gnosis_helper/0.1.0 05
	adev -v metadata validate mints/05.json

	adev metadata generate . contract/lstolas/lst_distributor/0.1.0 06
	adev -v metadata validate mints/06.json
	adev metadata generate . contract/lstolas/lst_activity_module/0.1.0 07
	adev -v metadata validate mints/07.json
	adev metadata generate . contract/lstolas/lst_staking_manager/0.1.0 08
	adev -v metadata validate mints/08.json
	adev metadata generate . contract/lstolas/lst_staking_processor_l2/0.1.0 09
	adev -v metadata validate mints/09.json
	adev metadata generate . contract/lstolas/lst_unstake_relayer/0.1.0 10
	adev -v metadata validate mints/10.json
	adev metadata generate . contract/lstolas/lst_collector/0.1.0 11
	adev -v metadata validate mints/11.json
	adev metadata generate . contract/lstolas/lst_staking_token_locked/0.1.0 12
	adev -v metadata validate mints/12.json

	adev metadata generate . agent/lstolas/lst_agent/0.1.0 02
	adev -v metadata validate mints/02.json

	adev metadata generate . skill/lstolas/lst_skill/0.1.0 01
	adev -v metadata validate mints/01.json



	adev metadata generate . agent/lstolas/lst_agent_prod/0.1.0 13
	adev -v metadata validate mints/13.json

	adev metadata generate . service/lstolas/lst_service/0.1.0 14
	adev -v metadata validate mints/14.json



typecheck:
	poetry run pyright packages/lstolas/skills/lst_skill/

release:
	poetry run adev release

all: fmt lint typecheck test
