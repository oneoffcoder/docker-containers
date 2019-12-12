#!/bin/bash
# $AUTOBUILD_HOST $AUTOBUILD_PORT
cd /sphinx && make clean && make html
/usr/local/conda/bin/python -m sphinx_autobuild \
    /sphinx/source \
    /sphinx/build \
    -b html \
    --poll \
    -H $AUTOBUILD_HOST \
    -p $AUTOBUILD_PORT

exit 0