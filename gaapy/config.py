import os
import sys

APP_ROOT = os.environ['GAAPY_HOME']
sys.path.append(APP_ROOT)

import json

from ga_proxy.google_auth import GoogleAuth


class Config(object):
    
    def __init__(self):
        with open(os.path.join(APP_ROOT, 'config', 'config.json')) as f:
            self.config = json.loads(f.read())
        
    def get_service(self, auth_flags):
        client_secrets_path = os.path.join(APP_ROOT, self.config['client_secrets_path'])
        token_path = os.path.join(APP_ROOT, self.config['token_path'])
        auth = GoogleAuth(auth_flags, client_secrets_path, token_path)
        service = auth.build_service('analytics', 'v3')
        return service
