import streamlit as st


def attivita():
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

    risultato = []
    for lettera in chiave:
        risultato.append(lettere[lettera])
    chiave = risultato

    if cripto == 2:
        for i in range(0, len(chiave)):
            chiave[i] = 26 - (chiave[i])

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


# corriere()
# attività() #max 6
# crittografia()

st.header('OPS cracker')
want = st.selectbox('What do u wanna do?', ('Attività', 'Corriere', 'Crittografia'))

print = st.write
input = st.text_input
if want == 'Attività':
    attivita()
elif want == 'Corriere':
    corriere()
elif want == 'Crittografia':
    crittografia()
