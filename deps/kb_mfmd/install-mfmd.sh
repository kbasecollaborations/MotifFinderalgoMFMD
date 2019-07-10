#!/bin/bash
#R CMD INSTALL /kb/deps/kb_mfmd/Rserve_1.7-3.1.tar.gz
#Rscript /kb/deps/kb_mfmd/script.R
git clone https://github.com/jadermcg/mfmd.git
pip install weblogo
R CMD INSTALL /kb/deps/kb_mfmd/Rserve_1.7-3.1.tar.gz
Rscript /kb/deps/kb_mfmd/script.R
#cd mfmd
#cd ..
