from sympy import symbols, Eq, solve

def linear_equation(a, b):
    """
    Solves a simple linear equation of the form ax + b = 0.
    
    Parameters:
    a (int/float): Coefficient of x
    b (int/float): Constant term

    """
    if a == 0:
        return "No solution" if b != 0 else "Infinite solutions"
    
    x = symbols('x')
    equation = Eq(a * x + b, 0)
    solution = solve(equation, x)
    
    return solution[0]  

# Example Usage
  
print(linear_equation(0, 5))   
print(linear_equation(0, 0))   
