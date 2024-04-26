dog_age= int(input("Input age of dog: "))

dog_weight = int(input("Input dog weight:"))

dog_table_small = [
    (1,15),
    (2,24),
    (3,28),
    (4,32),
    (5,36),
    (6,40),
    (7,44),
    (8,48),
    (9,52),
    (10,56),
    (11,60),
    (12,64)
]

dog_table_medium = [
    (1,15),
    (2,24),
    (3,28),
    (4,32),
    (5,36),
    (6,42),
    (7,47),
    (8,51),
    (9,56),
    (10,60),
    (11,65),
    (12,69)
]


dog_table_large = [
    (1,15),
    (2,24),
    (3,28),
    (4,32),
    (5,36),
    (6,45),
    (7,50),
    (8,55),
    (9,61),
    (10,66),
    (11,72),
    (12,77)
]

# define dogs category
def categorize_dog(dog_weight):
    if dog_weight < 9:
        size = "small"
    elif 9 <= dog_weight <= 23:
        size = "medium"
    else:
        size = "large"
    return size



def get_human_age(dog_age):
    # Determine the appropriate dog table based on size
    size_table = globals()[f"dog_table_{size}"]

    # Search for the human age in the corresponding dog table
    for row in size_table:
        if row[0] == dog_age:
            return row[1]
    return None


# Determine dog size category
size = categorize_dog(dog_weight)

# Get human age from size table
human_age = get_human_age(dog_age)

# Print the result
if human_age is not None:
    print(f"In human years, your dog is {human_age} years old.")
    print(f"Your dog's size is {size}.")
else:
    print("Dog age not found in the selected size table.")