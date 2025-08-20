def add(x, y):
  """ For Addition """
  return x + y

def subtract(x, y):
  """ For Substraction """
  return x - y

def multiply(x, y):
  """ For Multiplication """
  return x * y

def divide(x, y):
  """ For Division """
  if y == 0:
    return "Error! Division by zero."
  else:
    return x / y

def floor_division(x, y):
  """ Flor Division """
  if y == 0:
    return "Error! Division by zero."
  else:
    return x // y

def calculator():
  """The main function to run the calculator"""
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Floor Division")
  print("6. Exit")

  while True:
    choice = input("Enter To Perform (1/2/3/4/5/6): ")
    if choice in ('1', '2', '3', '4', '5'):
      try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

      if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

      elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

      elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

      elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")

      elif choice == '5':
        result = floor_division(num1, num2)
        print(f"{num1} // {num2} = {result}")
    
    elif choice == '6':
        print("Exiting calculator. Goodbye!")
        break
    else:
      print("Invalid input. Please enter a valid choice.")

# Run the calculator function
if __name__ == "__main__":
  calculator() 