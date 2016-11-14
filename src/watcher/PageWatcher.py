from pyquery import PyQuery as pq

from src.notify.PushNotify import PushNotify


class PageWatcher(object):
    def __init__(self):
        self.push = PushNotify()

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
        self.push.push_msg(type(self).__name__, message)
        pass

    def start(self):
        url = self.get_url()
        document = pq(url=url)
        self.process(document)
