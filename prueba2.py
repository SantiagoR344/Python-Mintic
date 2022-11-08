
def cliente(informacion:dict):
    if informacion['edad'] >18:
        atraccion='X-Treme'
        apto=True
        if informacion['primer_ingreso']:
            total_boleta=20000*(1-0.05)
        else:
            total_boleta=20000
    elif informacion['edad'] >=15 and informacion['edad'] <= 18: 
        atraccion='Carros chocones'
        apto=True
        if informacion['primer_ingreso']:
            total_boleta=5000*(1-0.07)
        else:
            total_boleta=5000
    elif informacion['edad'] >=7 and informacion['edad'] <15:
        atraccion='Sillas voladoras'
        apto=True
        if informacion['primer_ingreso']:
            total_boleta=10000*(1-0.05)
        else:
            total_boleta=10000
    if informacion['edad'] <7:
        atraccion='N/A'
        apto=False
        total_boleta='N/A'
    respuesta={'nombre':informacion['nombre'],'edad':informacion['edad'],'atraccion':atraccion,'apto':apto,'primer_ingreso':informacion['primer_ingreso'],'total_boleta':total_boleta}            
    return respuesta
 
informacion={}
informacion['id_cliente']=int(1)
informacion['nombre']=str('Johana Fernandez')
informacion['edad']=int(20)
informacion['primer_ingreso']=bool(1)


print(cliente(informacion))

    
    
        
