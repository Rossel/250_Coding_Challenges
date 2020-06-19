import re
     
s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"
     
result = re.search(r"\$(\d{1,3},\d{1,3}\.\d{1,3}),", s)
     
print(result.group(1))