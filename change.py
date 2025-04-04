def change():
    expense = 23.75
    money = 100
    
    cambio= money-expense 
    pesos= int(cambio)
    centavos= int((cambio-pesos)*100)

   print("ingresar gasto:")
   print(expense)
   print("dinero recibido")
   print(money)
   print()
   print("vuelto")
   print()
   print("pesos:")
   print(pesos)
   print("centavos:")
   print(centavos)

change()
