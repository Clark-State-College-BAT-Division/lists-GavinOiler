#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class
# video url: https://youtu.be/VGrRdUunjXg
numbers = []
for i in range(5):
    numbers.append(int(input(f"Enter a number {i+1}/5: ")))
print(f'Entered as: {numbers}')
numbers.sort()
print(f'Small to Large: {numbers}')
numbers.sort(reverse = True)
print(f'Large to Small: {numbers}')
total = 0
for i in numbers:
    total = total + i
print(f'The mean is of all numbers is {total / len(numbers)} the median is {numbers[2]}')
