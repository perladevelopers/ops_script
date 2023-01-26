import streamlit as st


def attivita():
    try:
        giornii = str(input("inserire i giorni delle attività"))
        priorità = str(input("priorità:"))
        giorni = giornii.split()
        pr = priorità.split()
        c = []
        a = []
        j = []
        a.append(float(giorni[0]))
        print(giorni)

        # a1
        if True:
            if "a1a2" in pr:
                if "a2a3" in pr or "a2a4" in pr or "a2a5" in pr or "a2a6" in pr or "a2a7" in pr or "a2a8" in pr or "a2a9" in pr or "a2a10" in pr or "a2a11" in pr or len(
                        giorni) == 2:
                    d = giorni[1]
                    c.append(float(d))
            if "a1a3" in pr:
                if "a3a4" in pr or "a3a5" in pr or "a3a6" in pr or "a3a7" in pr or "a3a8" in pr or "a3a9" in pr or "a3a10" in pr or "a3a11" in pr or len(
                        giorni) == 3:
                    d = giorni[2]
                    c.append(float(d))
            if "a1a4" in pr:
                if "a4a5" in pr or "a4a6" in pr or "a4a7" in pr or "a4a8" in pr or "a4a9" in pr or "a4a10" in pr or "a4a11" in pr or len(
                        giorni) == 4:
                    d = giorni[3]
                    c.append(float(d))
            if "a1a5" in pr:
                if "a5a6" in pr or "a5a7" in pr or "a5a8" in pr or "a5a9" in pr or "a5a10" in pr or "a5a11" in pr or len(
                        giorni) == 5:
                    d = giorni[4]
                    c.append(float(d))
            if "a1a6" in pr:
                if "a6a7" in pr or "6a8" in pr or "a6a9" in pr or "a6a10" in pr or "a6a11" in pr or len(giorni) == 6:
                    d = giorni[5]
                    c.append(float(d))
            if "a1a7" in pr:
                if "a7a8" in pr or "7a9" in pr or "a7a10" in pr or "a7a11" in pr or len(giorni) == 7:
                    d = giorni[6]
                    c.append(float(d))
            if "a1a8" in pr:
                if "a8a9" in pr or "8a10" in pr or "a8a11" in pr or len(giorni) == 8:
                    d = giorni[7]
                    c.append(float(d))
            if "a1a9" in pr:
                if "a9a10" in pr or "9a11" in pr or len(giorni) == 9:
                    d = giorni[8]
                    c.append(float(d))
            if "a1a10" in pr:
                if "a10a11" in pr or len(giorni) == 10:
                    d = giorni[9]
                    c.append(float(d))
            if "a1a11" in pr:
                d = giorni[10]
                c.append(float(d))

            try:
                a.append(max(c))
            except:
                pass
            c = [0]  # #

        # a2
        if True:
            if "a2a3" in pr:
                if "a3a4" in pr or "a3a5" in pr or "a3a6" in pr or "a3a7" in pr or "a3a8" in pr or "a3a9" in pr or "a3a10" in pr or "a3a11" in pr or len(
                        giorni) == 3:
                    d = giorni[2]
                    c.append(float(d))
            if "a2a4" in pr:
                if "a4a5" in pr or "a4a6" in pr or "a4a7" in pr or "a4a8" in pr or "a4a9" in pr or "a4a10" in pr or "a4a11" in pr or len(
                        giorni) == 4:
                    d = giorni[3]
                    c.append(float(d))
            if "a2a5" in pr:
                if "a5a6" in pr or "a5a7" in pr or "a5a8" in pr or "a5a9" in pr or "a5a10" in pr or "a5a11" in pr or len(
                        giorni) == 5:
                    d = giorni[4]
                    c.append(float(d))
            if "a2a6" in pr:
                if "a6a7" in pr or "6a8" in pr or "a6a9" in pr or "a6a10" in pr or "a6a11" in pr or len(giorni) == 6:
                    d = giorni[5]
                    c.append(float(d))
            if "a2a7" in pr:
                if "a7a8" in pr or "7a9" in pr or "a7a10" in pr or "a7a11" in pr or len(giorni) == 7:
                    d = giorni[6]
                    c.append(float(d))
            if "a2a8" in pr:
                if "a8a9" in pr or "8a10" in pr or "a8a11" in pr or len(giorni) == 8:
                    d = giorni[7]
                    c.append(float(d))
            if "a2a9" in pr:
                if "a9a10" in pr or "9a11" in pr or len(giorni) == 9:
                    d = giorni[8]
                    c.append(float(d))
            if "a2a10" in pr:
                if "a10a11" in pr or len(giorni) == 10:
                    d = giorni[9]
                    c.append(float(d))
            if "a2a11" in pr:
                d = giorni[10]
                c.append(float(d))

            try:
                a.append(max(c))
            except:
                pass
            c = [0]

        # a3
        if True:
            if "a3a4" in pr:
                if "a4a5" in pr or "a4a6" in pr or "a4a7" in pr or "a4a8" in pr or "a4a9" in pr or "a4a10" in pr or "a4a11" in pr or len(
                        giorni) == 4:
                    d = giorni[3]
                    c.append(float(d))
            if "a3a5" in pr:
                if "a5a6" in pr or "a5a7" in pr or "a5a8" in pr or "a5a9" in pr or "a5a10" in pr or "a5a11" in pr or len(
                        giorni) == 5:
                    d = giorni[4]
                    c.append(float(d))
            if "a3a6" in pr:
                if "a6a7" in pr or "6a8" in pr or "a6a9" in pr or "a6a10" in pr or "a6a11" in pr or len(giorni) == 6:
                    d = giorni[5]
                    c.append(float(d))
            if "a3a7" in pr:
                if "a7a8" in pr or "7a9" in pr or "a7a10" in pr or "a7a11" in pr or len(giorni) == 7:
                    d = giorni[6]
                    c.append(float(d))
            if "a3a8" in pr:
                if "a8a9" in pr or "8a10" in pr or "a8a11" in pr or len(giorni) == 8:
                    d = giorni[7]
                    c.append(float(d))
            if "a3a9" in pr:
                if "a9a10" in pr or "9a11" in pr or len(giorni) == 9:
                    d = giorni[8]
                    c.append(float(d))
            if "a3a10" in pr:
                if "a10a11" in pr or len(giorni) == 10:
                    d = giorni[9]
                    c.append(float(d))
            if "a3a11" in pr:
                d = giorni[10]
                c.append(float(d))

            try:
                a.append(max(c))
            except:
                pass
            c = [0]

        # a4
        if True:
            if "a4a5" in pr:
                if "a5a6" in pr or "a5a7" in pr or "a5a8" in pr or "a5a9" in pr or "a5a10" in pr or "a5a11" in pr or len(
                        giorni) == 5:
                    d = giorni[4]
                    c.append(float(d))
            if "a4a6" in pr:
                if "a6a7" in pr or "6a8" in pr or "a6a9" in pr or "a6a10" in pr or "a6a11" in pr or len(giorni) == 6:
                    d = giorni[5]
                    c.append(float(d))
            if "a4a7" in pr:
                if "a7a8" in pr or "7a9" in pr or "a7a10" in pr or "a7a11" in pr or len(giorni) == 7:
                    d = giorni[6]
                    c.append(float(d))
            if "a4a8" in pr:
                if "a8a9" in pr or "8a10" in pr or "a8a11" in pr or len(giorni) == 8:
                    d = giorni[7]
                    c.append(float(d))
            if "a4a9" in pr:
                if "a9a10" in pr or "9a11" in pr or len(giorni) == 9:
                    d = giorni[8]
                    c.append(float(d))
            if "a4a10" in pr:
                if "a10a11" in pr or len(giorni) == 10:
                    d = giorni[9]
                    c.append(float(d))
            if "a4a11" in pr:
                d = giorni[10]
                c.append(float(d))

            try:
                a.append(max(c))
            except:
                pass
            c = [0]

        # a5
        if True:
            if "a5a6" in pr:
                if "a6a7" in pr or "6a8" in pr or "a6a9" in pr or "a6a10" in pr or "a6a11" in pr or len(giorni) == 6:
                    d = giorni[5]
                    c.append(float(d))
            if "a5a7" in pr:
                if "a7a8" in pr or "7a9" in pr or "a7a10" in pr or "a7a11" in pr or len(giorni) == 7:
                    d = giorni[6]
                    c.append(float(d))
            if "a5a8" in pr:
                if "a8a9" in pr or "8a10" in pr or "a8a11" in pr or len(giorni) == 8:
                    d = giorni[7]
                    c.append(float(d))
            if "a5a9" in pr:
                if "a9a10" in pr or "9a11" in pr or len(giorni) == 9:
                    d = giorni[8]
                    c.append(float(d))
            if "a5a10" in pr:
                if "a10a11" in pr or len(giorni) == 10:
                    d = giorni[9]
                    c.append(float(d))
            if "a5a11" in pr:
                d = giorni[10]
                c.append(float(d))

            try:
                a.append(max(c))
            except:
                pass
            c = [0]

        # a6
        if True:
            if "a6a7" in pr:
                if "a7a8" in pr or "7a9" in pr or "a7a10" in pr or "a7a11" in pr or len(giorni) == 7:
                    d = giorni[6]
                    c.append(float(d))
            if "a6a8" in pr:
                if "a8a9" in pr or "8a10" in pr or "a8a11" in pr or len(giorni) == 8:
                    d = giorni[7]
                    c.append(float(d))
            if "a6a9" in pr:
                if "a9a10" in pr or "9a11" in pr or len(giorni) == 9:
                    d = giorni[8]
                    c.append(float(d))
            if "a6a10" in pr:
                if "a10a11" in pr or len(giorni) == 10:
                    d = giorni[9]
                    c.append(float(d))
            if "a6a11" in pr:
                d = giorni[10]
                c.append(float(d))

            try:
                a.append(max(c))
            except:
                pass
            c = [0]

        # a7
        if True:
            if "a7a8" in pr:
                if "a8a9" in pr or "8a10" in pr or "a8a11" in pr or len(giorni) == 8:
                    d = giorni[7]
                    c.append(float(d))
            if "a7a9" in pr:
                if "a9a10" in pr or "9a11" in pr or len(giorni) == 9:
                    d = giorni[8]
                    c.append(float(d))
            if "a7a10" in pr:
                if "a10a11" in pr or len(giorni) == 10:
                    d = giorni[9]
                    c.append(float(d))
            if "a7a11" in pr:
                d = giorni[10]
                c.append(float(d))

            try:
                a.append(max(c))
            except:
                pass
            c = [0]

        # a8
        if True:
            if "a8a9" in pr:
                if "a9a10" in pr or "9a11" in pr or len(giorni) == 9:
                    d = giorni[8]
                    c.append(float(d))
            if "a8a10" in pr:
                if "a10a11" in pr or len(giorni) == 10:
                    d = giorni[9]
                    c.append(float(d))
            if "a8a11" in pr:
                d = giorni[10]
                c.append(float(d))

            try:
                a.append(max(c))
            except:
                pass
            c = 0

        # a9
        if True:
            if "a9a10" in pr:
                if "a10a11" in pr or len(giorni) == 10:
                    d = giorni[9]
                    c.append(float(d))
            if "a9a11" in pr:
                d = giorni[10]
                c.append(float(d))

            try:
                a.append(max(c))
            except:
                pass
            c = 0

        if "a10a11" in pr:
            d = giorni[10]
            c.append(float(d))

        try:
            a.append(max(c))
        except:
            pass
        c = 0
        a = list(dict.fromkeys(a))
        print(a)
        print("risultato:", int(sum(a)))
    except:
        pass


def interpreter():
    import streamlit as st

    a = """A = 0
   P = 3
   C = 4

   for i in range(A, P, C):
       D = P + C + i

   print(D)
   """

    st.title('ADAM2')
    st.header('Python Interpreter')
    b = st.text_area('scrivi il codice')

    butt = st.button('Run Code')
    write = st.write
    if butt:
        st.write(exec(b))


def corriere():
    portata = int(input("portata del carro:"))
    numero_di_pacchi = int(input("numero di pacchi"))
    a = str(input("valori:"))
    b = a.split()
    pesi = []
    valori = []
    x = []

    if len(b) < 3:
        pesi.extend(int(b[1]))
        valori.extend(int(b[0]))

    elif len(b) < 5:
        pesi.extend((int(b[1]), int(b[3])))
        valori.extend((int(b[0]), int(b[2])))

    elif len(b) < 7:
        pesi.extend((int(b[1]), int(b[3]), int(b[5])))
        valori.extend((int(b[0]), int(b[2]), int(b[4])))

    elif len(b) < 9:
        pesi.extend((int(b[1]), int(b[3]), int(b[5]), int(b[7])))
        valori.extend((int(b[0]), int(b[2]), int(b[4]), int(b[6])))

    elif len(b) < 11:
        pesi.extend((int(b[1]), int(b[3]), int(b[5]), int(b[7]), int(b[9])))
        valori.extend((int(b[0]), int(b[2]), int(b[4]), int(b[6]), int(b[8])))

    elif len(b) < 13:
        pesi.extend((int(b[1]), int(b[3]), int(b[5]), int(b[7]), int(b[9]), int(b[11])))
        valori.extend((int(b[0]), int(b[2]), int(b[4]), int(b[6]), int(b[8]), int(b[10])))

    elif len(b) < 15:
        pesi.extend((int(b[1]), int(b[3]), int(b[5]), int(b[7]), int(b[9]), int(b[11]), int(b[13])))
        valori.extend((int(b[0]), int(b[2]), int(b[4]), int(b[6]), int(b[8]), int(b[10]), int(b[12])))

    elif len(b) < 17:
        pesi.extend((int(b[1]), int(b[3]), int(b[5]), int(b[7]), int(b[9]), int(b[11]), int(b[13]), int(b[15])))
        valori.extend((int(b[0]), int(b[2]), int(b[4]), int(b[6]), int(b[8]), int(b[10]), int(b[12]), int(b[14])))

    for i in range(0, len(pesi)):
        for j in range(0, len(pesi)):
            if j != i and numero_di_pacchi == 3:
                for z in range(0, len(pesi)):
                    if z != j and z != i:
                        p = pesi[i] + pesi[j] + pesi[z]
                        v = valori[i] + valori[j] + valori[z]
                        if p < portata:
                            xx = [float(v), i + 1, j + 1, z + 1]
                            x.append(xx)
            elif numero_di_pacchi == 2 and j != i:
                p = pesi[i] + pesi[j]
                v = valori[i] + valori[j]
                if p < portata:
                    xx = [float(v), i + 1, j + 1]
                    x.append(xx)

    xxx = max(x)
    xxx = sorted(xxx)
    print(xxx)

def crittografia():
    cripto = int(input("criptare(1) o decriptare(2)?"))
    parola = str(input("parola da crittare")).replace(' ', '')
    chiave = str(input("chiave:"))
    chiave = tuple(chiave)
    caratteri = list(parola)
    alfabeto = tuple("abcdefghijklmnopqrstuvwxyz")
    posizione = range(len(alfabeto))
    lettere = dict(zip(alfabeto, posizione))
    ripetizioni = int(input("ripetizioni"))


    risultato = []
    for lettera in chiave:
        risultato.append(int(lettere[lettera]))
    chiave = risultato

    if cripto == 2:
        for i in range(0, len(chiave)):
            chiave[i] = (26 - (chiave[i])) * ripetizioni

    else:
        for i in range(0, len(chiave)):
            chiave[i] = chiave[i] * ripetizioni


    def crittografo(j):
        if caratteri[j] == "a":
            caratteri[j] = ("b")
        elif caratteri[j] == "b":
            caratteri[j] = ("c")
        elif caratteri[j] == "c":
            caratteri[j] = ("d")
        elif caratteri[j] == "d":
            caratteri[j] = ("e")
        elif caratteri[j] == "e":
            caratteri[j] = ("f")
        elif caratteri[j] == "f":
            caratteri[j] = ("g")
        elif caratteri[j] == "g":
            caratteri[j] = ("h")
        elif caratteri[j] == "h":
            caratteri[j] = ("i")
        elif caratteri[j] == "i":
            caratteri[j] = ("j")
        elif caratteri[j] == "j":
            caratteri[j] = ("k")
        elif caratteri[j] == "k":
            caratteri[j] = ("l")
        elif caratteri[j] == "l":
            caratteri[j] = ("m")
        elif caratteri[j] == "m":
            caratteri[j] = ("n")
        elif caratteri[j] == "n":
            caratteri[j] = ("o")
        elif caratteri[j] == "o":
            caratteri[j] = ("p")
        elif caratteri[j] == "p":
            caratteri[j] = ("q")
        elif caratteri[j] == "q":
            caratteri[j] = ("r")
        elif caratteri[j] == "r":
            caratteri[j] = ("s")
        elif caratteri[j] == "s":
            caratteri[j] = ("t")
        elif caratteri[j] == "t":
            caratteri[j] = ("u")
        elif caratteri[j] == "u":
            caratteri[j] = ("v")
        elif caratteri[j] == "v":
            caratteri[j] = ("w")
        elif caratteri[j] == "w":
            caratteri[j] = ("x")
        elif caratteri[j] == "x":
            caratteri[j] = ("y")
        elif caratteri[j] == "y":
            caratteri[j] = ("z")
        elif caratteri[j] == "z":
            caratteri[j] = ("a")

    for i in range(0, int(chiave[0])):
        for j in range(0, len(caratteri), len(chiave)):
            crittografo(j)

    if len(chiave) > 1:
        for i in range(0, int(chiave[1])):
            for j in range(1, len(caratteri), len(chiave)):
                crittografo(j)

    if len(chiave) > 2:
        for i in range(0, int(chiave[2])):
            for j in range(2, len(caratteri), len(chiave)):
                crittografo(j)

    if len(chiave) > 3:
        for i in range(0, int(chiave[3])):
            for j in range(3, len(caratteri), len(chiave)):
                crittografo(j)

    if len(chiave) > 4:
        for i in range(0, int(chiave[4])):
            for j in range(4, len(caratteri), len(chiave)):
                crittografo(j)

    if len(chiave) > 5:
        for i in range(0, int(chiave[5])):
            for j in range(5, len(caratteri), len(chiave)):
                crittografo(j)

    print(caratteri)


def canali():
    canali = str(input('canali: '))
    direzioni = str(input('direzioni: '))
    lista_canali = canali.split(' ')
    lista_direzioni = direzioni.split(' ')
    # lista_direzioni = ['ac', 'bc', 'fe', 'cd', 'ge']
    # lista_canali = ['0', '0', '11.8', '4', '5', '2', '7.3']
    d = 0

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    ii = 0
    m = 0

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'l', 'm']

    def count(v):
        C = 0
        for j in lista_direzioni:
            if j[0] == v:
                C += 1

        return C

    for i, valore in enumerate(lista_canali):
        if i == 0:
            a = float(valore)
        elif i == 1:
            b = float(valore)
        elif i == 2:
            c = float(valore)
        elif i == 3:
            d = float(valore)
        elif i == 4:
            e = float(valore)
        elif i == 5:
            f = float(valore)
        elif i == 6:
            g = float(valore)
        elif i == 7:
            h = float(valore)
        elif i == 8:
            ii = float(valore)
        elif i == 9:
            m = float(valore)

    for i in lista_direzioni:
        if i[1] == 'a':
            if i[0] == 'b':
                a += (a / count('b'))
            elif i[0] == 'c':
                a += (c / count('c'))
            elif i[0] == 'd':
                a += (d / count('d'))
            elif i[0] == 'e':
                a += (e / count('e'))
            elif i[0] == 'f':
                a += (f / count('f'))
            elif i[0] == 'g':
                a += (g / count('g'))
            elif i[0] == 'h':
                a += (h / count('h'))
            elif i[0] == 'i':
                a += (ii / count('i'))
            elif i[0] == 'm':
                a += (m / count('m'))
        elif i[1] == 'b':
            if i[0] == 'a':
                b += (a / count('a'))
            elif i[0] == 'c':
                b += (c / count('c'))
            elif i[0] == 'd':
                b += (d / count('d'))
            elif i[0] == 'e':
                b += (e / count('e'))
            elif i[0] == 'f':
                b += (f / count('f'))
            elif i[0] == 'g':
                b += (g / count('g'))
            elif i[0] == 'h':
                b += (h / count('h'))
            elif i[0] == 'i':
                b += (ii / count('i'))
            elif i[0] == 'm':
                b += (m / count('m'))
        elif i[1] == 'c':
            if i[0] == 'a':
                c += (a / count('a'))
                print(i[0], a / count('a'))
            elif i[0] == 'b':
                c += (b / count('b'))
                print(i[0], b / count('b'))
            elif i[0] == 'd':
                c += (d / count('d'))
            elif i[0] == 'e':
                c += (e / count('e'))
            elif i[0] == 'f':
                c += (f / count('f'))
            elif i[0] == 'g':
                c += (g / count('g'))
            elif i[0] == 'h':
                c += (h / count('h'))
            elif i[0] == 'i':
                c += (ii / count('i'))
            elif i[0] == 'm':
                c += (m / count('m'))
        elif i[1] == 'd':
            if i[0] == 'a':
                d += (a / count('a'))
            elif i[0] == 'b':
                d += (b / count('b'))
            elif i[0] == 'c':
                d += (c / count('c'))
                print(i[0], c / count('c'))
            elif i[0] == 'e':
                d += (e / count('e'))
            elif i[0] == 'f':
                d += (f / count('f'))
                print(i[0], f / count('f'))
            elif i[0] == 'g':
                d += (g / count('g'))
            elif i[0] == 'h':
                d += (h / count('h'))
            elif i[0] == 'i':
                d += (ii / count('i'))
            elif i[0] == 'm':
                d += (m / count('m'))
        elif i[1] == 'e':
            if i[0] == 'a':
                e += (a / count('a'))
            elif i[0] == 'b':
                e += (b / count('b'))
            elif i[0] == 'c':
                e += (c / count('c'))
            elif i[0] == 'd':
                e += (d / count('d'))
            elif i[0] == 'f':
                e += (f / count('f'))
            elif i[0] == 'g':
                e += (g / count('g'))
                print(i[0], g / count('g'))
            elif i[0] == 'h':
                e += (h / count('h'))
            elif i[0] == 'i':
                e += (ii / count('i'))
            elif i[0] == 'm':
                e += (m / count('m'))
        elif i[1] == 'f':
            if i[0] == 'a':
                f += (a / count('a'))
            elif i[0] == 'b':
                f += (b / count('b'))
            elif i[0] == 'c':
                f += (c / count('c'))
            elif i[0] == 'd':
                f += (d / count('d'))
            elif i[0] == 'e':
                f += (e / count('e'))
            elif i[0] == 'g':
                f += (g / count('g'))
            elif i[0] == 'h':
                f += (h / count('h'))
            elif i[0] == 'i':
                f += (ii / count('i'))
            elif i[0] == 'm':
                f += (m / count('m'))
        elif i[1] == 'g':
            if i[0] == 'a':
                g += (a / count('a'))
            elif i[0] == 'b':
                g += (b / count('b'))
            elif i[0] == 'c':
                g += (c / count('c'))
            elif i[0] == 'd':
                g += (d / count('d'))
            elif i[0] == 'e':
                g += (e / count('e'))
            elif i[0] == 'f':
                g += (f / count('f'))
            elif i[0] == 'h':
                g += (h / count('h'))
            elif i[0] == 'i':
                g += (ii / count('i'))
            elif i[0] == 'm':
                g += (m / count('m'))
        elif i[1] == 'h':
            if i[0] == 'a':
                h += (a / count('a'))
            elif i[0] == 'b':
                h += (b / count('b'))
            elif i[0] == 'c':
                h += (c / count('c'))
            elif i[0] == 'd':
                h += (d / count('d'))
            elif i[0] == 'e':
                h += (e / count('e'))
            elif i[0] == 'f':
                h += (f / count('f'))
            elif i[0] == 'g':
                h += (g / count('g'))
            elif i[0] == 'i':
                h += (ii / count('i'))
            elif i[0] == 'm':
                h += (m / count('m'))
        elif i[1] == 'i':
            if i[0] == 'a':
                ii += (a / count('a'))
            elif i[0] == 'b':
                ii += (b / count('b'))
            elif i[0] == 'c':
                ii += (c / count('c'))
            elif i[0] == 'd':
                ii += (d / count('d'))
            elif i[0] == 'e':
                ii += (e / count('e'))
            elif i[0] == 'f':
                ii += (f / count('f'))
            elif i[0] == 'g':
                ii += (g / count('g'))
            elif i[0] == 'h':
                ii += (h / count('h'))
            elif i[0] == 'm':
                ii += (m / count('m'))
        elif i[1] == 'm':
            if i[0] == 'a':
                m += (a / count('a'))
            elif i[0] == 'b':
                m += (b / count('b'))
            elif i[0] == 'c':
                m += (c / count('c'))
            elif i[0] == 'd':
                m += (d / count('d'))
            elif i[0] == 'e':
                m += (e / count('e'))
            elif i[0] == 'f':
                m += (f / count('f'))
            elif i[0] == 'g':
                m += (g / count('g'))
            elif i[0] == 'h':
                m += (h / count('h'))
            elif i[0] == 'i':
                m += (ii / count('i'))
        print(i)

    print(f' a:{a}, b:{b}, c:{c}, d:{d}, e:{e}, f:{f}, g:{g}, h:{h}, i:{ii}, l:{m}')
    totale = (a, b, c, d, e, f, g, h, ii, m)
    print(max(totale))

    r = 'ab bc bd ce cf df dg di eh fh lh hm'
    h = '8 4 2 3 6 9 6 1 1 10'


# corriere()
# attivita() #max 6
# crittografia()
# canali()

st.header('OPS cracker')
want = st.selectbox('What do u wanna do?', ('Attività', 'Corriere', 'Crittografia', 'Linguaggio'))

print = st.write
input = st.text_input
if want == 'Attività':
    try:
        attivita()
    except:
        pass
elif want == 'Corriere':
    try:
        corriere()
    except:
        pass
elif want == 'Crittografia':
    try:
        crittografia()
    except:
        pass
elif want == 'Linguaggio':
    interpreter()

elif want == 'Canali':
    interpreter()
    try:
        canali()
    except:
        pass

