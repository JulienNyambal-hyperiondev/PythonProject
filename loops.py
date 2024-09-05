numbers = [1,2,3,4,5, 6,7,8,9,10]

total = 0
counter = 0

while counter < len(numbers):
    total = total + numbers[counter]
    print(f"The current number is {counter} and the total is {total}")
    counter = counter + 1
print(f"The total is {total}")


# contacts = ["Julien", "Riaan", "Armand"]

# for contact in contacts:
#     print(f"Contact : {contact}")