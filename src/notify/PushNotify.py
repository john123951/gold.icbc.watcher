# -*- coding:utf-8 -*-
import json
import logging
import requests
import Config

__author__ = 'sweet'


class PushNotify(object):
    def __init__(self):
        self.config = Config.config
        self.token = self.config.get_dict()['pushbullet']['token']

    def push_msg(self, title, content):
        url = 'https://api.pushbullet.com/v2/pushes'
        req = {'type': 'note', 'title': title, 'body': content}
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
