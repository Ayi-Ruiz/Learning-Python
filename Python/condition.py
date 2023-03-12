#if and elif
sueldo_chingon = 50000
gastos_de_casa = 40000

if sueldo_chingon > 10000:
    if sueldo_chingon - gastos_de_casa < 0:
        print('estas en deficit')
    elif gastos_de_casa - sueldo_chingon > 20000:
        print('estas bien pa')
    elif gastos_de_casa - sueldo_chingon > 40000:
        print('fuaa la re vivis scooby gastas mucho')
else:
    print('sos pobre')              