#!/bin/bash
script_dir=$(dirname "$(readlink -f "$0")")
export PYTHONPATH=$script_dir/../lib:$PATH:$PYTHONPATH
python -u $script_dir/../lib/man4ish_guptamfmd/man4ish_guptamfmdServer.py $1 $2 $3
