stockvalues_dict = {
  "SIRI": "85.55" ,
  "AAPL": "100.33" ,
  "TM": "77.77" ,
  "CSCO": "80.22" ,
  "VZ": "50.20" ,
  "DELL": "42.30" ,
  "EBAY": "150.23" ,
  "HMC": "200.02" ,
  "DIS": "320.60" ,
  "BBY": "175.45" ,
  "AMZN": "350.85" ,
}
chosen_stock = input("Please enter the stock symbol:")

stock_value = stockvalues_dict.get(chosen_stock, "Chosen stock ticker is not found.")

print(chosen_stock, stock_value)
    