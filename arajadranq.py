# ex 1

# price_list = [10, 2, 12, 5, 1, 7, 3, 2, 9, 5]
# d =  {'profit': None, 'day_start': None, 'day_sell' : None}
# for i in range(0, len(price_list)):
#     for j in range(1, len(price_list)):
#         if j > i:
#             if d['profit'] is None or price_list[j] - price_list[i] > d['profit']:
#                d['profit'] = price_list[j] - price_list[i]
#                d['day_start'] = price_list[i]
#                d['day_sell'] = price_list[j]
# print(d)


# ex 2

# def fib(n):
#     if n <= 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(4))