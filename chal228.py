import re
     
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"
     
result = re.sub(r"[A-Z]{3}", "Bitcoin", s)
     
print(result)