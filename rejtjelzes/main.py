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

def getkeyfromvalue(_value):
    key = list(filter(lambda x : my_dict[x] == _value, my_dict))[0]
    return key

def rejtjelzes(_uzenet,_kulcs):
    _rejtjelzett = ""
    mostani_betu = 0
    for i in range(len(_uzenet)):
        mostani_betu = my_dict.get(_uzenet[i]) + my_dict.get(_kulcs[i])
        if mostani_betu > 26:
            mostani_betu = mostani_betu % 27
        _rejtjelzett += getkeyfromvalue(mostani_betu)
    return _rejtjelzett

def rejtjelzesreverse(_rejtjelzett,_kulcs):
    _uzenet = ""
    mostani_betu = 0
    for i in range(len(_rejtjelzett)):
        mostani_betu = my_dict.get(_rejtjelzett[i]) - my_dict.get(_kulcs[i])
        if mostani_betu < 0:
            mostani_betu += 27
        _uzenet += getkeyfromvalue(mostani_betu)
    return _uzenet

print(rejtjelzes("zzz","xxx"))
print(rejtjelzesreverse("vvv","xxx"))