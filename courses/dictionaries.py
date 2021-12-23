product = {
    "name":"book1",
    "price":4.55
}
print(product)
print(type(product))
print(dir(product))
print(product.keys())
print(product.items())


product.clear() # clean dictionaries
print(product)


# add two o more dictionaries
add = [
    {"name":"carlos"},
    {"age":35}
]
print(add)