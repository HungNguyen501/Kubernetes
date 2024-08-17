#!/bin/bash

PYTHON="python3"

generate_readme() {
    ${PYTHON} -m flake8 ci/ --show-source --statistics && ${PYTHON} -m pylint ci/
    items=$(find -name "README.md")
    output=$(${PYTHON} ci/readme_maker.py $(echo ${items} | sed 's/ /,/g'))
    if [ $? == 0 ];
    then
        echo "${output}" > README.md
    else
        echo ${output}
    fi
}
$*
