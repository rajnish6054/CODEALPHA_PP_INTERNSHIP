import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, quantity):
        self.portfolio[ticker] = quantity

    def remove_stock(self, ticker):
        if ticker in self.portfolio:
            del self.portfolio[ticker]

    def track_performance(self):
        total_value = 0
        for ticker, quantity in self.portfolio.items():
            stock = yf.Ticker(ticker)
            current_price = stock.info['regularMarketPrice']
            total_value += current_price * quantity
            print(f"{ticker}: {current_price} x {quantity} = {current_price * quantity}")
        print(f"Total portfolio value: {total_value}")

# Example usage
portfolio = StockPortfolio()
portfolio.add_stock('AAPL', 10)
portfolio.add_stock('GOOG', 5)
portfolio.track_performance()
portfolio.remove_stock('GOOG')
portfolio.track_performance()





