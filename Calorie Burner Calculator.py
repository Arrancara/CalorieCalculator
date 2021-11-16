
def input_checker(user_input):
    """
    Checks the user input to ensure that it is a float.
    Args:
        user_input : float
    Returns:
        user_input : float
    """
    while True:
        try:
            user_input = float(user_input)
            if user_input <= 0:
                user_input = input("Please enter a positive value: ")
                continue
        except ValueError:
            user_input = input("Please enter a numerical value: ")
        else:
            break
    return user_input

def calorie_counter(weight,height,age):
    """
    Calculates the users daily caloric intake dependent on
    weight and height
    Args:
        weight : float
    Returns:
        calories: float
    """
    calories = 10*weight + 6.25*height - 5*age + 5

    return calories

WEIGHT_OBTAINED = False

while not WEIGHT_OBTAINED:
    users_weight = input("Please enter your weight in kilograms: ")
    users_weight = input_checker(users_weight)
    WEIGHT_OBTAINED = True

HEIGHT_OBTAINED = False

while not HEIGHT_OBTAINED:
    users_height = input("Please enter your height in centimeters: ")
    users_height = input_checker(users_height)
    HEIGHT_OBTAINED = True

AGE_OBTAINED  = False
while not AGE_OBTAINED:
    users_age = input("Please enter your age: ")
    users_age = input_checker(users_age)
    AGE_OBTAINED = True

caloric_intake = calorie_counter(users_weight,users_height,users_age)

print("For a sedentary lifestyle, you need to consume " + str(1.2*caloric_intake) + " calories.")