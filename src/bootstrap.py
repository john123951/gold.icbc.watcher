#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import os
import Config

from apscheduler.schedulers.blocking import BlockingScheduler
from util.JsonConfig import JsonConfig
from watcher.ICBCWatcher import ICBCWatcher

config_file_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], '..', 'config', 'watcher.config')


def update_config():
    Config.config = JsonConfig(config_file_path)


class App(object):
    @classmethod
    def main(cls):
        update_config()
        print('启动...')
        scheduler = BlockingScheduler()
        scheduler.add_job(ICBCWatcher().start, trigger="cron", minute="*/2", hour="7-23", day_of_week="0-4")
        scheduler.start()
        print('程序退出')


if __name__ == "__main__":
    App.main()
