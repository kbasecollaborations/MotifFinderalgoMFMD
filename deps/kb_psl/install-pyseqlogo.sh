#!/bin/bash

pip install pyBigWig
pip install --upgrade numpy
#mkdir /tmp/python-eggs
#export PYTHON_EGG_CACHE = /tmp/python-eggs
#sudo easy_install six=1.10
#sudo easy_install matplotlib
#pip uninstall six
pip install six
pip install --upgrade matplotlib==2.1.0
pip install pandas
python ChanePath.py
git clone https://github.com/saketkc/pyseqlogo.git
cd pyseqlogo
python setup.py build
python setup.py install
cd ..
