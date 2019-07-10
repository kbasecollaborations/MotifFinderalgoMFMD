#!/bin/bash
/home/manish/Desktop/reorganization/reorg/git/MotifFindermfmd/test_local/run_docker.sh run --rm -v /home/manish/Desktop/reorganization/reorg/git/MotifFindermfmd/test_local/subjobs/$1/workdir:/kb/module/work -v /home/manish/Desktop/reorganization/reorg/git/MotifFindermfmd/test_local/workdir/tmp:/kb/module/work/tmp $4 -e "SDK_CALLBACK_URL=$3" $2 async
