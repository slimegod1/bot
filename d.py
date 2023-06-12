import time
from binance.client import Client

# Set up Binance API client
api_key = ''
api_secret = ''
client = Client(api_key, api_secret)

# Set up trading parameters
symbol = 'ARBUSDT'
quantity = 900
buy_price = 1.3
sell_price = 1.36

# Main trading loop
while True:
    # Get current price of symbol
    ticker = client.get_symbol_ticker(symbol=symbol)
    price = float(ticker['price'])

    # Check if buy trigger is met
    if price <= buy_price:
        order = client.order_market_buy(symbol=symbol, quantity=quantity)
        print('Bought', quantity, symbol, 'at', price)

    # Check if sell trigger is met
    elif price >= sell_price:
        order = client.order_market_sell(symbol=symbol, quantity=quantity)
        print('Sold', quantity, symbol, 'at', price)

    # Wait before checking again
    time.sleep(5)
