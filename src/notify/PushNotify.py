# -*- coding:utf-8 -*-
import json
import logging
import os

import requests

from src.util.Config import Config

__author__ = 'sweet'


class PushNotify(object):
    def __init__(self):
        config_file_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], '..', 'config', 'push.config')
        self.config = Config(config_file_path)
        self.token = self.config.get('pushbullet', 'token')

    def push_msg(self, title, content):
        url = 'https://api.pushbullet.com/v2/pushes'
        req = {}
        req['type'] = 'note'
        req['title'] = title
        req['body'] = content
        data = json.dumps(req)
        logging.debug('data: ' + data)
        response = requests.post(url, data, headers={'Content-Type': 'application/json', 'Access-Token': self.token})
        result = json.loads(response.text)
        if 'iden' in result:
            return True
        return False


if __name__ == "__main__":
    push = PushNotify()
    print(push.token)
    push.push_msg('test', u'测试下')
