#conversion de cntenedores 
#conversion de cadenas 
'''print('\x1Bc')
cadena='aeiou'
cadenalista=list(cadena)
print(cadenalista)
cadenalista=cadena.split()
print(cadenalista)'''


#cadena a tuplas función--tuple 
'''cadena='aeiou'
cadenatupla=tuple(cadena)
print(cadenatupla)'''

#cadena conjuntos-- set
'''cadena='aeiiiiuuuuuuuuuuuuuuu'
cadenaconjunto=set(cadena)
print(cadenaconjunto)'''''

#conversion de listas
#listas a cadenas--- join
'''lista=['a', 'e', 'i', 'o', 'u', 'n']
listacadena=''.join(lista)
print(listacadena)'''

#convertir lsitas a tuplas
'''lista=['a','e','i','o','u']
listatupla=tuple(lista)
print(listatupla)'''

#convertir lista a conjuntos ----set
'''listas=['a','e','i','o','u']
listaconjunto=set(listas)
print(listaconjunto)'''

#conversion de tuplas
#tuplas a cadenas --- join
'''tupla=('a', 'e', 'i', 'o', 'u')
tuplacadena=''.join(tupla)'''

#tupla a lista--- list

'''tupla=('a', 'e', 'i', 'o', 'u')
tuplalista=list(tupla)
print(tuplalista)'''

#tuplas a conjutos ---set
'''tupla=('a', 'e', 'i', 'o', 'u','a', 'e', 'i', 'o', 'u')
tuplaconjunto=set(tupla)
print(tuplaconjunto)'''

#conversion de conjutos
#conjuntos a cadenas ---join
'''conjunto={'a', 'e', 'i', 'o',}
conjuntocadena=''.join(conjunto)
print(conjuntocadena)'''

#conjunto  tuplas--- tuple
'''conjunto={'a', 'e', 'i', 'o', 'u','a', 'e', 'i', 'o', 'u'}
conjuntotupla=tuple(conjunto)
print(conjuntotupla)'''

#conjunto a lista ---list
'''conjunto={'a', 'e', 'i', 'o',}
conjutolista=list(conjunto)
print(conjutolista)'''


#conversion a diccionarios
#lista a diccionarios
#zip(rango,estructuras de datos--lista)
'''lista=[1,2,3,4]
rango=range(len(lista))

diccionariolista=dict(zip(rango,lista))
print(diccionariolista)'''

#cadena a diccionario

'''cadena='hola'
diccionariocadena=dict(zip(range(len(cadena)),cadena))
print(diccionariocadena)'''

#tula a diccionario
'''tupla=('a', 'e', 'i', 'o', 'u')
diccionariotupla=dict(zip(range(len(tupla)),tupla))
print(diccionariotupla)'''

#conjunto a diccionario
'''conjunto={'a', 'e', 'i', 'o',}
diccionarioconjunto=dict(zip(range(len(conjunto)),conjunto))
print(diccionarioconjunto)'''

#conversion a diccionarios
'''diccionario={0:'ky',1:'lopez'} 
listakeys= list(diccionario)
listavalues=list(diccionario.values())
listaitems=list(diccionario.items())
print(listakeys)
print(listaitems)
print(listaitems)'''

#diccionario a cadena
'''diccionario={0:'ky',1:'lopez'} 
cadenakeys= str(diccionario)
cadenavalues=list(diccionario.values())
cadenaitems=list(diccionario.items())
print(listakeys)
print(listaitems)
print(listaitems)'''

#diccionario a tuplas
'''diccionario={0:'ky',1:'lopez'} 
tuplakeys= tuple(diccionario)
tuplavalues=tuple(diccionario.values())
tuplaitems=tuple(diccionario.items())
print(tuplakeys)
print(tuplaitems)
print(tuplaitems)'''

#diccionario a conjunto
'''diccionario={0:'ky',1:'lopez'} 
conjuntokeys= set(diccionario)
conjuntovalues=set(diccionario.values())
conjuntoitems=set(diccionario.items())
print(conjuntokeys)
print(conjuntoitems)
print(conjuntoitems)'''

