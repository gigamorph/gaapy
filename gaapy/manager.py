"""Using Google Analytics Management API
"""

import os
import sys

#APP_ROOT = os.path.dirname(os.path.realpath(__file__))
APP_ROOT = os.environ['GAAPY_HOME']
sys.path.append(APP_ROOT)

import argparse
import logging

from oauth2client.tools import argparser

from ga_proxy.management_api import ManagementAPI
from gaapy.config import Config 


class Manager(object):

    def __init__(self, args):
        self.args = args
        
    def run(self, command, *rest):
        config = Config()
        service = config.get_service(self.args)
        api = ManagementAPI(service)
        if command == 'get_profile':
            print api.get_profile(account_id=rest[0],
                                  webproperty_id=rest[1],
                                  profile_name=rest[2])
        elif command == 'delete_profile':
            api.delete_profile(account_id=rest[0],
                               webproperty_id=rest[1],
                               profile_name=rest[2])
        else:
            print 'Command not recognized: %s' % command
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[argparser])
    parser.add_argument('command', type=str, help='command')
    parser.add_argument('command_args', type=str, nargs='*', help='optional arguments to command')
     
    args = parser.parse_args(sys.argv[1:])
     
    manager = Manager(args)
    manager.run(args.command, *args.command_args)
