import yaml

from core.AbstractConfig import AbstractConfig


class YamlConfig(AbstractConfig):
    def __init__(self, config_path):
        self.path = config_path
        with open(config_path) as fr:
            self.conf = yaml.load(fr)
        pass

    def get_dict(self):
        return self.conf
