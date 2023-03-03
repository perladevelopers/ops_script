import streamlit as st
import random as rd

try:
    zones = ['Desert', 'Mesa', 'Oak', 'lakes', 'Oceans', 'Jungle', 'Birch', 'Cave', 'Big Hills', 'Plains']
    objectives = {
        'Conquista le zone Sabbiose ': '(Desert, Mesa)',
        'Conquista le zone Idriche ': '(Oceans, Lakes)',
        'Conquista le zone Rocciose ': '(Cave, Big Hills)',

        'Conquista le zone di Foresta ': '(Oak, Jungle)',
        'Conquista le zone Pianeggianti ': '(Plains, Desert)',
        'Conquista gli Altopiani ': '(Mesa, Big Hills)',

        'Conquista 3 zone a tua scelta': '',
        'Conquista ': '(Birch, Lakes)',
        "Conquista un totale di 10 basi": '',

        'Conquista le zone': '(Oak, Lakes)'
    }

    st.title('RISIKRAFT - Randomizer')

    wdr_zone = rd.randrange(0, len(zones))
    wdr_objectives = rd.randrange(0, len(objectives))

    n_player = st.slider(label='Numero di Giocatori', min_value=2, max_value=10)
    zones_posse = str(st.text_input('Scrivi le zone che possiedi separate da una virgola')).split(',')
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
