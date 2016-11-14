from src.watcher.PageWatcher import PageWatcher
from src.util import stringUtils


class ICBCWatcher(PageWatcher):
    def get_url(self):
        return 'http://www.icbc.com.cn/FinanceMarket/gold/Default.aspx'

    def process(self, document):
        strPrice1 = document("#ctl00_Content_Boby_AccountGold1_Label_mrj1")
        price1 = stringUtils.getAmount(strPrice1.text())
        # print('银行买入价：%s元/克' % price1)

        strPrice2 = document('#ctl00_Content_Boby_AccountGold1_Label_mcj1')
        price2 = stringUtils.getAmount(strPrice2.text())
        # print('银行卖出价：%s元/克' % price2)

        strPrice3 = document('#ctl00_Content_Boby_AccountGold1_Label_zjj1')
        price3 = stringUtils.getAmount(strPrice3.text())
        # print('中间价：%s元/克' % price3)

        # 到达设定值时，发送警告
        highest = float(270)
        lowest = float(260)
        if price1 > highest:
            icbc.notify('银行买入价高于设定值%s，目前价格%s' % (highest, price1))
        if price1 < lowest:
            icbc.notify('！！！银行买入价低于设定值%s，目前价格%s' % (lowest, price1))
        pass


if __name__ == '__main__':
    icbc = ICBCWatcher()
    icbc.start()
