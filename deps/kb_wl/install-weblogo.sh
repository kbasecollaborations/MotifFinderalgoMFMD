#!/bin/bash
git clone https://github.com/WebLogo/weblogo.git
cd weblogo
python setup.py build
python setup.py install
cd ..
