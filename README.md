# AST Output Evaluation

## 1. Loops (For Loop)

### Output:
```
Module(
    body=[
        For(
            target=Name(id='i', ctx=Store()),
            iter=Call(
                func=Name(id='range', ctx=Load()),
                args=[
                    Constant(value=10)]),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            Name(id='i', ctx=Load())]))])])
```
### Code:
This AST represents the Python code:
```python
for i in range(10):
    print(i)
```

**Breakdown:**
- `Module` = block of code
- `body=[...]` = the list of top-level statements inside the program.
- `For` = a `for` loop node. It tells Python to repeat the same block of code once for every value in an iterable.
- `target=Name(id='i', ctx=Store())` = the loop variable being assigned on each iteration.
  - `Name(id='i')` identifies the variable name `i`.
  - `ctx=Store()` means `i` is on the left side of assignment, so it is being written to.
- `iter=Call(...)` = the iterable being looped over is produced by a function call.
  - `Call` means Python is executing a function.
  - `func=Name(id='range', ctx=Load())` means the function being called is `range`.
  - `ctx=Load()` means `range` is being read so it can be called.
- `args=[Constant(value=10)]` = the argument passed to `range`.
  - `Constant(value=10)` is a literal number.
  - `range(10)` creates the sequence `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`.
- `body=[...]` = the statements that run during each loop iteration.
- `Expr(...)` = an expression used as a standalone statement.
- `value=Call(...)` = the expression is a function call.
- `func=Name(id='print', ctx=Load())` = the function being called is `print`.
- `args=[Name(id='i', ctx=Load())]` = the value passed to `print`.
  - `Name(id='i', ctx=Load())` means the current value of `i` is being read.
  - `ctx=Load()` means the variable is being accessed, not assigned.


---
## 2. Generation Function (Generator with Yield)
### Output:
```
Module(
    body=[
        FunctionDef(
            name='simple_gen',
            args=arguments(),
            body=[
                Expr(
                    value=Yield(
                        value=Constant(value='Alice'))),
                Expr(
                    value=Yield(
                        value=Constant(value='Bob'))),
                Expr(
                    value=Yield(
                        value=Constant(value='Charlie')))]),
        Assign(
            targets=[
                Name(id='gen', ctx=Store())],
            value=Call(
                func=Name(id='simple_gen', ctx=Load()))),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Call(
                        func=Name(id='next', ctx=Load()),
                        args=[
                            Name(id='gen', ctx=Load())])])),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Call(
                        func=Name(id='next', ctx=Load()),
                        args=[
                            Name(id='gen', ctx=Load())])])),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Call(
                        func=Name(id='next', ctx=Load()),
                        args=[
                            Name(id='gen', ctx=Load())])]))])
```

### Code:
This AST represents the Python code:
```python
def simple_gen():
    yield 'Alice'
    yield 'Bob'
    yield 'Charlie'

gen = simple_gen()
print(next(gen))  # Output: Alice
print(next(gen))  # Output: Bob
print(next(gen))  # Output: Charlie
```

**Breakdown:**
- `Module` = block of code
- `body=[...]` = the list of top-level statements in the file.
- `FunctionDef(name='simple_gen')` = defines a function named `simple_gen`.
  - `FunctionDef` means “function definition.”
  - Because this function contains `yield`, Python treats it as a generator function instead of a normal function.
- `args=arguments()` = the function takes no parameters.
- `body=[...]` = the statements inside the function body.
- `Expr(value=Yield(...))` = a `yield` statement wrapped as an expression.
  - `Yield(value=Constant(value='Alice'))` means the generator produces `'Alice'` and pauses at that point.
  - `Yield(value=Constant(value='Bob'))` means execution resumes later and produces `'Bob'`.
  - `Yield(value=Constant(value='Charlie'))` means the generator produces `'Charlie'` on the next resume.
- `Assign(targets=[Name(id='gen', ctx=Store())], value=Call(...))` = stores the generator object in the variable `gen`.
  - `targets=[Name(id='gen', ctx=Store())]` means `gen` is the name being assigned.
  - `ctx=Store()` means the name is being created or updated.
  - `value=Call(func=Name(id='simple_gen', ctx=Load()))` means `simple_gen()` is called to create the generator object.
- `Call(func=Name(id='next', ctx=Load()), args=[Name(id='gen', ctx=Load())])` = asks the generator for its next value.
  - `next(gen)` resumes execution from the last `yield`.
  - The first call returns `'Alice'`.
  - The second call returns `'Bob'`.
  - The third call returns `'Charlie'`.
- `print(...)` = displays the value returned by `next(gen)`.

**What it does:** Define a generator, create an instance, then print each yielded value one at a time.

---
## 3. Complex Conditional Statement (If-Else)
### Output:
```
Module(
    body=[
        Assign(
            targets=[
                Name(id='x', ctx=Store())],
            value=Constant(value=10)),
        If(
            test=Compare(
                left=Name(id='x', ctx=Load()),
                ops=[
                    Gt()],
                comparators=[
                    Constant(value=5)]),
            body=[
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            Constant(value='x is greater than 5')]))],
            orelse=[
                Expr(
                    value=Call(
                        func=Name(id='print', ctx=Load()),
                        args=[
                            Constant(value='x is less than or equal to 5')]))])])
```
### Code:
This AST represents the Python code:
```python
x = 10
if x > 5:
    print('x is greater than 5')
else:
    print('x is less than or equal to 5')
```
**Breakdown:**
- `Module` = block of code
- `body=[...]` = the list of top-level statements in the file.
- `Assign(targets=[Name(id='x')], value=Constant(value=10))` = assigns `10` to `x`.
  - `targets=[Name(id='x', ctx=Store())]` means `x` is the assignment target.
  - `ctx=Store()` means the name is being written to.
  - `value=Constant(value=10)` means the assigned value is the literal number `10`.
- `If(test=Compare(...))` = an `if` statement that checks a condition and then chooses one of two code paths.
- `test=Compare(...)` = the condition being tested.
  - `left=Name(id='x', ctx=Load())` means the left side of the comparison is the current value of `x`.
  - `ctx=Load()` means `x` is being read.
  - `ops=[Gt()]` means the comparison operator is `>` (“greater than”).
  - `comparators=[Constant(value=5)]` means `x` is being compared against `5`.
- `body=[...]` = the code that runs when the condition is true.
  - Inside it, the `print` call is wrapped in `Expr(...)` because it is used as a standalone statement.
- `orelse=[...]` = the code that runs when the condition is false.
  - It contains the alternate `print` statement.
- `Call(func=Name(id='print', ctx=Load()), ...)` = a function call to `print`.
- `Constant(value='...')` = a literal string value being printed.

**What it does:** Since `10 > 5` is true, print "x is greater than 5"

---
## 4. Complex Arithmetic Expression
### Output:
```
Module(
    body=[
        Assign(
            targets=[
                Name(id='result', ctx=Store())],
            value=BinOp(
                left=BinOp(
                    left=BinOp(
                        left=Constant(value=2),
                        op=Add(),
                        right=Constant(value=3)),
                    op=Mult(),
                    right=BinOp(
                        left=Constant(value=4),
                        op=Sub(),
                        right=Constant(value=1))),
                op=Div(),
                right=Constant(value=5))),
        Expr(
            value=Call(
                func=Name(id='print', ctx=Load()),
                args=[
                    Name(id='result', ctx=Load())]))])
```
### Code:
This AST represents the Python code:
```python
result = (2 + 3) * (4 - 1) / 5
print(result)
```
**Breakdown:**
- `Module` = block of code
- `body=[...]` = the list of top-level statements in the file.
- `Assign(targets=[Name(id='result', ctx=Store())], value=BinOp(...))` = stores the final computed value in `result`.
  - `targets=[Name(id='result', ctx=Store())]` means `result` is the variable being assigned.
  - `ctx=Store()` means the variable is on the left side of assignment.
- `value=BinOp(...)` = the assigned value is built from nested binary operations.
- `BinOp(left=..., op=..., right=...)` = a binary operation with a left operand, an operator, and a right operand.
- The nested structure reflects the order of evaluation:
  - `Constant(value=2)` and `Constant(value=3)` are combined first with `Add()` to represent `2 + 3`.
  - `Constant(value=4)` and `Constant(value=1)` are combined with `Sub()` to represent `4 - 1`.
  - Those two inner results are multiplied with `Mult()` to represent `(2 + 3) * (4 - 1)`.
  - The multiplication result is divided by `5` with `Div()` to represent the full expression.
- `Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Name(id='result', ctx=Load())]))` = prints the computed value.
  - `Name(id='result', ctx=Load())` means the stored result is being read and passed to `print`.

**Step-by-step calculation:**
```
(2 + 3) * (4 - 1) / 5
= 5 * 3 / 5
= 15 / 5
= 3.0
```
**What it does:** Calculate `(2+3) * (4-1) / 5` and print result: `3.0`

---
## 5. Class Definition
### Output:
```
Module(
    body=[
        ClassDef(
            name='MyClass',
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        args=[
                            arg(arg='self'),
                            arg(arg='name')]),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='name',
                                    ctx=Store())],
                            value=Name(id='name', ctx=Load()))]),
                FunctionDef(
                    name='greet',
                    args=arguments(
                        args=[
                            arg(arg='self')]),
                    body=[
                        Return(
                            value=JoinedStr(
                                values=[
                                    Constant(value='Hello, '),
                                    FormattedValue(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='name',
                                            ctx=Load()),
                                        conversion=-1),
                                    Constant(value='!')]))])])])
```
### Code:
This AST represents the Python code:
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
```

**Breakdown:**
- `Module` = block of code
- `body=[...]` = the list of top-level statements in the file.
- `ClassDef(name='MyClass')` = defines a class named `MyClass`.
  - `ClassDef` means “class definition.”
  - `name='MyClass'` is the class name.
- `body=[...]` = the list of statements inside the class.
- `FunctionDef(name='__init__')` = defines the constructor method.
  - `__init__` runs automatically when a new instance of the class is created.
- `args=arguments(args=[arg(arg='self'), arg(arg='name')])` = the parameters accepted by the constructor.
  - `self` refers to the current object instance.
  - `name` is the value being passed into the object.
- `Assign(...)` inside `__init__` = assigns the incoming `name` value to an attribute on the object.
  - `Attribute(value=Name(id='self', ctx=Load()), attr='name', ctx=Store())` represents `self.name` on the left side of assignment.
  - `value=Name(id='name', ctx=Load())` means the parameter `name` is being read and stored into the object.
  - `ctx=Store()` means `self.name` is being written to.
- `FunctionDef(name='greet')` = defines a second method called `greet`.
- `args=arguments(args=[arg(arg='self')])` = this method only needs the object instance itself.
- `Return(...)` = sends a value back from the method.
- `JoinedStr(...)` = represents an f-string, or formatted string literal.
  - `Constant(value='Hello, ')` is the fixed text at the start of the string.
  - `FormattedValue(...)` is the part inside `{...}` that gets evaluated dynamically.
  - `Attribute(value=Name(id='self', ctx=Load()), attr='name', ctx=Load())` reads `self.name` from the object.
  - `Constant(value='!')` is the final punctuation at the end of the string.
- `conversion=-1` = means no special string conversion is being applied to the formatted value.

**What it does:** Define a class with a constructor that stores a name, and a greet method that returns a formatted greeting message.

---
## Summary Table
| Example | Input Code | Output | Key AST Nodes |
|---------|-----------|--------|---------------|
| **Loops** | `for i in range(10): print(i)` | For loop AST | `For`, `Call`, `range` |
| **Generator** | `def simple_gen(): yield 'Alice'...` | FunctionDef with Yield | `FunctionDef`, `Yield`, `next()` |
| **Conditional** | `if x > 5: print(...) else: print(...)` | If-Compare AST | `If`, `Compare`, `Gt()` |
| **Arithmetic** | `result = (2+3)*(4-1)/5` | Nested BinOp AST | `BinOp`, `Add`, `Sub`, `Mult`, `Div` |
| **Class** | `class MyClass: def __init__, def greet` | ClassDef with FunctionDef | `ClassDef`, `FunctionDef`, `Attribute`, `JoinedStr` |
---

## How to Read AST Output
- **Constant(value=X)** = literal value (number, string)
- **Name(id='X', ctx=Load())** = variable being read
- **Name(id='X', ctx=Store())** = variable being assigned
- **Call(func=Name(id='X'))** = function call to X
- **BinOp(left=..., op=..., right=...)** = binary operation (two operands + operator)
- **Module(body=[...])** = entire program
- **ClassDef(name='X')** = class definition with name X
- **FunctionDef(name='X')** = function definition with name X
- **Attribute(value=..., attr='X')** = attribute access (e.g., `self.name`)
- **JoinedStr(values=[...])** = f-string (formatted string literal)
- **FormattedValue(value=...)** = expression inside f-string (e.g., `{self.name}`)
- **arg(arg='X')** = function parameter with name X
- **ctx** = context (Load = read, Store = assign)