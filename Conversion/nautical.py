def height_inches():
    height = input("What is you heigh in feet and inches? (ie 6(feet),4(inches)\n:")
    new_height = height.split(",")
    feet = int(new_height[0])
    inches = int(new_height[1])
    feet_inches = feet * 12
    inches_tall = feet_inches + inches
    return inches_tall


def nautical_tall():
    nautial_miles_tall = height_inches() / 72913.39
    new_height = str(nautial_miles_tall)
    new_new_height = new_height[0:8]
    return new_new_height


print(nautical_tall())
