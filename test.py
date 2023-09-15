exchange_rates = [1320, 950, 182]
currencies = [13, 200, 13]
converted_amounts = [currency * rate for currency, rate in zip(currencies, exchange_rates)]
total_krw = sum(converted_amounts)
print("철수가 가지고 있는 돈의 원화 가치는 X원 입니다.", total_krw)
