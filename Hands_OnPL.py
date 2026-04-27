import ast

def print_ast(codes):
    print(ast.dump(ast.parse(codes), indent=4))


Class = """
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
"""
loops = """
for i in range(10):
    print(i)"""

gf = """
def simple_gen():
    yield "Alice"
    yield "Bob"
    yield "Charlie"

# Initialize the generator object
gen = simple_gen()

print(next(gen)) # Output: Alice
print(next(gen)) # Output: Bob
print(next(gen)) # Output: Charlie
"""

complex_cs = """
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
"""

complex_a = """result = (2 + 3) * (4 - 1) / 5
print(result)"""

print(f"\n--Loops:")
print_ast(loops)
print(f"\n--Generation Function")
print_ast(gf)
print(f"\n--Complex Conditional Statement")
print_ast(complex_cs)
print(f"\n--Complex Arithmetic Expression")
print_ast(complex_a)
print(f"\n--Class")
print_ast(Class)
