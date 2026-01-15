def calculate_shipping_cost(weight, distance):
    rate_per_km = 0.5
    return weight * distance * rate_per_km

if __name__ == "__main__":
    cost = calculate_shipping_cost(10, 50)
    print(f"Shipping cost: ${cost}")
