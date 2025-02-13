# money-maker
Investment app that helps you make money.

## To run Jupyter:
```
uv run jupyter lab
```

 |  
 |  ----------------------------------------------------------------------
 |  Readonly properties defined here:
 |  
 |  actions
 |  
 |  analyst_price_targets
 |  
 |  balance_sheet
 |  
 |  balancesheet
 |  
 |  calendar
 |      Returns a dictionary of events, earnings, and dividends for the ticker
 |  
 |  capital_gains
 |  
 |  cash_flow
 |  
 |  cashflow
 |  
 |  dividends
 |  
 |  earnings
 |  
 |  earnings_dates
 |  
 |  earnings_estimate
 |  
 |  earnings_history
 |  
 |  eps_revisions
 |  
 |  eps_trend
 |  
 |  fast_info
 |  
 |  financials
 |  
 |  funds_data
 |  
 |  growth_estimates
 |  
 |  history_metadata
 |  
 |  income_stmt
 |  
 |  incomestmt
 |  
 |  info
 |  
 |  insider_purchases
 |  
 |  insider_roster_holders
 |  
 |  insider_transactions
 |  
 |  institutional_holders
 |  
 |  isin
 |  
 |  major_holders
 |  
 |  mutualfund_holders
 |  
 |  news
 |  
 |  options
 |  
 |  quarterly_balance_sheet
 |  
 |  quarterly_balancesheet
 |  
 |  quarterly_cash_flow
 |  
 |  quarterly_cashflow
 |  
 |  quarterly_earnings
 |  
 |  quarterly_financials
 |  
 |  quarterly_income_stmt
 |  
 |  quarterly_incomestmt
 |  
 |  recommendations
 |  
 |  recommendations_summary
 |  
 |  revenue_estimate
 |  
 |  sec_filings
 |  
 |  shares
 |  
 |  splits
 |  
 |  sustainability
 |  
 |  upgrades_downgrades
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from yfinance.base.TickerBase:
 |  
 |  get_actions(self, proxy=None) -> pandas.core.series.Series
dividen dates and stock splits

 |  get_analyst_price_targets(self, proxy=None) -> dict
 |      Keys:   current  low  high  mean  median
price targets

 |  get_balancesheet(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
 |  get_balance_sheet(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
 |      :Parameters:
 |          as_dict: bool
 |              Return table as Python dict
 |              Default is False
 |          pretty: bool
 |              Format row names nicely for readability
 |              Default is False
 |          freq: str
 |              "yearly" or "quarterly"
 |              Default is "yearly"
 |          proxy: str
 |              Optional. Proxy server URL scheme
 |              Default is None
 |  
 |  
 |  get_calendar(self, proxy=None) -> dict
Earnings Date [datetime.date(2025, 4, 23), datetime.date(2025, 5, 3)]
Earnings High 0.82
Earnings Low 0.24
Earnings Average 0.52124
Revenue High 27069000000
Revenue Low 21538000000
Revenue Average 23976313660

 |  get_capital_gains(self, proxy=None) -> pandas.core.series.Series
? Broken ?

 |  get_cashflow(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
 |  get_cash_flow(self, proxy=None, as_dict=False, pretty=False, freq='yearly') -> Union[pandas.core.frame.DataFrame, dict]
 |      :Parameters:
 |          as_dict: bool
 |              Return table as Python dict
 |              Default is False
 |          pretty: bool
 |              Format row names nicely for readability
 |              Default is False
 |          freq: str
 |              "yearly" or "quarterly"
 |              Default is "yearly"
 |          proxy: str
 |              Optional. Proxy server URL scheme
 |              Default is None

 |  
 |  get_dividends(self, proxy=None) -> pandas.core.series.Series
 |  
 |  get_earnings(self, proxy=None, as_dict=False, freq='yearly')
 |      :Parameters:
 |          as_dict: bool
 |              Return table as Python dict
 |              Default is False
 |          freq: str
 |              "yearly" or "quarterly"
 |              Default is "yearly"
 |          proxy: str
 |              Optional. Proxy server URL scheme
 |              Default is None
Just like the name sounds

 |  get_earnings_dates(self, limit=12, proxy=None) -> Optional[pandas.core.frame.DataFrame]
 |      Get earning dates (future and historic)
 |      
 |      Args:
 |          limit (int): max amount of upcoming and recent earnings dates to return.
 |              Default value 12 should return next 4 quarters and last 8 quarters.
 |              Increase if more history is needed.
 |          proxy: requests proxy to use.
 |      
 |      Returns:
 |          pd.DataFrame
Just like the name sounds

 |  get_earnings_estimate(self, proxy=None, as_dict=False)
 |      Index:      0q  +1q  0y  +1y
 |      Columns:    numberOfAnalysts  avg  low  high  yearAgoEps  growth

 |  get_earnings_history(self, proxy=None, as_dict=False)
 |      Index:      pd.DatetimeIndex
 |      Columns:    epsEstimate  epsActual  epsDifference  surprisePercent

 |  
 |  get_eps_trend(self, proxy=None, as_dict=False)
 |      Index:      0q  +1q  0y  +1y
 |      Columns:    current  7daysAgo  30daysAgo  60daysAgo  90daysAgo
Just like the name sounds

 |  get_fast_info(self, proxy=None)
[('currency', 'USD'),
 ('dayHigh', 346.3999938964844),
 ('dayLow', 329.1199951171875),
 ('exchange', 'NMS'),
 ('fiftyDayAverage', 401.7293994140625),
 ('lastPrice', 336.510009765625),
 ('lastVolume', 104520600),
 ('marketCap', 1082391155074.6875),
 ('open', 329.94000244140625),
 ('previousClose', 326.93),
 ('quoteType', 'EQUITY'),
 ('regularMarketPreviousClose', 328.5),
 ('shares', 3216519936),
 ('tenDayAverageVolume', 83848410),
 ('threeMonthAverageVolume', 83828873),
 ('timezone', 'America/New_York'),
 ('twoHundredDayAverage', 270.4983000946045),
 ('yearChange', 0.7832123246959583),
 ('yearHigh', 488.5400085449219),
 ('yearLow', 138.8000030517578)]

 |  get_financials(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
? Seems like income statement ?
 |  
 |  get_growth_estimates(self, proxy=None, as_dict=False)
 |      Index:      0q  +1q  0y  +1y +5y -5y
 |      Columns:    stock  industry  sector  index
? Percent of how much they expect it to grow ?
 |  
 |  get_income_stmt(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
 |  get_incomestmt(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
 |      :Parameters:
 |          as_dict: bool
 |              Return table as Python dict
 |              Default is False
 |          pretty: bool
 |              Format row names nicely for readability
 |              Default is False
 |          freq: str
 |              "yearly" or "quarterly"
 |              Default is "yearly"
 |          proxy: str
 |              Optional. Proxy server URL scheme
 |              Default is None
 |  
Just like it sounds

 |  get_info(self, proxy=None) -> dict
industry 
previousClose 
trailingPE 161.00958
forwardPE 89.281975
volume 103935563
regularMarketVolume 103935563
averageVolume 82773476
averageVolume10days 80199710
averageDailyVolume10Day 80199710
bid 330.0
ask 348.0
bidSize 100
askSize 100
marketCap 1082391134208
fiftyTwoWeekLow 138.8
fiftyTwoWeekHigh 488.54
fiftyDayAverage 401.657
twoHundredDayAverage 269.66666
profitMargins 0.13075
recommendationMean 2.74468
recommendationKey hold
numberOfAnalystOpinions 42
totalCash 33648001024
totalCashPerShare 10.482
ebitda 13244000256
totalDebt 12782999552
quickRatio 1.214
currentRatio 1.844
totalRevenue 97150001152
debtToEquity 18.078
revenuePerShare 30.457
returnOnAssets 0.04759
returnOnEquity 0.20389
grossProfits 17709000704
freeCashflow 676625024
operatingCashflow 14478999552
earningsGrowth 0.17
revenueGrowth 0.078
grossMargins 0.18229

 |  
 |  get_major_holders(self, proxy=None, as_dict=False)
Percent of insiders/institutions own the shares

 |  get_mutualfund_holders(self, proxy=None, as_dict=False)
List of index funds that has this stock

 |  get_news(self, count=10, tab='news', proxy=None) -> list
 |      Allowed options for tab: "news", "all", "press releases
As the name implies

 |  
 |  get_recommendations_summary(self, proxy=None, as_dict=False)
How many recommend buy/hold/sell

 |  get_revenue_estimate(self, proxy=None, as_dict=False)
 |      Index:      0q  +1q  0y  +1y
 |      Columns:    numberOfAnalysts  avg  low  high  yearAgoRevenue  growth
As the name implies
don't do dict

 |  get_sec_filings(self, proxy=None) -> dict
Just like the name

 |  get_shares_full(self, start=None, end=None, proxy=None)
Get num of shares

 |  get_sustainability(self, proxy=None, as_dict=False)
Controversy rating and Sustainability 

 |  get_upgrades_downgrades(self, proxy=None, as_dict=False)
 |      Returns a DataFrame with the recommendations changes (upgrades/downgrades)
 |      Index: date of grade
 |      Columns: firm toGrade fromGrade action
res['Firm'] the firm that gave the rating
res['ToGrade'] {'', 'Strong Buy', 'In-Line', 'Underweight', 'Peer Perform', 'Sector Weight', 'Equal-Weight', 'Sell', 'Buy', 'Market Outperform', 'Outperform', 'Underperform', 'Perform', 'Neutral', 'Overweight', 'Sector Perform', 'Reduce', 'Underperformer', 'Hold', 'Market Perform'}
res['FromGrade'] {'', 'Reduce', 'Underperform', 'Sell', 'In-Line', 'Strong Buy', 'Perform', 'Underweight', 'Neutral', 'Buy', 'Overweight', 'Market Perform', 'Peer Perform', 'Market Outperform', 'Sector Perform', 'Hold', 'Outperform', 'Equal-Weight'}
res['Action'] {'reit', 'up', 'init', 'down', 'main'}

 |  history(self, *args, **kwargs) -> pandas.core.frame.DataFrame
* daily price, volume, high, low

