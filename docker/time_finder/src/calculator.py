import pandas as pd
from dateutil.relativedelta import relativedelta

def time_finder(run_date:str, period:int=1):
    return pd.to_datetime(run_date) + relativedelta(days=period)