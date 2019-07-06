import subprocess
import os

def BuildBackground(fastapath):
    mfmdpath = '/kb/module/work/tmp/mfmd_background.fa'
    backgroundCommand = 'mv ' + fastapath + ' ' + mfmdpath

    try:
        out_txt = subprocess.check_output(backgroundCommand,shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        print('************GET BACKGROUND ERROR************\n')
        print(e.returncode)
        exit(0)
    assert os.path.isfile(mfmdpath)
