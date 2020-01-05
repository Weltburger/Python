isGrowing = True


def check(arr):
    for i in range(0, len(arr) - 2):
        if arr[i] > arr[i + 1]:
            global isGrowing
            isGrowing = False
            break


def conclusion():
    global isGrowing
    print(isGrowing)
    isGrowing = True


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10]
check(arr2)
conclusion()
check(arr2)
conclusion()
check(arr1)
conclusion()
check(arr2)
conclusion()
check(arr1)
conclusion()