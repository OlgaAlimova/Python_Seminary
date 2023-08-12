# portfolio.py

class Portfolio:
    def __init__(self):
        self.initial_stocks_value = {}

    def calculate_portfolio_value(self, stocks, prices):
        total_value = 0
        for stock, quantity in stocks.items():
            total_value += quantity * prices.get(stock, 0)
        self._set_initial_stocks_value(stocks, prices)
        return total_value

    def calculate_portfolio_return(self, initial_value, current_value):
        return ((current_value - initial_value) / initial_value) * 100

    def get_most_profitable_stock(self, stocks, prices):
        if not self.initial_stocks_value:
            raise ValueError("Initial stock values not set")

        most_profitable_stock = None
        max_profit = 0

        for stock, initial_value in self.initial_stocks_value.items():
            current_value = stocks.get(stock, 0) * prices.get(stock, 0)
            profit = current_value - initial_value

            if profit > max_profit:
                most_profitable_stock = stock
                max_profit = profit

        return most_profitable_stock

    def _set_initial_stocks_value(self, stocks, prices):
        if not self.initial_stocks_value:
            self.initial_stocks_value = {stock: quantity * prices.get(stock, 0) for stock, quantity in stocks.items()}
