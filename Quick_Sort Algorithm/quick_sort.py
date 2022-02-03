import random

def quick_sort(sequence): # sequqence of unsorted values
    length = len(sequence) # Return the number of items in a list
    if length <= 1: 
        return sequence
    else: 
        pivot = sequence.pop() #removes the last element in array and stores in pivot

    numbers_bigger = [] # creates an empty array for all potential values that may be bigger then pivot
    numbers_smaller = [] # creates an empty array for all potential values that may be smaller then pivot
    for number in sequence:  #
        if number > pivot: 
            numbers_bigger.append(number) #if the number is greater then the pivot, add it to number
        else: 
            numbers_smaller.append(number)
    return quick_sort(numbers_smaller) + [pivot] + quick_sort(numbers_bigger) # goes over and over untill logic breaks thus array is sorted

print(quick_sort(random.sample(range(0, 8), 8))) # picks a random 8 random integers ranging from 0-8 and stores in array my_arr = random.sample(range(0, 8), 8) 

