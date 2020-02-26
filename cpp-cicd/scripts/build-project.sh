#!/bin/bash
[ -d "/project/cmake-build-debug" ] && rm -fr /project/cmake-build-debug
[ ! -d "/project/cmake-build-debug" ] && mkdir /project/cmake-build-debug
cd /project/cmake-build-debug
cmake ..
make clean
make -j $NJOBS
make ccov-all -j $NJOBS
ctest -T memcheck -j $NJOBS
make doc