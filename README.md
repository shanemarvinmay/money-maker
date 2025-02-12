# money-maker
Investment app that helps you make money.

## To run Jupyter:
```
uv run jupyter lab
```

Help on class Ticker in module yfinance.ticker:

class Ticker(yfinance.base.TickerBase)
 |  Ticker(ticker, session=None, proxy=None)
 |  
 |  Method resolution order:
 |      Ticker
 |      yfinance.base.TickerBase
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, ticker, session=None, proxy=None)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __repr__(self)
 |      Return repr(self).
 |  
 |  option_chain(self, date=None, tz=None)
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
 |  * dividen dates and stock splits

 |  get_analyst_price_targets(self, proxy=None) -> dict
 |      Keys:   current  low  high  mean  median
    * price targets

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
 |  get_balancesheet(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
 |  
 |  get_calendar(self, proxy=None) -> dict
 |  
 |  get_capital_gains(self, proxy=None) -> pandas.core.series.Series
 |  
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
 |  get_cashflow(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
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
 |  
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
 |  
 |  get_earnings_estimate(self, proxy=None, as_dict=False)
 |      Index:      0q  +1q  0y  +1y
 |      Columns:    numberOfAnalysts  avg  low  high  yearAgoEps  growth
 |  
 |  get_earnings_history(self, proxy=None, as_dict=False)
 |      Index:      pd.DatetimeIndex
 |      Columns:    epsEstimate  epsActual  epsDifference  surprisePercent
 |  
 |  get_eps_revisions(self, proxy=None, as_dict=False)
 |      Index:      0q  +1q  0y  +1y
 |      Columns:    upLast7days  upLast30days  downLast7days  downLast30days
 |  
 |  get_eps_trend(self, proxy=None, as_dict=False)
 |      Index:      0q  +1q  0y  +1y
 |      Columns:    current  7daysAgo  30daysAgo  60daysAgo  90daysAgo
 |  
 |  get_fast_info(self, proxy=None)
 |  
 |  get_financials(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
 |  
 |  get_funds_data(self, proxy=None) -> Optional[yfinance.scrapers.funds.FundsData]
 |  
 |  get_growth_estimates(self, proxy=None, as_dict=False)
 |      Index:      0q  +1q  0y  +1y +5y -5y
 |      Columns:    stock  industry  sector  index
 |  
 |  get_history_metadata(self, proxy=None) -> dict
 |  
 |  get_income_stmt(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
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
 |  get_incomestmt(self, proxy=None, as_dict=False, pretty=False, freq='yearly')
 |  
 |  get_info(self, proxy=None) -> dict
 |  
 |  get_insider_purchases(self, proxy=None, as_dict=False)
 |  
 |  get_insider_roster_holders(self, proxy=None, as_dict=False)
 |  
 |  get_insider_transactions(self, proxy=None, as_dict=False)
 |  
 |  get_institutional_holders(self, proxy=None, as_dict=False)
 |  
 |  get_isin(self, proxy=None) -> Optional[str]
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

