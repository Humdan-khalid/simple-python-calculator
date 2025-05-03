def calculator():
  print("=====Calculator=====\n")
  try:
    value1 : int = int(input("Enter your value1: "))
    select_operator : str = input("Enter your operator(+ - * / // **) ")
    value2 : int = int(input("Enter your value2: "))
  except ValueError:
    print("please enter a right value!")
    return

  if select_operator == "+":
    print(f"{value1} + {value2} = {value1 + value2}")
  elif select_operator == "-":
    print(f"{value1} - {value2} = {value1 - value2}")
  elif select_operator == "*":
    print(f"{value1} * {value2} = {value1 * value2}")
  elif select_operator == "/":
    if value2 == 0:
      print(f"cannot divide by zero.")
    else:
      print(f"{value1} / {value2} = {value1 / value2}")
  elif select_operator == "//":
    print(f"{value1} // {value2} = {value1 // value2}")
  else:
    print("please enter a right value")
calculator()
  