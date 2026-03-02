#Create a list
#Prompt the user to enter five foods, and store the responses in the list
#Display the list on one line, each item seperated by commas
#Calculate how many characters were entered and display this to the user
#Hint: Using the len() function will be useful here
#Below is a sample of what your output might look like. You do not have to follow the text exactly.
#
#Enter a food: pizza
#Enter a food: beef jerkey
#Enter a food: rice triangles
#Enter a food: steamed chinese bun
#Enter a food: fried chicken
#
#Your entered foods are:
#pizza, beef jerkey, rice triangles, steamed chinese bun, fried chicken 
#You entered a total of 62 characters
foods = []
for i in range(5):
    foods.append(input(f"Enter a food {i+1}/5: "))
chars = 0
for x in foods:
    for x in x:
        chars = chars + 1
print("your entered foods are: ")
print(", ".join(foods))
print(f"you entered a total number of {chars} characters")
