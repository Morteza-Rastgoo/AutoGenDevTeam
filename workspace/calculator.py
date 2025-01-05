class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

def main():
    calc = Calculator()
    
    try:
        # Test basic operations
        print("Addition: 5 + 3 =", calc.add(5, 3))
        print("Subtraction: 10 - 4 =", calc.subtract(10, 4))
        print("Multiplication: 6 * 2 =", calc.multiply(6, 2))
        print("Division: 15 / 3 =", calc.divide(15, 3))
        
        # Test division by zero
        print("Division by zero:", calc.divide(10, 0))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 