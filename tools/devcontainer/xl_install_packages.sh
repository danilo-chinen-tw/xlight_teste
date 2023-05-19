#!/bin/bash

# Install requirements via pip
echo "*** Installing python modules ***"
sudo pip install -r tools/devcontainer/requirements.txt

# Install firebird and kinterbasdb from tar packages
cp tools/devcontainer/xlightdata_packages.tar.gz /tmp
cd /tmp
tar -xf xlightdata_packages.tar.gz

echo "*** Installing firebird ***"
tar -xf FirebirdCS-2.0.7.13318-0.amd64.tar.gz
cd FirebirdCS-2.0.7.13318-0.amd64
sudo sh install.sh -silent
cd ..

echo "*** Installing kinterbasdb ***"
tar -xf kinterbasdb.tar.gz
cd kinterbasdb
sudo python2.7 setup.py build
sudo python2.7 setup.py install

cd /workspaces/xlightdata





