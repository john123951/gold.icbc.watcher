from pyquery import PyQuery as pq

from src.util import stringUtils

doc = pq(url='http://www.icbc.com.cn/FinanceMarket/gold/Default.aspx')
strPrice1 = doc("#ctl00_Content_Boby_AccountGold1_Label_mrj1")
price1 = stringUtils.getAmount(strPrice1.text())
print('银行买入价：' + price1 + '元/克')

strPrice2 = doc('#ctl00_Content_Boby_AccountGold1_Label_mcj1')
price2 = stringUtils.getAmount(strPrice2.text())
print('银行卖出价：' + price2 + '元/克')

strPrice3 = doc('#ctl00_Content_Boby_AccountGold1_Label_zjj1')
price3 = stringUtils.getAmount(strPrice3.text())
print('中间价：' + price3 + '元/克')

