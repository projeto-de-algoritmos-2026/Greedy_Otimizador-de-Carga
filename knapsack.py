def fractional_knapsack(capacity, materials):
    for m in materials:
        m["ratio"] = m["price_per_ton"]

    sorted_materials = sorted(materials, key=lambda x: x["ratio"], reverse=True)

    selected = []
    remaining = capacity
    total_value = 0.0

    for material in sorted_materials:
        if remaining <= 0:
            break

        take = min(material["stock"], remaining)
        fraction = take / material["stock"]
        value = take * material["price_per_ton"]

        selected.append({
            "name": material["name"],
            "available": material["stock"],
            "taken": take,
            "fraction": fraction,
            "price_per_ton": material["price_per_ton"],
            "value": value,
        })

        total_value += value
        remaining -= take

    return selected, total_value
