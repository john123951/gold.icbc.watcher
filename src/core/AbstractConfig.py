# coding=utf-8
from abc import abstractmethod


class AbstractConfig(object):
    """
    配置抽象类
    """

    @abstractmethod
    def get_dict(self):
        """
        获取字典
        :return: dict
        """
        return {}
