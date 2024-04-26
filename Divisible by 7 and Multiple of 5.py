
#Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).


#Create empty obj for results
result = []

for num in range(1500,2701):
    #check if this is divisible by 7 and multiple of 5
    if num % 7 and num % 5 == 0:
        result.append(num)      #this will append the result to the list

print("Numbers between 1500 and 2700 (both included), that are divisible by 7 and multiples of 5: ")

print(result)