# Import the `calculator` module here
import calculator
calc = calculator.Calculator()        #Create a new instance of the `Calculator` class defined in the `calculator` module
for i in range(100):
    # Use the Calculator method `add` to add `i` o the current value.
    calc.add(i)


print(calc.get_current())




