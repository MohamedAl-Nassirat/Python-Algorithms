import random

def quick_sort(sequence):
    length = len(sequence)


    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()


    num_bigger = []
    num_smaller = []


    for number in sequence:
        if number > pivot:
            num_bigger.append(number)
        else:
            num_smaller.append(number)


    return quick_sort(num_bigger) + [pivot] + quick_sort(num_smaller)
    
print(quick_sort(random.sample(range(0, 8), 8)))
