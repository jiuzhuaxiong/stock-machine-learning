# coding=utf-8
# 客户端调用，用于查看API返回结果
from OkexSpotAPI import OkexSpot
import talib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 初始化apikey，secretkey,url
apikey = 'XXXX'
secretkey = 'XXXXX'
okexRESTURL = 'www.okex.com'
# 现货API
okexSpot = OkexSpot(okexRESTURL, apikey, secretkey)

print('获取K线数据')
# 从API接口获取最新K线数据(2017-11-01起，11月之前的数据交易量过小)
kline_data_json = okexSpot.kline('btc_usdt',since='1509465600000')
print(kline_data_json)

kline_data = pd.DataFrame(kline_data_json,
                          columns=['time', 'open', 'high', 'low', 'close', 'volume'])
print('kline_data',kline_data.shape)
print('计算K线指标')
# 提取数据列
time = np.array(kline_data['time'], dtype=np.string_)
close_prices = np.array(kline_data['close'], dtype=np.double)
high_prices = np.array(kline_data['high'], dtype=np.double)
low_prices = np.array(kline_data['low'], dtype=np.double)
volumes = np.array(kline_data['volume'], dtype=np.double)

#折线图展示
plt.title('收市价格曲线')
plt.xlabel('时间')
plt.ylabel('价格')

plt.plot(time, close_prices,'r', label='收市价')
plt.grid()
plt.show()

# 通过数据计算指标
ma7_data = talib.MA(close_prices, timeperiod=7)
ma30_data = talib.MA(close_prices, timeperiod=30)
# wma_data = talib.WMA(close_prices)
# mom_data = talib.MOM(close_prices)
# stck, stcd = talib.STOCH(high_prices, low_prices, close_prices)
macd, macdsignal, macdhist = talib.MACD(close_prices)
rsi_data = talib.RSI(close_prices, timeperiod=10)
boll_upper, boll_middle, boll_lower = talib.BBANDS(close_prices)
print('macd', macd)