# CodeAlpha  Task 2 - Stock Portfolio Tracker

stock_prices = {
    "computer" : 100000,
    "monitor" : 12000,
    "charger" : 1800,
    "printer" : 20000,
    "speaker" : 1900,
    "mouse": 350,
    "keyboard" : 500,
}



print(" Stock Portfolio Tracker")

portfolio = {}
total_investment = 0


while True:

    stock = input("Enter stock name (or type 'done' to finish): ").lower()

    if stock == "done":
        break

    if stock not in stock_prices:
        print(" Stock not found!")
        print("Available stocks:", list(stock_prices.keys()))
        continue


    quantity = int(input("Enter quantity: "))


    portfolio[stock] = quantity


print("\n Portfolio:")


for stock, quantity in portfolio.items():

    price = stock_prices[stock]

    investment = price * quantity

    total_investment += investment

    print(
        stock,
        "Quantity:",
        quantity,
        "Price:",
        price,
        "Investment:",
        investment
    )


print("\nTotal Investment =", total_investment)

with open("result.txt", "w") as file:

    file.write("Stock Portfolio Report\n")
    file.write("--\n")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | Price: {price} | Investment: {investment}\n"
        )


    file.write(f"\nTotal Investment = {total_investment}")


print("\n Result saved in result.txt")

