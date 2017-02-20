# -*- coding:utf-8 -*-
from pyquery import PyQuery as pq
from notify.PushNotify import PushNotify
import datetime


class PageWatcher(object):
    def __init__(self):
        self._push = PushNotify()
        self._lastNotifyTime = {}

    def get_url(self):
        """
        获取要监视的页面url
        :return: String
        """
        pass

    def process(self, document):
        """
        处理程序
        :param document:
        :return:
        """
        pass

    def notify(self, message):
        """
        发送通知
        :param message:
        :return:
        """
        interval = 60 * 30
        if self._get_self_name() in self._lastNotifyTime.keys():
            now = datetime.datetime.now()
            last_time = self._lastNotifyTime[self._get_self_name()]
            if (now - last_time).seconds < interval:
                return
            pass

        success = self._push.push_msg(self._get_self_name(), message)
        if success:
            self._lastNotifyTime[self._get_self_name()] = datetime.datetime.now()
            pass
        pass

    def _get_self_name(self):
        return type(self).__name__

    def start(self):
        try:
            url = self.get_url()
            document = pq(url=url)
            self.process(document)
        except Exception, ex:
            print (ex.message)
            return
