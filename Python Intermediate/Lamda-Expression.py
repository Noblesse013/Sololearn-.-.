'''
Lambda expressions are quick-to-create and-use functions without a name. 
Using the lambda keyword, they can be expressed in a single line and are frequently employed for short, straightforward operations.
'''
#Define a lambda expression:
discount = lambda price: price * 0.9 
print(discount(100))
#You can assign the lambda expression to a variable and then call it as a regular function.


#Lambda expressions can take multiple arguments separated by commas.
area=lambda width,height: width * height
print(area(10*20))

'''
By enclosing parameters in parenthesis right after the lambda function, you can supply arguments to lambda expressions dynamically. 
Additionally, the lambda expression needs to be contained in parenthesis.
'''
res = (lambda x, y: x + y) (2, 3)
print(res)
