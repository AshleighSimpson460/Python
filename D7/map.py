# map() = applies a function to each item in an iterable (list, tuple, etc.)
# map(function, iterable)

store = [("shirt", 20.00),("pants", 25.00),("jacket", "50.00"),("socks", 10.00)]

to_dollar = lambda data : (data[0], float(data[1]) * 1.27)
to_pounds = lambda data : (data[0], float(data[1]) / 1.27)


store_dollar = list(map(to_pounds, store))

for i in store_dollar:
    print(i)