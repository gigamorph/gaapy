import json
import logging


class ManagementAPI(object):

    def __init__(self, service):
        self.service = service

    def get_profile_id(self, account_name, webproperty_id, profile_name):
        account = self.get_account(account_name)
        account_id = account.get('id')
        profile = self.get_profile(account_id, webproperty_id,
            profile_name)
        return profile.get('id')

    def get_account(self, account_name):
        accounts = self.service.management().accounts().list().execute()
        account_items = accounts.get('items')
        filtered = filter(lambda x: x.get('name') == account_name,
            account_items)
        count = len(filtered)
        if count == 1:
            return filtered[0]
        elif count == 0:
            return None
        else:
            raise RuntimeError('GAProxy#get_account - got %d accounts, expected 1.' % count)

    def get_webproperty(self, account_id, webproperty_id):
        webproperties = self.service.management().webproperties().list(accountId=account_id).execute()
        webproperty_items = webproperties.get('items')
        filtered = filter(lambda x: x.get('id') == webproperty_id,
            webproperty_items)
        count = len(filtered)
        if count == 1:
            return filtered[0]
        elif count == 0:
            return None
        else:
            raise RuntimeError('GAProxy#get_webproperty - got %d webproperties, expected 1.' % count)

    def get_profile(self, account_id, webproperty_id, profile_name):
        profiles = self.service.management().profiles().list(
            accountId=account_id,
            webPropertyId=webproperty_id).execute()
        profile_items = profiles.get('items')
        filtered = filter(lambda x: x.get('name') == profile_name,
            profile_items)
        count = len(filtered)
        if count == 1:
            return filtered[0]
        elif count == 0:
            return None
        else:
            raise RuntimeError('GAProxy#get_profile - got %d profiles, expected 1.' % count)
