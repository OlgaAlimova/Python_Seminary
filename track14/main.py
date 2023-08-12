# main.py
from portfolio import Portfolio

def main():
    portfolio = Portfolio()

    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

    initial_value = portfolio.calculate_portfolio_value(stocks, prices)
    print(f"Initial portfolio value: {initial_value:.2f} USD")

    initial_value = 10000.0
    current_value = 15000.0
    return_value = portfolio.calculate_portfolio_return(initial_value, current_value)
    print(f"Portfolio return: {return_value:.2f}%")

    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}

    most_profitable_stock = portfolio.get_most_profitable_stock(stocks, prices)
    print(f"Most profitable stock: {most_profitable_stock}")

if __name__ == "__main__":
    main()
