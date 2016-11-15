import datetime

interval = 60 * 30
_lastNotifyTime = {}


def _get_self_name():
    return "key"


def test():
    if _get_self_name() in _lastNotifyTime.keys():
        now = datetime.datetime.now()
        last_time = _lastNotifyTime[_get_self_name()]
        if (now - last_time).seconds < interval:
            return
        pass

    success = True
    if success:
        _lastNotifyTime[_get_self_name()] = datetime.datetime.now()
        pass
    pass


if __name__ == "__main__":
    print('start')
    test()
    test()
