def programa_peso():
    peso=int(input("inrese su peso en (kg)"))
    estatura=float(input("ingrese su estatura en (metros)"))
    rta= round(peso/estatura**2,2)
    respuesta="Tu índice de masa corporal es {}donde <imc> es el índice de masa corporal calculado redondeado con dos decimales{}"
    return respuesta.format(rta,rta)
    
print(programa_peso())  
    

#forma de solucion de la paigna que investigue
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))

   
     