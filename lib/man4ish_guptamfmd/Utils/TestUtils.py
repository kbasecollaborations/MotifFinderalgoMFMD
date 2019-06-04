import os

def GetGenome(targetpath):
    localgenomepath = '/kb/data/Ptrichocarpa_444_v3.1.fa.assembly.fa'
    command = 'cp ' + localgenomepath + ' ' + targetpath
    os.system(command)
