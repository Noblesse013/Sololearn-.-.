'''
The map() function applies a specified function to every element in an iterable, like lists or tuples. 
It produces a result that can be transformed into a list using the list() function for easy viewing or further use.
'''
names = ["alice", "bob", "CHARLIE", "Tom"]

def capitalize(name):
  return name.capitalize()

capitalized = map(capitalize, names)
capitalized = list(capitalized)
