#!/bin/bash
R CMD INSTALL /kb/module/deps/kb_mfmd/Rserve_1.7-3.1.tar.gz
Rscript /kb/module/deps/kb_mfmd/script.R
git clone https://github.com/jadermcg/mfmd.git
#pip install weblogo
#cd mfmd
#java -jar mfmd.jar dataset_crp.fasta 22 0.005    //system call
cd ..
