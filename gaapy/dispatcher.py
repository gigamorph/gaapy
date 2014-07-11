"""Extract information from Google Analytics
"""

import os
import os.path
import sys

#APP_ROOT = os.path.dirname(os.path.realpath(__file__))
APP_ROOT = os.environ['GAAPY_HOME']
sys.path.append(APP_ROOT)

import argparse
import json
import logging
import re

from oauth2client.tools import argparser

from ga_proxy.google_auth import GoogleAuth
from ga_proxy.report_api import ReportAPI 


class Dispatcher(object):

    def __init__(self, args):
        self.app_root = APP_ROOT
        self.args = args
        
    def get_config(self):
        with open(os.path.join(self.app_root, 'config', 'config.json')) as f:
            config = json.loads(f.read())
        return config

    def get_query_params(self):
        """Each line looks like
        key = value
        with an optional end of line comment that begins with a "#".
        """

        fpath = self.args.params
        params = dict()
        with open(fpath, 'r') as f:
            for line in f:
                line2 = re.sub(r'^([^#]*)#.*$', r'\1', line) #remove comment
                m = re.match(r'\s*(\S+?)\s*=\s*(\S+)', line2)
                if m:
                    key = m.group(1)
                    value = m.group(2)
                    params[key] = value
                elif line2.strip() != '': #not a pure comment line nor an empty line
                    logging.warning('Invalid line: %s' % line)
        return params
        
    def run(self):
        config = self.get_config()
        client_secrets_path = os.path.join(self.app_root, config['client_secrets_path'])
        token_path = os.path.join(self.app_root, config['token_path'])
        auth = GoogleAuth(self.args, client_secrets_path, token_path)
        service = auth.build_service('analytics', 'v3') 
        reporter = ReportAPI(service)
                
        params = self.get_query_params()
        params['start'] = self.args.start
        params['end'] = self.args.end

        print(json.dumps(reporter.get_report(params), sort_keys=True, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[argparser])
    parser.add_argument('--params', type=str, help='File containing query parameters')
    parser.add_argument('--start', type=str, help='Start date')
    parser.add_argument('--end', type=str, help='End date')
     
    args = parser.parse_args(sys.argv[1:])
     
    dispatcher = Dispatcher(args)
    dispatcher.run()
