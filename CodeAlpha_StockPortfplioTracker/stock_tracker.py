# Stock Portfolio Tracker
# CodeAlpha Python Programming Internship - Task 2

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 180
}

portfolio = {}

print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

while True:
    print("\nAvailable Stocks:")

    for stock, price in stocks.items():
        print(f"{stock} - ${price}")

    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stocks:
        print("Invalid stock name. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

        print(f"{quantity} shares of {stock_name} added successfully.")

    except ValueError:
        print("Please enter a valid number.")

print("\n" + "=" * 40)
print("          PORTFOLIO SUMMARY")
print("=" * 40)

total_investment = 0

if not portfolio:
    print("No stocks added.")

else:
    for stock, quantity in portfolio.items():
        price = stocks[stock]
        value = price * quantity
        total_investment += value

        print(f"{stock}: {quantity} shares × ${price} = ${value}")

    print("-" * 40)
    print(f"Total Investment Value: ${total_investment}")
    print("=" * 40)