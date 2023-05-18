#!/bin/bash

# Install tftpy via pip
pip install tftpy==0.6.0

# Install fdb via pip
pip install fdb

# Install firebird and kinterbasdb from tar packages
cp tools/devcontainer/xlightdata_packages.tar.gz /tmp
cd /tmp
tar -xf xlightdata_packages.tar.gz

tar -xf FirebirdCS-2.0.7.13318-0.amd64.tar.gz
cd FirebirdCS-2.0.7.13318-0.amd64
sh install.sh

cd ..
tar -xf kinterbasdb.tar.gz
cd kinterbasdb
python2.7 setup.py build
python2.7 setup.py install

cd /workspaces/xlightdata





