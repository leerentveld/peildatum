from datetime import date
import yaml

from sources.binance import Binance
from sources.bitfenix import Bitfenix
from sources.bitstamp import Bitstamp
from sources.bitvavo import Bitvavo
from sources.coinbase import Coinbase
from sources.kraken import Kraken

end_year = date.today().year
start_year = 2012

# Create range of years to get ohlc data for (desc).
years = range(end_year, start_year-1, -1)

# Define available exchanges.
exchanges = {
  'binance': Binance(),
  'bitfenix': Bitfenix(),
  'bitstamp': Bitstamp(),
  'bitvavo': Bitvavo(),
  'coinbase': Coinbase(),
  'kraken': Kraken(),
}

# Create a dict to collect ohlc data for all exchanges.
ohlc = {}
for name, exchange in exchanges.items():
  ohlc[name] = []

# Loop years.
for year in years:
  print(year)
  # Loop exchanges and get ohlc data for the provided year.
  for name, exchange in exchanges.items():
    value = exchange.get(year)
    ohlc[name].append({
      "year": year,
      "open": value,
    })
    print("On 1 jan " + str(year)+" "+name + " was worth EUR "+ str(value))

  print("")

for exchange_name, values in ohlc.items():
  filename = "ohlc/"+exchange_name + ".yaml"
  with open(filename, 'w') as outfile:
    yaml.dump(values, outfile, default_flow_style=False)
