import os

from util.YamlConfig import YamlConfig


def yaml_test():
    config_file_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], '..', 'config', 'watcher.config')
    config = YamlConfig(config_file_path)
    dir(config.__dict__)


if __name__ == "__main__":
    yaml_test()
