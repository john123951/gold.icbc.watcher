import schedule
import time

from src.watcher.ICBCWatcher import ICBCWatcher


def process():
    icbc = ICBCWatcher()
    icbc.start()
    print('.', end='')


schedule.every(2).minutes.do(process)
# schedule.every(10).minutes.do(process)
# schedule.every().hour.do(process)
# schedule.every().day.at("10:30").do(process)
# schedule.every().monday.do(process)
# schedule.every().wednesday.at("13:15").do(process)

while True:
    schedule.run_pending()
    time.sleep(5)
