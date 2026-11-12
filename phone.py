# Sample sales data

sales = [
    {"customer": "Asha", "city": "Hyderabad", "amount": 5000},
    {"customer": "Ravi", "city": "Chennai", "amount": 7000},
    {"customer": "Priya", "city": "Hyderabad", "amount": 3000},
    {"customer": "Kiran", "city": "Chennai", "amount": 6000}
]

# Calculate total sales

total_sales = sum(item["amount"] for item in sales)

print("Total Sales:", total_sales)


# Calculate sales by city

city_sales = {}

for item in sales:
    city = item["city"]
    amount = item["amount"]

    if city not in city_sales:
        city_sales[city] = 0

    city_sales[city] += amount

print("\nSales by City:")

for city, amount in city_sales.items():
    print(city, ":", amount)