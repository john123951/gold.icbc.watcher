# -*- coding:utf-8 -*-
from util import stringUtils
from watcher.PageWatcher import PageWatcher
import Config


class ICBCWatcher(PageWatcher):
    def get_url(self):
        return 'http://www.icbc.com.cn/FinanceMarket/gold/Default.aspx'

    def process(self, document):
        str_price1 = document("#ctl00_Content_Boby_AccountGold1_Label_mrj1")
        price1 = stringUtils.getAmount(str_price1.text())
        # print('银行买入价：%s元/克' % price1)

        str_price2 = document('#ctl00_Content_Boby_AccountGold1_Label_mcj1')
        price2 = stringUtils.getAmount(str_price2.text())
        # print('银行卖出价：%s元/克' % price2)

        str_price3 = document('#ctl00_Content_Boby_AccountGold1_Label_zjj1')
        price3 = stringUtils.getAmount(str_price3.text())
        # print('中间价：%s元/克' % price3)

        # 到达设定值时，发送警告
        highest = float(Config.config.get_dict()["icbc"]["highest"])
        lowest = float(Config.config.get_dict()["icbc"]["lowest"])
        if (price1 is not None) and (price1 > highest):
            self.notify('银行买入价高于设定值%s，目前价格%s' % (highest, price1))
        if (price1 is not None) and (price1 < lowest):
            self.notify('！！！银行买入价低于设定值%s，目前价格%s' % (lowest, price1))
        pass


if __name__ == '__main__':
    icbc = ICBCWatcher()
    icbc.start()
