# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
#import MotifUtils.Utils.MotifSetUtil as MSU
#import MotifUtils.Utils.mfmdUtil as MFU
import man4ish_guptamfmd.Utils.mfmdUtil as MFU
#import mfmdUtil as MFU
from installed_clients.DataFileUtilClient import DataFileUtil

#END_HEADER


class MotifParserUtils:
    '''
    Module Name:
    MotifUtils

    Module Description:
    A KBase module: MotifUtils
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        #END_CONSTRUCTOR
        pass


    def UploadFrommfmd(self, ctx, params):
        """
        :param params: instance of type "UploadmfmdInParams" -> structure:
           parameter "path" of String, parameter "ws_name" of String,
           parameter "obj_name" of String
        :returns: instance of type "UploadOutput" -> structure: parameter
           "obj_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN UploadFrommfmd
        print('Extracting motifs')
        motifList = MFU.parse_mfmd_output(params['path'])
        print(motifList)
       
        MSO = {}
        MSO['Condition'] = 'Temp'
        MSO['SequenceSet_ref'] = '123'
        MSO['Motifs'] = []
        MSO['Alphabet'] = ['A','C','G','T']
        #MSO['Background'] = MSU.GetBackground()
        #for letter in MSO['Alphabet']:
        #    MSO['Background'][letter] = 0.0
        
        #MSU.parseMotifList(motifList,MSO)
        MSO=motifList
        '''params['min_len']=22   #put dummy value for min and max len
        params['max_len']=22
        #MSU.CheckLength(motifList,params['min_len'],params['max_len'])
        #MSU.CheckLength(MSO,params['min_len'],params['max_len'])
        
        
        for motif in MSO['Motifs']:
            print()
            for letter in MSO['Alphabet']:
                if len(motif['PWM'][letter]) != len(motif['Iupac_sequence']):
                    print('CAUGHT PWM ERROR HERE')
                    exit(1)
        if 'absolute_locations' in params:
            for motif in MSO['Motifs']:
                for loc in motif['Motif_Locations']:
                    if loc['sequence_id'] in params['absolute_locations']:
                        loc['sequence_id'] = params['contig']
                        absStart = int(params['start'])
                        loc['start'] = absStart
                        loc['end'] = absStart + loc['end']
        print("test2")'''
        
        dfu = DataFileUtil(self.callback_url)
        save_objects_params = {}
        save_objects_params['id'] = dfu.ws_name_to_id(params['ws_name'])
        save_objects_params['objects'] = [{'type': 'KBaseGeneRegulation.MotifSet' , 'data' : MSO , 'name' : params['obj_name']}]

        info = dfu.save_objects(save_objects_params)[0]
        print('SAVED OBJECT')
        print(info)
        motif_set_ref = "%s/%s/%s" % (info[6], info[0], info[4])
        print(motif_set_ref)
        output = {'obj_ref' : motif_set_ref}
        print(output)

        
        #exit("test")
        #END UploadFrommfmd

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method UploadFrommfmd return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
