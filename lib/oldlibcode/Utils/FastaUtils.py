import os

def RemoveRepeats(path,newpath):
    tmp = '/kb/module/work/tmp/tmp.fa'
    command = '/kb/deployment/bin/meme/bin/dust ' + path + ' > ' + tmp
    os.system(command)
    newFasta = ''
    with open(tmp,'r') as tmpFile:
        newFasta = ''
        sequence = ''
        first = True
        for line in tmpFile:
            if '>' in line:
                if not first:
                    newFasta += sequence + '\n'
                    sequence = ''
                else:
                    first = False 

                newFasta += line.replace('\n','') + '\n'
            else:
                sequence += line.replace('\n','')
        newFasta += sequence + '\n'
    with open(newpath,'w') as newFile:
        newFile.write(newFasta)
