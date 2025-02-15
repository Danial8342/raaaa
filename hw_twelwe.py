def summa(prices: list[float]) -> float:
    sum_prices = sum(prices)
    return sum_prices

def unique(items: list[str]) -> list[str]:
    unique_list = []
    for s in items:
        if s not in unique_list:
            unique_list.append(s)
    return unique_list

def is_shopping(budget: float, price: float) -> bool:
    answer = False
    if budget >= price:
        answer = True
    return answer

prices = [10.5, 20.75, 5.99, 10.5, 20.75, 5.99]
my_sum_prices = summa(prices)
print(f"total sum: {my_sum_prices}")

strings = ["cat", "dog", "cat", "brother"]
unique_strings = unique(strings)
print(unique_strings)

budget = 100.50
price = 500.35
my_answer = is_shopping(budget, price)
print(my_answer)
