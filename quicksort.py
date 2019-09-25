import sys

def quicksort(array):
    # return statement for recurrsion
    if len(array) < 2:
        return array

    # variables we will need to setup 
    arrayiter = iter(array)
    pivot = next(arrayiter)
    left = []
    right = []
    equal = [pivot]

    # place each value in it's appropriate array
    for current in arrayiter:
        if current < pivot:
            left.append(current)
        elif current > pivot:
            right.append(current)
        else:
            equal.append(current)
    print("Pivot and numbers equal to it: %s, Numbers less than: %s, Numbers more than: %s" % (equal, left, right))
    # recursively call quicksort on left and right side then combine with pivot
    return quicksort(left) + equal + quicksort(right) 




# exit if a list was not given
if not len(sys.argv) > 1:
    print("usage: python " + sys.argv[0], " <comma seperated list>")
    exit(1)

# init an array and add the string to it
array = []
for x in sys.argv[1].split(','):
    array.append(int(x))


# call the quicksort and print the results
array = quicksort(array)
print("\nFinal sorted array: %s" % (array))
