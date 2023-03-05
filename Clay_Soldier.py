import streamlit as st
import random as rd

try:
    zones = ['Desert', 'Meadow', 'Pine', 'Birch', 'Savana', 'Miras', 'Plains', 'Autumn', 'Shrubble', 'Dried']
    objectives = {
        'Conquista le zone Sabbiose ': '(Desert, Dried)',
        'Conquista le zone Idriche ': '(Miras, Plains)',
        'Conquista le zone Rocciose ': '(Savana, Shrubble)',

        'Conquista le zone di Foresta ': '(Pine, Miras)',
        'Conquista i Boschi ' '(Birch, Autumn)'
        'Conquista le zone Pianeggianti ': '(Plains, Dried)',
        'Conquista gli Altopiani ': '(Desert, Miras)',
        
        'Conquista il Continente del NORD ': '(Shrubble, Miras)',
        'Conquista il Continente del SUD-EST ': '(Autumn, Pine, Meadow)',
        'Conquista il Continente del SUD-OVEST ': '(Desert, Savana, Dried)',
        'Conquista il Continente del CENTRO': '(Plains, Birch) e altre 2 basi a tua scelta',

        'Conquista 3 zone a tua scelta': '',
        'Conquista ': '(Birch, Lakes)',
        "Conquista un totale di 10 basi": '',
        'Ottieni il controllo di 18 basi totali tra Neutre, Proprie e Conquistate': ''
    }

    st.title('RISIKRAFT - Randomizer')

    wdr_zone = rd.randrange(0, len(zones))
    wdr_objectives = rd.randrange(0, len(objectives))

    zones_posse = str(st.text_input('Scrivi le zone che possiedi separate da una virgola, SOLO la prima lettera MAIUSCOLA')).split(',')
    name = st.text_input('Player Name')
    bc = st.button(label='Estrai Zona')

    while bc:
        a = False
        Obj, Zone = rd.choice(list(objectives.items()))
        for z in zones_posse:
            print(z, Zone, a)
            if z in Zone:
                a = False
                print(z, ' in ', Zone)
            else:
                if a:
                    aa = True
                else:
                    aa = False
                a = True
        if aa:
            print('stop')
            break

    show_button = True

    if show_button:
        st.download_button(
            label='Scarica il tuo Obiettivo e SHHHHH!',
            data=f"""Sig. {name},
        Con questo Fax intendiamo comunicarle che gli obiettivi sono chiari:
        {Obj}{Zone}""",
        )
except Exception as e:
    print(e)
