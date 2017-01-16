import json
import os

from core.AbstractConfig import AbstractConfig

__author__ = 'sweet'


# rootDir = os.path.join(os.path.split(os.path.realpath(__file__))[0], '..')
# config_path = os.path.join(rootDir, 'config', 'autosign.conf')


class JsonConfig(AbstractConfig):
    def __init__(self, config_path):
        self.path = config_path
        with open(config_path) as fr:
            self.conf = json.loads(fr.read())  # ConfigParser.ConfigParser()
        pass

    def get(self, section, option):
        result = self.conf[section][option]
        return result

    def get_dict(self):
        return self.conf


if __name__ == "__main__":
    print(os.path.expanduser('~/.myapp.cfg'))
    print(os.path.expanduser('.myapp.cfg'))
    rootDir = os.path.join(os.path.split(os.path.realpath(__file__))[0], '..')
    print(rootDir)
    # strJson = r'{"name":"test","age":18}'
    # j = json.loads(strJson)
    # print(dir(j))
    # print(type(j))
    # print('age' in j.keys())
    # print(getattr(j, 'age'))
    pass
