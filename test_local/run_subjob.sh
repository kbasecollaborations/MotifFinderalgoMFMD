#!/bin/bash
/home/manish/Desktop/Data/motifs/man4ish_guptamfmd/test_local/run_docker.sh run --rm -v /home/manish/Desktop/Data/motifs/man4ish_guptamfmd/test_local/subjobs/$1/workdir:/kb/module/work -v /home/manish/Desktop/Data/motifs/man4ish_guptamfmd/test_local/workdir/tmp:/kb/module/work/tmp $4 -e "SDK_CALLBACK_URL=$3" $2 async
