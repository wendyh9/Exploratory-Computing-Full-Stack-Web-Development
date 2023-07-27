nums = input("Enter at least two numbers: ")
nums_arr = nums.split()

if (len(nums_arr) < 2):
    print("You did not enter at least two numbers!")

else:
    sum = 0
    for num in nums_arr:
        sum = sum + int(num)
    print(f'Your sum is {sum}')
