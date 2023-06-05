class Calculator:

    def add(self, num1, num2):
        if isinstance(num1, str) and num1.isnumeric():
            num1 = int(num1)
        return num1 + int(num2)
    
    def multiply(self, num1, num2):
        return num2 * num1