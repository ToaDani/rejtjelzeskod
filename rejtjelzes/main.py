my_dict = {"a" : 0,
           "b" : 1,
           "c" : 2,
           "d" : 3,
           "e" : 4,
           "f" : 5,
           "g" : 6,
           "h" : 7,
           "i" : 8,
           "j" : 9,
           "k" : 10,
           "l" : 11,
           "m" : 12,
           "n" : 13,
           "o" : 14,
           "p" : 15,
           "q" : 16,
           "r" : 17,
           "s" : 18,
           "t" : 19,
           "u" : 20,
           "v" : 21,
           "w" : 22,
           "x" : 23,
           "y" : 24,
           "z" : 25,
           " " : 26}

test_uzenet = "helloworld"
test_kulcs = "abcdefgijkl"
test_rejtjelzett = ""

def getkeyfromvalue(_value):
    key = list(filter(lambda x : my_dict[x] == _value, my_dict))[0]
    return key

for i in range(len(test_uzenet)):
    test_rejtjelzett += getkeyfromvalue(my_dict.get(test_uzenet[i])+my_dict.get(test_kulcs[i]))

print(test_rejtjelzett)