VENV_NAME=devenv
PYTHON=$(VENV_NAME)/bin/python

clean:
	@echo Remove virtual environment
	@rm -rf $(VENV_NAME)

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	@test -d devenv || virtualenv $(VENV_NAME)
	@$(VENV_NAME)/bin/pip install -Ur requirements.txt
	@touch devenv/bin/activate

test:
	@$(VENV_NAME)/bin/flake8 agentpy
	@$(VENV_NAME)/bin/python setup.py test

run: venv
	@PYTHONPATH=agentpy $(PYTHON) agentpy/main.py
