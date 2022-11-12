import os
from pprint import pprint

from dotenv import load_dotenv
from pandas import read_csv
from plotly.express import line

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"

df = read_csv(request_url)

import os
from pprint import pprint

from dotenv import load_dotenv
from pandas import read_csv
from plotly.express import line

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"

df = read_csv(request_url)

# Challenge A
# What is the most recent unemployment rate? And the corresponding date? Display the unemployment rate using a percent sign.

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
first_row = df.iloc[0]
print(f"{first_row['value']}%", "as of", first_row["timestamp"])

# Challenge B
# What is the average unemployment rate for all months during this calendar year? How many months does this cover?

this_year_df = df[df["timestamp"].str.contains("2022-")]

print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{this_year_df['value'].mean()}%")
print("NO MONTHS:", len(this_year_df))

# Challenge C
# Plot a line chart of unemployment rates over time.

from plotly.express import line

fig = line(x=df["timestamp"], y=df["value"], title="United States Unemployment Rate over time", labels= {"x": "Month", "y": "Unemployment Rate"})
fig.show()