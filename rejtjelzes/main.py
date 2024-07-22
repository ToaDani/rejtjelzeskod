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


def rejtjelzes(_uzenet : str,_kulcs : str) -> str:
    if len(_kulcs) < len(_uzenet):
        return "A kulcs rövidebb az üzenetnél"
    else:
        _rejtjelzett = ""
        mostani_betu = 0
        for i in range(len(_uzenet)):
            mostani_betu = my_dict.get(_uzenet[i]) + my_dict.get(_kulcs[i])
            if mostani_betu > 26:
                mostani_betu = mostani_betu % 27
            _rejtjelzett += getkeyfromvalue(mostani_betu)
        return _rejtjelzett


def rejtjelzesreverse(_rejtjelzett : str,_kulcs : str) -> str:
    if len(_kulcs) < len(_rejtjelzett):
        return "A kulcs rövidebb az üzenetnél"
    else:
        _uzenet = ""
        mostani_betu = 0
        for i in range(len(_rejtjelzett)):
            mostani_betu = my_dict.get(_rejtjelzett[i]) - my_dict.get(_kulcs[i])
            if mostani_betu < 0:
                mostani_betu += 27
            _uzenet += getkeyfromvalue(mostani_betu)
        return _uzenet

#2.feladat ___________________

angolszotar = []
for i in open("words.txt","r").readlines():
    angolszotar.append((i.strip("\n")+" "))

kodoltszo2 = rejtjelzes("curiosity killed the cat","abcdefghijlkmnopqrstuwabcdefghijlkmnopqrstuw")
kodoltszo1 = rejtjelzes("early bird catches the worm","abcdefghijlkmnopqrstuwabcdefghijlkmnopqrstuw")

kulcs = ""

"""
for i in angolszotar:
    kulcstoredek = rejtjelzesreverse(kodoltszo1[0:len(i)],i)
    try:
        szotoredek = rejtjelzesreverse(kodoltszo2[0:len(kulcstoredek)],kulcstoredek)
        for j in angolszotar:
            if szotoredek == j[:len(szotoredek)]:
                szomaradek = j[len(szotoredek):]
                kulcstoredek2 = rejtjelzesreverse(kodoltszo2[len(szotoredek):len(j)],szomaradek)
                szotoredek2 = rejtjelzesreverse(kodoltszo1[len(szotoredek):len(szotoredek)+len(szomaradek)],kulcstoredek2)
                for v in angolszotar:
                    if szotoredek2 == v[:len(szotoredek2)]:
                        None
    except:
        None
"""
def szotarban(_szotoredek):
    szo = ""
    for szavak in angolszotar:
        if _szotoredek == szavak[:len(_szotoredek)]:
            szo = szavak
    return szo

def gyujtes(_szotoredek,_szolista,_angolszotar):
    szolistavalt = _szolista
    for i in angolszotar:
        if _szotoredek == i[:len(_szotoredek)]:
            szolistavalt.append(i)
    print(szolistavalt)
    return szolistavalt

def kettouzenetdekodolasa(_szo,_kodoltuzenet1,_kodoltuzenet2,_kulcs):
    try:
        kulcstoredek = rejtjelzesreverse(_kodoltuzenet1[0:len(_szo)], _szo)
        szotoredek = rejtjelzesreverse(_kodoltuzenet2[0:len(kulcstoredek)], kulcstoredek)
        szotarbanvalt = 1
        szotoredektomb = szotoredek.split(" ")
        for i in range(len(szotoredektomb)-1):
            szotoredektomb[i] = szotoredektomb[i]+" "
        for i in szotoredektomb:
            if szotarban(i) == "":
                szotarbanvalt = 0
        if szotarbanvalt == 0:
            return
        else:
            szolista = []
            szavak_eleje = ""
            for szavak in szotoredektomb:
                if 0 < len(szotoredektomb)-1:
                    szavak_eleje += szavak
                    print("szavak eleje",szavak_eleje)
                else:
                    gyujtott_szavak = gyujtes(szavak,szolista,angolszotar)
            szostring = ""
            for szavak in gyujtott_szavak:
                szostring += szavak

                print("szosztring",szostring)
            _kulcs = kettouzenetdekodolasa(szostring, _kodoltuzenet2, _kodoltuzenet1, kulcstoredek)
    except:
        return

for i in angolszotar:
    if (kettouzenetdekodolasa(i, kodoltszo1, kodoltszo2, kulcs)) != None:
        print(kettouzenetdekodolasa(i,kodoltszo1,kodoltszo2,kulcs),i)


