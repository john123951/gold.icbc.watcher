#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

import schedule
import time
from src.watcher.ICBCWatcher import ICBCWatcher
from util.JsonConfig import JsonConfig

config_file_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'config', 'watcher.config')


def update_config():
    App.config = JsonConfig(config_file_path)


class App(object):
    config = None

    @classmethod
    def main(cls):
        App.config = JsonConfig(config_file_path)
        schedule.every(2).minutes.do(ICBCWatcher().start)
        schedule.every(1).hours.do(update_config)
        # schedule.every(10).minutes.do(process)
        # schedule.every().hour.do(process)
        # schedule.every().day.at("10:30").do(process)
        # schedule.every().monday.do(process)
        # schedule.every().wednesday.at("13:15").do(process)
        print('启动...OK')
        while True:
            schedule.run_pending()
            time.sleep(5)
        print('程序退出')


if __name__ == "__main__":
    App.main()
