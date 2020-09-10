prizes = [5,10,50,100,1000]
double = []
for prize in prizes:
    double.append(prize*2)
print(double)

# comprehension method
double =[prize*2 for prize in prizes]
print(double)

# squaring numbers in comprehension method
nums = [2,3,4,5,6,7,8]
square = [num**2 for num in nums if (num**2)%2 == 0]
print(square)