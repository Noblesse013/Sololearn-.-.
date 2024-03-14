'''
Similar to the map() method, the filter() function accepts two parameters: an iterable and a function. Applying a condition given in the supplied function to each item in the iterable and returning only those for which the function evaluates to True is the main goal of filter().
Product names that are four characters or fewer are filtered out by this code.
'''
products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]
filtered_prod = list(filter(lambda name: len(name) == 4, products))
