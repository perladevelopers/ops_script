import re
import streamlit as st

st.header('Perla Enviroment TERMINAL')

Blue = ''
Red = ''
Reset = ''

printi = print
print = st.write
input = st.text_input



def helper():
    print("""COMMANDS:
- print(argomenti...)
- plotma(stock)(timeframe)(lunghezza ma1)(lunghezza ma2)
- open(URL)
- easytk(Take Profit)(Stop Loss)(Investimento)(Leva)
- spread(Valore Asset)(Spread Asset)
- open(easytk) >>> apre Easy Task
- open(stcalc) >>> apre Strat Calculator
- val(asset) >>> scrive il valore di un asset. se è una valuta indicherà ask e bid
- info(asset) >>> scrive tutte le info di un assetù
- botto2(args0, 1, 2, 3, 4, 5, 6, 7) compila una au91 = trade_segnal(con gli argomenti)
- mean(args)(args2)...)(args 2000) >>> ritorna la media
- py(  oppure python(  >>>> esegue un codice Python non serve chiudere la parentesi del py() ma se si vuole si può solo con un trattino = py(codice python -) ; più veloce py(codice python
\n 
\n------------------------------------------------------------------------------------
******************Formattazione Rapide******************
- media( 3 4 5     >>> ritorna la media. da notare la differenza da mean(). si scrive media(spazio arg1 spazio arg2... senza chiudere la parentesi.
- Proporzione ----> a:b=x:c >>>> ritorna il valore di 'x' qualsiasi sia la sua posizione. con o senza spazi tra valori e operatori\n
Se si scrive una proporzione senza la x ritornerà True o False 
\n 
\n 
\n------------------------------------------------------------------------------------

CALCULATOR COMMANDS:\n
modo di scrittura:\n
argomento1 operatore argomento2 es(3 + 4); non ci sono parentesi, ma ci sono gli spazi. obbligo di 2 argomenti\n
Operatori:\n
********Se si usa un espressione con più di due argomenti. gli operatori speciali non funzioneranno********
- '+' (somma)
- '-' (sottrazione)
- '*' (Moltiplicazione)
- '/' o ':' (divisione)
- '**' (elevazione a potenza)
- 'sp' (spread tra due valori in percentuale)
- 'sp+' (spread dato VALORE e SPREAD in punti)
- '%' (calcola il arg2% del arg2)
- '%%' (calcola arg1 in % relativa ad arg2)
""")


def arg_sep(args):
    for i, arg in enumerate(args):
        args[i] = arg.replace('(', '').replace(')', '')
        # args[i] = arg.replace(')', '')
    return args


def Easy_Task(t, s, i, leva):
    l = (t - 0.02) * leva
    m = (s + 0.02) * leva

    x = l * i / 100
    y = m * i / 100

    print("il take profit è di", x, "$")
    print("il Stop Loss è di", y, "$")


def Spread_Calculator(va, spa):
    valore_asset = va
    spread_asset = spa
    media_valore_asset = (valore_asset + valore_asset + spread_asset) / 2
    spread = spread_asset * 100 / media_valore_asset
    print(spread)


def proportion(args):
    ind = args.index('x')
    if ind == 1:
        print(float((float(args[0]) * float(args[3])) / float(args[2])))
    elif ind == 0:
        print(float((float(args[1]) * float(args[2])) / float(args[3])))
    elif ind == 2:
        print(float((float(args[0]) * float(args[3])) / float(args[1])))
    elif ind == 3:
        print(float(args[1]) * float(args[2]) / float(args[0]))


i = 0
calcmod = st.checkbox('Calculator Mode')
try:
    if i == 0:
        print('Perla Enviroment OS Terminal v2.1')
        print('Scrivi help (senza calc. mode) per la lista comandi')
    text = str(input(f'PerlaOS  '))
    text_split = text.split(' ')
    text_splitp = text.split('(')
    text_prop_split = text.replace(' ', '').replace('=', ':').split(':')
    #print(f'text_split = {text_split}, text_prop_split = {text_prop_split}')

    if calcmod:
        if len(text_split) < 4:
            args = text_split[0], text_split[2]
            operand = text_split[1]
            st.subheader('Calculator Mode')
            if args[0] == 'calc-o':
                print(f'{Blue}Calculator Mod OFF')
                calcmod = False
            if args[0] == 'help':
                helper()
                print(f'{Blue}Calculator Mod OFF')
                calcmod = False
            args = float(args[0]), float(args[1])
            if operand == '+':
                print(args[0] + args[1])
            elif operand == '-':
                print(args[0] - args[1])
            elif operand == '*':
                print(args[0] * args[1])
            elif operand == ':' or operand == '/':
                print(args[0] / args[1])
            elif operand == '**':
                print(args[0] ** args[1])
            elif operand == 'sp':
                med = (args[0] + args[1]) / 2
                dif = abs(args[0] - args[1])
                perc = (dif * 100) / med
                print(f'{perc}%')
            elif operand == '%%':
                res = (float(args[0]) * 100) / float(args[1])
                print(res)

            elif operand == '%':
                res = (float(args[0]) * float(args[1])) / 100
                print(res)

            elif operand == 'sp+':
                Spread_Calculator(args[0], args[1])
        elif len(text_split) > 4:
            print(eval(text))

    else:
        args = re.findall(r'\(.*?\)', text)
        args = arg_sep(args)
        argss = text_split[1::]
        base = text_splitp[0]

        if base == 'print':
            for arg in args:
                print(arg + ' ', end='')
            print('\n')
        elif base == 'spread':
            Spread_Calculator(float(args[0]), float(args[1]))
        elif base == 'easytk':
            Easy_Task(args[0], args[1], args[2], args[3])
        elif base == 'open':
            import webbrowser

            if 'easytk' in args:
                webbrowser.open('https://t3rr1x-perla-easytask-cvihg2.streamlit.app/')  # Go to example.com
            elif 'stcalc' in args:
                webbrowser.open('https://t3rr1x-perla-stratcalculator-li0z8b.streamlit.app/')  # Go to example.com
            else:
                webbrowser.open(args[0])  # Go to example.com
        elif "%%" in text_split:
            res = (float(args[0]) * 100) / float(args[1])
            print(res)
        elif "%" in text_split:
            res = (float(args[0]) * float(args[1])) / 100
            print(res)

        elif base == 'mean':
            argsint = []
            for arg in args:
                argsint.append(float(arg))
            print(sum(argsint)/len(args))

        elif base == 'calc-s':
            if not calcmod:
                calcmod = True
                print(f'{Blue}Calculator Mod Insert')

        elif base == 'calc-o':
            calcmod = False
            print(f'{Blue}Calculator Mod Disabled')

        elif base == 'help':
            helper()

        elif base == 'val':
            import yfinance as yf

            stock = yf.Ticker(args[0])
            try:
                data1 = stock.info
                print(data1['currentPrice'])
            except:
                data1 = stock.info
                print('ask and bid = ', data1['ask'], data1['bid'])
        elif base == 'info':
            import yfinance as yf

            stock = yf.Ticker(args[0])
            data1 = stock.info
            print(data1)

        elif base == 'botto2':
            print(f'au91 = trade_segnal({args[0]}, {args[1]}, {args[2]} {args[3]}, {args[4]}, 0, t, s, p, {args[5]}, {args[6]})')

        elif base == 'py' or base == 'python':
            command = (text.replace('py(', '').replace('-)', ''))
            print(exec(command))

        # Formattazioni Speciali

        elif base == 'media':
            argsint = []
            for arg in argss:
                argsint.append(float(arg))
            print(sum(argsint)/len(argss))

        elif 'x' in text_prop_split:
            proportion(text_prop_split)

        elif len(text_prop_split) == 4:
            try:
                a = (float(text_prop_split[0]) * float(text_prop_split[3])) == (float(text_prop_split[1]) * float(text_prop_split[2]))
                print(a)
            except Exception as e:
                print(e)



except Exception as e:
    print(f'Comando non riconosciuto,', e)
    pass
