import requests
from datetime import datetime

from sources.exchange import Exchange

class Binance(Exchange):
  start_year = 2021
  api_url = "https://api.binance.com/api/v3/klines"


  def params(self, year):
    timestamp = self.timestamp(year)

    params = {
      "interval": "1h",
      "symbol": "BTCEUR",
      "startTime": str(timestamp)+"000",
      "endTime": str(timestamp)+"999",
    }

    return params

  def year(self, year):
    json_response = requests.get(
      self.api_url,
      params = self.params(year)
    ).json()

    return json_response[0][1]

