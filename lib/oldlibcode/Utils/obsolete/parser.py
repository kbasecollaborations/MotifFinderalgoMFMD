import sys                                                                                                      
import os                                                                                                       
import json                            
import re
def build_mfmd_command(inputFilePath, prb):                                                                     
    if not os.path.exists('/kb/module/work/tmp/mfmd'):                                                          
        os.mkdir('/kb/module/work/tmp/mfmd')                                                                    
    outputFilePath = '/kb/module/work/tmp/mfmd/mfmd_output_' + prb +  '.txt'                                    
                                                                                                                
    length = '8'                                                                                                
    parameter = '22'                                                                                            
    command = 'java -jar mfmd.jar ' + inputFilePath + ' ' + parameter + ' ' + prb + '  > ' + outputFilePath     
    return command                                                                                              
                                                                                                                
def run_mfmd_command(command):                                                                                 
    os.system(command)                                                                                          
                                                                                                                
def parse_mfmd_output(path):                                                                                   
    outputFileList = []       
    pfmMatrix=False
    for filename in os.listdir(path):    
        outputFileList.append(path + '/' + filename)
        if(filename=="mfmd_out.txt"):
           outputFilePath=path+'/'+filename
           mfmdFile = open(outputFilePath,'r') 
           for line in mfmdFile:
               if(re.search("PFM Matrix",line)):
                  pfmMatrix=True
                  '''print(line)'''
               '''if(pfmMatrix):
                  print(line)'''
               if(re.search('\d+\n\n*?', line)):
                  pfmMatrix=False
               if(re.search('seq',line)): 
                  print(line)
 
parse_mfmd_output("/home/manish/Desktop/Data/motifs/man4ish_guptamfmd/deps/kb_mfmd/mfmd/mfmd_out")
                                                                                                               

