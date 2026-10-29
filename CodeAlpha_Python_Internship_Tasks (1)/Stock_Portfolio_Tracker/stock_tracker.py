"""Simple stock portfolio tracker using sample hardcoded prices."""
import csv

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "MSFT": 420.00,
    "GOOGL": 165.00,
    "AMZN": 190.00,
}


def main():
    print("\n=== Stock Portfolio Tracker ===")
    print("Sample prices (USD; for this demo only):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol}: ${price:.2f}")

    portfolio = []
    while True:
        symbol = input("\nEnter stock symbol (or 'done' to finish): ").strip().upper()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Unknown symbol. Choose one from the list above.")
            continue

        try:
            quantity = int(input(f"Quantity of {symbol}: ").strip())
            if quantity <= 0:
                print("Quantity must be a positive whole number.")
                continue
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        price = STOCK_PRICES[symbol]
        portfolio.append((symbol, quantity, price, quantity * price))

    if not portfolio:
        print("\nNo stocks entered.")
        return

    total = sum(item[3] for item in portfolio)
    print("\n--- Portfolio Summary ---")
    for symbol, quantity, price, value in portfolio:
        print(f"{symbol}: {quantity} shares × ${price:.2f} = ${value:.2f}")
    print(f"Total investment value: ${total:.2f}")

    save = input("Save summary to portfolio.csv? (y/n): ").strip().lower()
    if save == "y":
        with open("portfolio.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Symbol", "Quantity", "Sample Price USD", "Investment Value USD"])
            writer.writerows(portfolio)
            writer.writerow([])
            writer.writerow(["", "", "Total", f"{total:.2f}"])
        print("Saved to portfolio.csv")


if __name__ == "__main__":
    main()
