numbers=[1,2,2,3,4,5]
print(numbers)
mean=sum(numbers)/len(numbers)
minimum=min(numbers)
maximum=max(numbers)
mode=max(numbers,key=numbers.count)
numbers.sort()
n=len(numbers)
median=numbers[n//2]

print("Min=",minimum)
print("Max=",maximum)
print( "Mean=",mean)
print("Mode=",mode)
print("Median",median)
