#! /bin/sh

cd ../build
make
sudo make install
sudo ldconfig
cd ../apps
