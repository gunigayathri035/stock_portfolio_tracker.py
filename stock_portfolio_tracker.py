from datetime import datetime

# Predefined stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 175,
    "AMZN": 190
}


def track_portfolio():
    portfolio = []
    total_investment = 0

    print("===================================")
    print("      STOCK PORTFOLIO TRACKER")
    print("===================================")

    print("Available stocks:", ", ".join(STOCK_PRICES))

    while True:
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print("Stock not available. Please choose from the listed stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

        except ValueError:
            print("Please enter a valid whole number.")
            continue

        price = STOCK_PRICES[stock]
        value = price * quantity

        total_investment += value

        portfolio.append({
            "stock": stock,
            "price": price,
            "quantity": quantity,
            "value": value
        })

        print(f"{stock}: {quantity} × ${price} = ${value}")

    print("\n===================================")
    print("       PORTFOLIO SUMMARY")
    print("===================================")

    if not portfolio:
        print("No stocks were added.")
        return

    for item in portfolio:
        print(
            f"{item['stock']} | "
            f"Price: ${item['price']} | "
            f"Quantity: {item['quantity']} | "
            f"Value: ${item['value']}"
        )

    print(f"\nTotal Investment Value: ${total_investment}")

    # Save result to a text file
    filename = "portfolio_result.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("STOCK PORTFOLIO TRACKER\n")
        file.write(
            f"Date: {datetime.now():%Y-%m-%d %H:%M:%S}\n\n"
        )

        for item in portfolio:
            file.write(
                f"{item['stock']} | "
                f"Price: ${item['price']} | "
                f"Quantity: {item['quantity']} | "
                f"Value: ${item['value']}\n"
            )

        file.write(
            f"\nTotal Investment Value: ${total_investment}\n"
        )

    print(f"Result saved to {filename}")


if __name__ == "__main__":
    track_portfolio()