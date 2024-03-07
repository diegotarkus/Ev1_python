import os
from re import X
import numpy as np
nombres=list(); rut=list(); telefono=list(); banco=list(); asiento=list()
pasajeros=[nombres, rut, telefono, banco, asiento]
n=42

arreglo = np.arange(1, n+1, 1)
matriz = np.reshape(arreglo, (7, 6))

def menu():
    os.system('cls')
    print("1. Ver asientos disponibles")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos del pasajero")
    print("5. Salir")
    op=input("Ingrese opción: ")
    if op=='1':
        print(matriz)
        input("Presione una tecla para continuar...")
        return(menu())
    if op=='2':
        vender()
        input("Presione una tecla para continuar...")
        return(menu())
    if op=='3':
        anular()
        input("Presione una tecla para continuar...")
        return(menu())
    if op=='4':
        modificar()
        input("Presione una tecla para continuar...")
        return(menu())
    if op=='5':
        salir()

    

def vender():
    print(matriz)
    print("Valor normal: $ 78.900")
    print("Valor VIP: $ 240.000")
    while True:
        xasiento=int(input("Ingrese número de asiento: "))
        for i in range (7):
            for j in range(6):
                if(matriz[i, j]==xasiento):
                    matriz[i,j] = 0
        if xasiento <= 30:
            precio_final = "78900"
        else:
            precio_final = "240000"    
        xnombre = input("Ingrese nombre de pasajero: ")
        xrut = input ("Ingrese rut del pasajero: ")
        xtelefono = input("Ingrese telefono: ")
        xbanco = input("Ingrese banco del pasajero: ")
        if xbanco == "Duoc":
            print("¡Tienes un descuento!")
            precio_final=(float(precio_final) * 0.85)
        else:
            precio_final = precio_final 
        nombres.append(xnombre), rut.append(xrut), telefono.append(xtelefono), banco.append(xbanco), asiento.append(xasiento)

        print("Nombre: ", xnombre)
        print("RUT: ", xrut)
        print("Teléfono: ", xtelefono)
        print("Banco: ", xbanco)    
        print("ASIENTO: ", xasiento)
        print("Valor total: ", precio_final)
        
        break  

def anular():
    xasiento=int(input("Ingrese asiento: "))
    for i in range (7):
        for j in range(6):
            if(matriz[i, j]==0):
                matriz[i,j] = xasiento
    xrut=input("Ingrese rut: ")
    k = rut.index(xrut)
    l = len(rut)
    for k in range(l):
        pasajeros[k].pop(k)
    
def modificar():
    xrut=input("Ingrese rut: ")
    i = rut.index(xrut)
    print(f'{pasajeros[0][i]} || {pasajeros[1][i]} || {pasajeros[2][i]} || {pasajeros[3][i]}')
    print('¿Qué desea modificar?: ')
    print("1. Nombre")
    print("2. Teléfono")
    op=input("Ingrese opción: ")

    if op=='1':
        xnombre=input("Ingrese nuevo nombre: ")
        pasajeros[0][i] = xnombre
        nombres.append(xnombre)
        input("Los datos se han cambiado satisfactoriamente...")
    
    if op == '2':
        xtelefono=input("Ingrese nuevo teléfono: ")
        pasajeros[2][i] = xtelefono
        telefono.append(xtelefono)
        input("Los datos se han cambiado satisfactoriamente...")
    

def salir():
    print("Gracias por ocupar este software!")
    input("Diego Galarce 2022")
    
menu()    