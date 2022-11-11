def hora_ampm(horas,minutos):
  nova_hora = hora if hora <=12 else hora-12
  A_ou_P = "AM" if hora <12 else "PM"
  return str( nova_hora)+":"+str(minutos)+A_ou_P
  
while True:
   hora = int(input("Informe a hora, e se quiser sair digite 0: "))
   if hora ==0:
    break
   minutos = int(input("Informe os minutos"))
   print(hora_ampm(hora,minutos))
