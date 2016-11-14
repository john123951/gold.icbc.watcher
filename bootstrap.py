#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import schedule
import time

from src.watcher.ICBCWatcher import ICBCWatcher


def process():
    icbc = ICBCWatcher()
    icbc.start()


schedule.every(2).minutes.do(process)
# schedule.every(10).minutes.do(process)
# schedule.every().hour.do(process)
# schedule.every().day.at("10:30").do(process)
# schedule.every().monday.do(process)
# schedule.every().wednesday.at("13:15").do(process)

if __name__ == "__main__":
    print('启动...')
    while True:
        schedule.run_pending()
        time.sleep(5)
    print('程序退出')