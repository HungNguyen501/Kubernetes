ProjectName := Mrroot501-Handbook
CiScript := ci/ci.sh
GithookScript := ci/githooks.sh

readme:
	@bash $(CiScript) generate_readme

init:
	@bash $(GithookScript) create_precommit_file

.DEFAULT_GOAL := help
.PHONY: help
all: help
help: Makefile
	@echo "Hello World!"