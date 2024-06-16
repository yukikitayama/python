
def modify_array(arr):
    arr.append(4)
    print("In modify_array")
    print(arr)


if __name__ == "__main__":
    nums = [1, 2, 3]

    print("Before modify_array")
    print(nums)

    # This is not pass-by-value
    modify_array(nums)

    print("After modify_array")
    print(nums)
