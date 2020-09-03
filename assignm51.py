num_int = int(input("Input a number: "))    # Do not change this line

# Búa til kóða þar sem notandi slær inn tölur, ef hún er neikvæð þá stoppar hann
# athugar ef nýja talan er stærri eða minni en fyrri talan
# skilar út stærstu tölunni sem var slegin inn

num_int_prev = 0
while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > num_int_prev:
        max_int = num_int
    num_int_prev = num_int

print("The maximum is", max_int)    # Do not change this line