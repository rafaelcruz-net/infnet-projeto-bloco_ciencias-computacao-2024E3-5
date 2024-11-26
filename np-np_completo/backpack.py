def backpack_guloso(items, capacity):
    #Ordernar os itens por valor/peso em ordem decrescente
    items = sorted(items, key=lambda x: x['value'] / x['weight'], reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    for item in items:
        if (total_weight + item['weight'] <= capacity):
            selected_items.append(item)
            total_value += item['value']
            total_weight += item['weight']
        else:
            remaining_capacity = capacity - total_weight
            fraction = remaining_capacity / item['weight']
            total_value += item['value'] * fraction
            total_weight += item['weight'] + fraction
            selected_items.append({**item, 'fraction': fraction})
            break
    return {
        'total_value': total_value,
        'total_weight': total_weight,
        'selected_items': selected_items
    }

items = [
    {'name': 'Item 1', 'weight': 10, 'value': 60},
    {'name': 'Item 2', 'weight': 20, 'value': 100},
    {'name': 'Item 3', 'weight': 30, 'value': 120},
    {'name': 'Item 4', 'weight': 14, 'value': 200}
]

capacity = 50

result = backpack_guloso(items, capacity)

print("Valor total:", result['total_value'])
print("Peso total:", result['total_weight'])
print("Itens selecionados:")
for item in result['selected_items']:
    print(item)