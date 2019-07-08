# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser

from pprint import pprint

from MotifFindermfmd.MotifFindermfmdImpl import MotifFindermfmd
from MotifFindermfmd.MotifFindermfmdServer import MethodContext
from MotifFindermfmd.authclient import KBaseAuth as _KBaseAuth

from installed_clients.WorkspaceClient import Workspace


class MotifFindermfmdTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = os.environ.get('KB_AUTH_TOKEN', None)
        config_file = os.environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('MotifFindermfmd'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'MotifFindermfmd',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = Workspace(cls.wsURL)
        cls.serviceImpl = MotifFindermfmd(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')
           
    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_MotifFindermfmd_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx        

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_mfmd(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
        params = {
            'workspace_name': 'man4ish_gupta:narrative_1559788829014',
            'SS_ref' : '29476/5/1',
            'motif_length':10,
            'prb':0.05,
            'obj_name':'mfmd_obj',
            'background_group': {'background' : 0, 'genome_ref' : '29476/2/1'},
            'mask_repeats' : 1
        }


        result = self.getImpl().DiscoverMotifsFromSequenceSet(self.getContext(),params)
        print('RESULT:')
        pprint(result) 
