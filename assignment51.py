num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
num_int_prev = 0
while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > num_int_prev:
        max_int = num_int
    num_int_prev = num_int

print("The maximum is", max_int)    # Do not change this line
