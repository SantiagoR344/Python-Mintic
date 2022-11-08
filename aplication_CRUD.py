#Paso No. 3
tareas={
        '01':{
            'descripcion': 'Ir a mercar',
            'estado':'pendiente',
            'tiempo':60
        },
        '02':{
            'descripcion': 'Estudiar Programación',
            'estado':'pendiente',
            'tiempo':180
        },
        '03':{
            'descripcion': 'Hacer Ejercicio',
            'estado':'pendiente',
            'tiempo':50
        }
}

#Funciones
def adicionarTarea(tareas,identificador,nuevaTarea):
    tareas[identificador]=nuevaTarea
    return tareas

def consultarTareas(tareas):
    for identificador, tarea in tareas.items():
        print(identificador,'--',end='')#end='', eliminar el salto de línea al final
        for atributo in tarea.values():
            print(atributo,'--',end='')
        print()

def buscarIdentificador(identificador, tareas):
    #crear un conjunto con mis identificadores - set ....
    conjuntoIdentificadores=set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        return True
    else:
        return False

def actualizarTarea(tareas, identificador):
    nuevaDescripcion=str(input('Nueva descripción: '))
    nuevoEstado=str(input('Nuevo Estado: '))
    nuevoTiempo=int(input('Nuevo tiempo: '))

    tareas[identificador]['descripcion']=nuevaDescripcion
    tareas[identificador]['estado']=nuevoEstado
    tareas[identificador]['tiempo']=nuevoTiempo

def eliminarTarea(tareas,identificador):
    conjuntoIdentificadores=set(tareas.keys())
    if identificador in conjuntoIdentificadores:
        #pop... elimar un elemento de mi diccionario
        tareas.pop(identificador)
        print(f'La tarea con identificador {identificador} ha sido eliminado')
    else:
        print('No existe una tarea con ese identificador')
#Fin de funciones

#Paso 1. Hacer el menú de opciones

menuOpciones=True

while menuOpciones:
    print('---------------Aplicación CRUD----------\n'
           '1. Adicionar Tarea  -   C\n'
           '2. Consultar Tareas -   R\n'
           '3. Actualizar Tarea -   U\n'
           '4. Eliminar Tarea   -   D\n'
           '5. Salir')

    opcion=input('Digite la opción: ')

    #Paso 2. Hacer funcional a todas las opciones
    if opcion=='1':
        print('----------Adicionar Tarea-----------')
        #Paso 3. Es hacer adicionar Tarea
        #Declarado mi diccionario tarea (inicio del módulo)
        #Recibir los datos por teclado
        identificador=str(input('Ingrese el identificador de la tarea: '))
        descripcion=str(input('Ingrese la descripción de la tarea: '))
        estado=str(input('Ingrese el estado de la Tarea: '))
        tiempo=int(input('Ingrese el tiempo de realización: '))
        nuevaTarea={
                    'descripcion':descripcion,
                    'estado':estado,
                    'tiempo':tiempo
        }
        #Hacer la función adicionarTarea(tareas, identificador,nuevaTarea)(Incio...)
        tareas=adicionarTarea(tareas,identificador,nuevaTarea)
        #print(tareas)
    elif opcion=='2':
        print('----------Consultar Tareas-----------')
        #Paso No. 4 
        #Hacer la función consultarTareas
        #llamar a la función consultarTareas(tareas)
        consultarTareas(tareas)
    
    elif opcion=='3':
        print('----------Actualizar Tarea-----------')
        #Paso No.5
        #Hacer la función actualizarTarea
        identificador=str(input('Digite el identificador de la tarea a actualizar: '))
        #Buscar si el identificador existe buscarIdentificador(identificador,tareas)
        if buscarIdentificador(identificador, tareas):
            actualizarTarea(tareas, identificador)
        else:
            print('No se ha encontrado una tarea con ese identificador...')
    elif opcion=='4':
        print('----------Eliminar Tarea-----------')
        #Paso No. 6
        identificador=str(input('Digite el identificador de la tarea a eliminar: '))
        eliminarTarea(tareas,identificador)
    
    elif opcion=='5':
        print('Ha salido correctamente del sistema...')
        menuOpciones=False
    
    else:
        print('No ha elegido una opción válida')
    # IdProducto=[2010,2010,3578,9251]
    # dProducto=
    # pnProducto=
    # cvProducto=
    # sProducto=
    # nComprador=
    # cComprador=
    # fVenta=