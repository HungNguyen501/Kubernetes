#!/bin/bash

pre_commit_file_content="#!/bin/sh

make readme

"

create_precommit_file() {
    echo "${pre_commit_file_content}" > .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
    git config --local core.hooksPath .git/hooks/
}

# Execute function
$*
