#!/bin/bash

if [[ "$#" -ne 1 ]]; then
    echo "Please provide a day number argument. E.g.  ./new-day 2" >&2
    exit 1
fi

dir="./day-$1"

if [[ -d "$dir" ]]; then
    echo "The ${dir} directory already exists" >&2
    exit 2
fi

mkdir ${dir}
cp ./template.py ./${dir}/easy.py
touch ./${dir}/test-input.txt
exit 0
