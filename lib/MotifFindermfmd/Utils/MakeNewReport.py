import json
import sys
import os

class MakeNewReport:
  def __init__(self):
      pass

  def MakeReport(self, htmlDir, motifSet):
      '''

      :param htmlDir:
      :param motifSet:
      :return:
      '''
      reportPath = '/kb/module/lib/MotifFindermfmd/Utils/Report/*'
      CopyCommand = 'cp -r ' + reportPath + ' ' + htmlDir
      os.system(CopyCommand)
      jsonFName = htmlDir + '/ReportMotif.json'
      with open(jsonFName,'w') as motifjson:
          json.dump(motifSet,motifjson)
      return
