import argparse
import datetime
import pandas as pd

from src.calculator import time_finder

# get given date
today = str(datetime.date.today())
parser = argparse.ArgumentParser()
parser.add_argument("--run_date", type=str, default=today)
parser.add_argument("--period", type=int, default=1)
args, _ = parser.parse_known_args()

# calculate next period
calculated_date = time_finder(args.run_date, args.period)

result = pd.DataFrame({"given_date": [args.run_date],
                       "calculated_date": [calculated_date]})

