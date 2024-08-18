def add_numbers(a, b):
  """
  adds two numeros together
  """
  result = a + b
  return result

def print_message(name, age):
  """
  greets the user
  """
  print(f"Hello, {name}! You are {age} years old.")
    
def calc_area_circle (r):
    """
    calculate the area of a circle
    """
    area = 3.14 * r * r
    return area

def check_age(age): 
    """
    Sees if the user is older than 18
    """
    if age >= 18: 
        print("You are an adult.") 
    else: 
        print("You are a minor.")

# main program starts here
name = "Alice"
age = 25

print_message(name , age)
check_age(age)

x = 10
y = 20
sum = add_numbers(x ,y)
print("The sum is:",sum)

radius=5
area = calc_area_circle(radius)
print ("The area of the circle is:",area)
