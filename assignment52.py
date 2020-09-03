n = int(input("Enter the length of the sequence: ")) # Do not change this line

fyrsta_stak = 1
annað_stak = 2
þriðja_stak = 3
print(fyrsta_stak)
print(annað_stak)
print(þriðja_stak)

for i in range(1,n-2):
    naesta_stak = fyrsta_stak + annað_stak + þriðja_stak
    print(naesta_stak)
    fyrsta_stak = annað_stak
    annað_stak = þriðja_stak
    þriðja_stak = naesta_stak

    
    