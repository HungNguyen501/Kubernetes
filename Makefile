ProjectName := Mrroot501-Handbook
CiScript := ci/ci.sh

readme:
	@bash $(CiScript) generate_readme

.DEFAULT_GOAL := help
.PHONY: help
all: help
help: Makefile
	@echo "Hello World!"