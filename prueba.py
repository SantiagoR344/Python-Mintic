def CDT(usuario:str,capital:int,tiempo:int):
    """CDT
    :Parámetros:  usuario (str):alfanumérico
    que identifica el usuario  capital(int):
    Monto a ingresar   tiempo(int):Tiempo del
    CDT"""
    if tiempo>(2):#tiempo es mayor que dos 
            valor_intereses=(capital*0.03*tiempo)/12
            valor_total=(valor_intereses+capital)
            respuesta="Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}"
            return respuesta.format(usuario,capital,tiempo,valor_total)
    else:#cuando el capital se saca antes de tiempo
        valor_perder=(capital*0.02)
        valor_total=(capital-valor_perder)
        respuesta="Para el usuario {} La cantidad de dinero a recibir, según el monto inicial {} para un tiempo de {} meses es: {}"
        return respuesta.format(usuario,capital,tiempo,valor_total)

print(CDT("user1",1000000,3))
print(CDT("ABBCD",650000,2))