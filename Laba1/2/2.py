isGrowing = True


def check(arr):
    for i in range(0, len(arr) - 2):
        if arr[i] > arr[i + 1]:
            return False
        else:
        	return True


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10]
if check(arr2):
	print('True')
else:
	print('False')
if check(arr1):
	print('True')
else:
	print('False')