#!/bin/bash

for i in protonfixes/gamefixes/*.py; do head -q -n1 "$i" |\
sed \
-e 's/"""//g' \
-e 's/\s\?Game fix\( for\)\?\s//' \
-e 's/\s\?([0-9]\+)//' \
-e "s/$/ \($(basename "$i" .py)\)/" \
-e 's/^/- /';
done | sort
