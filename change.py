def change():
    expense = 23.75
    money = 100
    vuelto= (money - expense)
    pesos=int(vuelto)
    centavos=int((vuelto-pesos)*100)
    print=(f"ingreso gastos:\n{expense}")(
    print(f"dinero recibido\n{money}\n")
    print("vuelto\n")
    print(f"pesos:\n{centavos}")
    print(f"centavos:\n{centavos}")
change()
