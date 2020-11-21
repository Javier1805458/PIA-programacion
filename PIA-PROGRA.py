#------------------------------------------------------
import pandas as pd
import datetime
import sqlite3
#------------------------------------------------------
def GuardarDatos(articulo, precio, piezas, total, fecha):
    con = sqlite3.connect('VENTAS.db')
    cursor = con.cursor()
    
    cursor.execute("INSERT INTO employees(descripcion, precio,piezas,total,fecha) VALUES(?,?,?,?,?)",
    (articulo,precio,piezas,total,fecha))  
    con.commit()
    cursor.close()
    
def ConsultarDatos(Fecha):
    con = sqlite3.connect('VENTAS.db')
    cursor = con.cursor()
    
    FechaIngresada = {"Fecha":Fecha}   
    cursor.execute('SELECT * FROM employees WHERE (fecha = :Fecha)',FechaIngresada) 
    filas = cursor.fetchall()
    
    if filas:
        for fila in filas:
           
            registro = {
                'Descripcion':[fila[1]],
                'Precio': [fila[2]],
                'Piezas': [fila[3]],
                'Total': [fila[4]],
                'Fecha': [fila[5]]
                }              
            filapd = pd.DataFrame(data = registro)
            
            print('===================================================')
            print(filapd)
            print('===================================================')
    else:
        print('No existen ventas en esa fecha')
#------------------------------------------------------

BucleMenu = True
SubTotal = 0

while BucleMenu == True:
    
    print('======== MENU ========\n')

    print('1- REGISTRAR UNA VENTA')
    print('2- CONSULTAR UNA VENTA')
    print('3- SALIR')

    OpcionMenu = int(input('Elige una opción: '))
    
    print('\n======================\n')
    
    if OpcionMenu == 1:
        BucleVenta = True
        while BucleVenta == True:
            
            print('====NUEVA VENTA====')
            
            try:
                Articulo = input('¿Que articulo deseas?: ')
                
                Precio = int(input('¿Cual es el precio?: '))
                      
                Piezas = int(input('¿Cuantas piezas deseas?: '))
            except ValueError:
                print('Escribe valores validos')         
            
            if (Articulo.isspace()) or (Articulo == ""):
                print('\nDebes escribir una descripcion del articulo')
            elif (Precio < 0) or (Piezas < 0):
                
                print('\nSolo valores positivos')
            else:      
                #-------------------
                SubTotal = SubTotal + (Precio*Piezas)
                Fecha = datetime.date.today()
                #-------------------
                
                print(f'Monto a pagar: ${SubTotal}')
                
                registro = {
                        'Descripcion':[Articulo],
                        'Precio': [Precio],
                        'Piezas': [Piezas],
                        'Total': [SubTotal],
                        'Fecha de venta': [Fecha]
                        }
                
                registropd = pd.DataFrame(data = registro)
                
                print('\n1- SEGUIR COMPRANDO     2- FINALIZAR COMPRA\n')
                
                OpcionCompra = int(input('¿Que deseas hacer?: '))
                print('\n')
                
                if OpcionCompra == 1:             
                    pass
                elif OpcionCompra == 2:
                    
                    GuardarDatos(Articulo, Precio, Piezas, SubTotal, Fecha)
                    SubTotal = 0
                    BucleVenta = False
                    print(registropd)
    
    elif OpcionMenu == 2:
        
        print('\n===CONSULTA DE VENTAS===\n')
        
        Año = str(input('Año: '))
        Mes = str(input('Mes: ' ))
        Dia = str(input('Dia: ' ))
        
        FechaIngresada = (f'{Año}-{Mes}-{Dia}')        
        ConsultarDatos(FechaIngresada)
              
    elif OpcionMenu == 3:       
        BucleMenu = False
    
    else:
        input('Tienes que seleccionar una de las 3 opciones')
        pass
    
                
                
        
        