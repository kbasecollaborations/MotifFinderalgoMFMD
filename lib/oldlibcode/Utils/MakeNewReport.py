import json
import sys
import os

#Pseudo:
#copy report into directory
#write motif set to directory
#pass info back

def MakeReport(htmlDir,motifSet):
    reportPath = '/kb/module/lib/man4ish_guptamfmd/Utils/Report/*'
    CopyCommand = 'cp -r ' + reportPath + ' ' + htmlDir
    os.system(CopyCommand)
    jsonFName = htmlDir + '/ReportMotif.json'
    with open(jsonFName,'w') as motifjson:
        json.dump(motifSet,motifjson)
    return
