import os

##################Variables globales: estas son las importantes para entrar a la interfaz.
######################
user_name=str("admin")
password=str("admin")
#Información que da el proyecto de github
"""
This is the LifeStore_SalesList data:
lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""
from life_store import lifestore_products
from life_store import lifestore_searches
from life_store import lifestore_sales



def productos_mayores_ventas_busquedas():
  #######10 productos con mayores ventas
  #lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
  j=0
  h=0
  z=0
  i=0
  sold_product=[]
  copy_sold_product=[]
  search_product=[]
  copy_search_product=[]
  id_product=[]

  #acomodar las 284 ventas con cada id product para saber que producto se vendio más, se tman en cuenta solo los productos que no se regresaron.
  sold_product=busqueda_id_ventas(lifestore_sales)
  copy_sold_product=busqueda_id_ventas(lifestore_sales)
  
  #print(sold_product)
  sold_product.sort()
  sold_product.reverse()
  #print(sold_product)

  #Acomodo mis id_product como viene la lista en orden para despues imprimirlos en pantalla 

  for k in range(0, (len(lifestore_products))):
  
    id_prod = copy_sold_product.index(sold_product[k])
    copy_sold_product[id_prod] = 99
    id_product.append(id_prod + 1)
   

  #print(id_product)

  #Imprime mis datos :
  print("\nLista de los 10 producto más vendidos.\n")
  print( "|No°|id_product|nombre_producto recortado |ventas|Stock|Costo|")
  i=0
  k=0
  for i in range (10):
    print("|" +str(i+1) +"  |" +str(id_product[i])+"    |"+ str(lifestore_products[id_product[i]-1][1][0:30])+" |"+str(sold_product[i])+"     |"+str(lifestore_products[id_product[i]-1][4])+" |"+str(lifestore_products[id_product[i]-1][2])+" |")
  #print("\n")
  #Enter de estetica.
  enter=input("Presiona enter para continuar: ")


  #50 productos con mayores busquedas
  search_product=busqueda_id(lifestore_searches)
  copy_search_product=busqueda_id(lifestore_searches)
  search_product.sort()
  search_product.reverse()
  
  #Saco id en lista ya ordenada de mayor a menor
  id_product1=[]
  for k in range(0, (len(lifestore_products))):
  
    id_prod = copy_search_product.index(search_product[k])
    copy_search_product[id_prod] = 99
    id_product1.append(id_prod + 1)
   

  #print(id_product1)
  #print(search_product)

  #Imprime mis datos :
  print("\nLista de los 20 producto más buscados.\n")
  print( "|No°|id_product|nombre_producto recortado |busquedas|Stock|costo|")
  i=0
  k=0
  for i in range (20):
    print("|" +str(i+1) +"  |" +str(id_product1[i])+"     |"+ str(lifestore_products[id_product1[i]-1][1][0:30])+" |"+str(search_product[i])+"     |"+str(lifestore_products[id_product[i]-1][4])+" |"+str(lifestore_products[id_product[i]-1][2])+"|")
  print("\n")

def productos_menores_ventas_busquedas():
  ########20 Peores vendidos##################
  sold_bad_product=[]
  copy_sold_bad_product=[]
  search_bad_product=[]
  copy_search_bad_product=[]
  
  #acomodar las 284 ventas con cada id product para saber que producto se vendio más y sin contar las ventas que fueron regrresadas (refund)
  sold_bad_product=busqueda_id_ventas(lifestore_sales)
  copy_sold_bad_product=busqueda_id_ventas(lifestore_sales)
  sold_bad_product.sort()

  #print(sold_bad_product)
  #print(copy_sold_bad_product)
  #enter=input("press")
  
  #Acomodo mis id_product como viene la lista en orden de mayor a menor para despues imprimirlos en pantalla 
  id_product3=[]
  for k in range(0, (len(lifestore_products))):
  
    id_prod = copy_sold_bad_product.index(sold_bad_product[k])
    copy_sold_bad_product[id_prod] = 9999
    id_product3.append(id_prod + 1)
   

  #print(id_product3)

  #Imprime mis datos :
  print("\nLista de los productos por categoria procesadores menos vendidos entre los 50 productos menos vendidos.\n")
  print( "|No°|id_product|nombre_producto recortado |no° de ventas|stock|costo|")
  producto_por_categoria(id_product3,'procesadores',sold_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria tarjetas de video menos vendidos entre los 50 productos menos vendidos.\n")
  print( "|No°|id_product|nombre_producto recortado |no° de ventas|stock|costo|")
  producto_por_categoria(id_product3,'tarjetas de video',sold_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\n\nLista de los productos por categoria tarjetas madre menos vendidos entre los 50 productos menos vendidos.\n")
  print( "|No°|id_product|nombre_producto recortado |no° de ventas|stock|costo|")
  producto_por_categoria(id_product3,'tarjetas madre',sold_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\n\nLista de los productos por categoria discos duros menos vendidos entre los 50 productos menos vendidos.\n")
  print( "|No°|id_product|nombre_producto recortado |no° de ventas|stock|costo|")
  producto_por_categoria(id_product3,'discos duros',sold_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\n\nLista de los productos por categoria memorias usb menos vendidos entre los 50 productos menos vendidos.\n")
  print( "|No°|id_product|nombre_producto recortado |no° de ventas|stock|costo|")
  producto_por_categoria(id_product3,'memorias usb',sold_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\n\nLista de los productos por categoria bocinas vendidos entre los 50 productos menos vendidos.\n")
  print( "|No°|id_product|nombre_producto recortado |no° de ventas|stock|costo|")
  producto_por_categoria(id_product3,'bocinas',sold_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria audifonos menos vendidos entre los 50 productos menos vendidos.\n")
  print( "|No°|id_product|nombre_producto recortado |no° de ventas|stock|costo|")
  producto_por_categoria(id_product3,'audifonos',sold_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria pantallas menos vendidos entre los 50 productos menos vendidos.\n")
  print( "|No°|id_product|nombre_producto recortado |no° de ventas|stock|costo|")
  producto_por_categoria(id_product3,'pantallas',sold_bad_product,50)
  

  #Enter de estetica.
  enter=input("Presiona enter para continuar: ")

  #100 productos con menores busquedas
  search_bad_product=busqueda_id(lifestore_searches)
  #print(search_bad_product)
  copy_search_bad_product=busqueda_id(lifestore_searches)
  #print("aqui")
  search_bad_product.sort()
  #print(search_bad_product)
  #print(copy_search_bad_product)
  id_product4=[]

  for k in range(0, (len(lifestore_products))):
  
    id_prod = copy_search_bad_product.index(search_bad_product[k])
    copy_search_bad_product[id_prod] = 9999
    id_product4.append(id_prod + 1)
  
  #print(id_product4)
  #Imprime mis datos :
  print("\nLista de los productos por categoria procesadores menos buscados entre los 50 productos menos buscados.\n")
  print( "|No°|id_product|nombre_producto recortado |busquedas|stock|costo|")
  producto_por_categoria(id_product3,'procesadores',search_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria tarjetas de video menos buscados entre los 50 productos menos buscados.\n")
  print( "|No°|id_product|nombre_producto recortado |busquedas|stock|costo|")
  producto_por_categoria(id_product4,'tarjetas de video',search_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria tarjetas madre menos buscados entre los 50 productos menos buscados.\n")
  print( "|No°|id_product|nombre_producto recortado |busquedas|stock|costo|")
  producto_por_categoria(id_product4,'tarjetas madre',search_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria discos duros menos buscados entre los 50 productos menos buscados.\n")
  print( "|No°|id_product|nombre_producto recortado |busquedas|stock|costo|")
  producto_por_categoria(id_product4,'discos duros',search_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria memorias usb menos buscados entre los 50 productos menos buscados.\n")
  print( "|No°|id_product|nombre_producto recortado |busquedas|stock|costo|")
  producto_por_categoria(id_product4,'memorias usb',search_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria bocinas menos buscados entre los 50 productos menos buscados.\n")
  print( "|No°|id_product|nombre_producto recortado |busquedas|stock|costo|")
  producto_por_categoria(id_product4,'bocinas',search_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria audifonos menos buscados entre los 50 productos menos buscados.\n")
  print( "|No°|id_product|nombre_producto recortado |busquedas|stock|costo|")
  producto_por_categoria(id_product4,'audifonos',search_bad_product,50)
  enter=input("Presiona enter para continuar: ")

  print("\nLista de los productos por categoria pantallas menos buscados entre los 50 productos menos buscados.\n")
  print( "|No°|id_product|nombre_producto recortado |busquedas|stock|costo|")
  producto_por_categoria(id_product4,'pantallas',search_bad_product,50)
  enter=input("Presiona enter para continuar: ")
  

def busqueda_id(lo_que_busco):
  h=0
  i=0
  j=0
  lista_id=[]
  for j in range(1,(len(lifestore_products)+1)):
    for i in range (len(lo_que_busco)):
      if lo_que_busco[i][1]==j:
        h+=1
      #print("id product: "+ str(j)+" " +str(h))
    lista_id.append(h)
    h=0
  return(lista_id)

def busqueda_id_ventas(lo_que_busco):
  h=0
  i=0
  j=0
  lista_id=[]
  for j in range(1,(len(lifestore_products)+1)):
    for i in range (len(lo_que_busco)):
      if lo_que_busco[i][1]==j and lo_que_busco[i][4]==0:
        h+=1
      #print("id product: "+ str(j)+" " +str(h))
    lista_id.append(h)
    h=0
  return(lista_id)

def producto_por_categoria(id_product,category,lista,rango):
  i=0
  k=0
  h=1
  for i in range (rango):
    #print(lifestore_products[id_product[i]-1][0])
    #print()

    if (lifestore_products[id_product[i]-1][3]==str(category)):
      print("|" +str(i+1) +"  |" +str(id_product[i])+"     |"+ str(lifestore_products[id_product[i]-1][1][0:30])+" |"+str(lista[i])+"           |"+ str(lifestore_products[id_product[i]-1][4])+"  |"+ str(lifestore_products[id_product[i]-1][2])+"|")
      h+=1
  print("\n")

  

def lista_20():
  #########Lista de 20 productos con los mejores puntajes:
  #Variables a usar en funcion
  i=0
  best_scored_product = []
  best_product = []
  copy_best_product = []
  id_product = []
  
  #Saco solo los prodcutos vendidos con mayor calificación:
  for i in range(len(lifestore_sales)):
     if lifestore_sales[i][2] == 5 or lifestore_sales[i][2] == 4 and lifestore_sales[i][4]==0:
       best_scored_product.append(lifestore_sales[i])
  #print("aqui")
  #print(len(best_scored_product))
  
  #Solo es para imprimir mi lista y revisar
  j=0
  #for j in range (len(best_scored_product)):
    #  print(best_scored_product[j])
    #  print()
  
  #saco cuanatas veces cada producto tuvo calificacion de 5
  k = 0
  l = 0
  z = 0
  for k in range(1, (len(lifestore_products) + 1)): 
    for l in range(len(best_scored_product)): 
      if best_scored_product[l][1] == k:
        z += 1
        #print("id product: "+ str(k)+" " +str(z))
    best_product.append(z)
    copy_best_product.append(z)

    z = 0
  best_product.sort()
  best_product.reverse()
  #print(best_product)
  #print(copy_best_product)
  
  #creación de lista por medio de id_product y los mejores calicacion con 5 ordenados de mayor a menor 
  k = 0
  for k in range(0, (len(lifestore_products))):
    #print(copy_best_product[k])
    #print(best_product[k])
    id_prod = copy_best_product.index(best_product[k])
    copy_best_product[id_prod] = 99
    id_product.append(id_prod + 1)
    #print(id_prod)
    #print(copy_best_product)
    #print(id_product)
    #print(best_product)
    #Lista 1 final
  i = 0
  print("\nLista de los 20 productos con mayor valoración de 4 y 5:\n")
  print("|No°| id    | Nombre recortado del producto | Numero de  |categoria|")
  print("|   |product|                               |valoraciones|         |")
  print("|   |       |                               |recibidas   |         |")
  for i in range(0, 20):
    print("| " + str(i + 1) + " |  " + str(id_product[i]) + " | " +str(lifestore_products[id_product[i]-1][1][0:30]) + " | " +str(best_product[i]) + "         |"+str(lifestore_products[id_product[i]-1][3])+"|")


  #########Lista de 12 productos con los menores puntajes de valoración:
  i = 0
  worse_scored_product = []
  worse_product = []
  copy_worse_product = []
  id_product1 = []
  for i in range(len(lifestore_sales)):
    if lifestore_sales[i][2] == 1 or lifestore_sales[i][2] == 2 or lifestore_sales[i][2] == 3:
      worse_scored_product.append(lifestore_sales[i])
  #Solo es para imprimir mi lista y revisar, que no haya algo mal
  #j=0
  #print("aqui")
  #for j in range (len(worse_scored_product)):
  #  print(worse_scored_product[j])
  #  print()
  #saco cuantas veces cada producto tuvo calificacion de 1,2,3
  k = 0
  l = 0
  z = 0
  for k in range(1, (len(lifestore_products) + 1)):
    for l in range(len(worse_scored_product)):
      if worse_scored_product[l][1] == k:
        z += 1
    #print("id product: "+ str(k)+" " +str(z))
    worse_product.append(z)
    copy_worse_product.append(z)

    z = 0
  worse_product.sort()
  worse_product.reverse()
  #print(worse_product)
  #print(copy_worse_product)
  k = 0
  for k in range(0, (len(lifestore_products))):
    #print(copy_best_product[k])
    #print(best_product[k])
    id_prod1 = copy_worse_product.index(worse_product[k])
    copy_worse_product[id_prod1] = 99
    id_product1.append(id_prod1 + 1)
    #print(id_prod)
  #print(copy_worse_product)
  #print(id_product1)
  #print(worse_product)
  #Lista 2 final
  i = 0
  print("\nLista de los 12 productos con menor valoración de 1 a 3:\n")
  print("|No°| id    | Nombre recortado del producto | Numero de  |categoria|")
  print("|   |product|                               |valoraciones|         |")  
  print("|   |       |                               |recibidas   |         |")
  for i in range(0, 12):
    print("| " + str(i + 1) + "|  " + str(id_product1[i]) + "  | " +str(lifestore_products[id_product1[i]-1][1][0:30]) + " | " +str(worse_product[i]) + "         |"+str(lifestore_products[id_product1[i]-1][3])+"|")

def ventas_prom_mensuales_y_anual():
  #####VENTAS MENSUALES.#######
  #Variables anuales de cada año
  total_2020_year=[]
  total_2019_year=[]
  total_2002_year=[]

  #Variables de todos los meses de 2020
  total_202001=[]
  total_202002=[]
  total_202003=[]
  total_202004=[]
  total_202005=[]
  total_202006=[]
  total_202007=[]
  total_202008=[]
  total_202009=[]
  total_202010=[]
  total_202011=[]
  total_202012=[]

  #copy_sold_prod=[]
  #sold_prod=[]
  j=0

  #ejemplo de mes impreso
  #print(lifestore_sales[1][3][2:6])

  for j in range(len(lifestore_sales)):
      if lifestore_sales[j][3][6:10]=='2020' and lifestore_sales[j][4]==0:
          total_y=lifestore_sales
          total_2020_year.append(total_y[j])
      elif lifestore_sales[j][3][6:10]=='2002' and lifestore_sales[j][4]==0 :
          total_y1=lifestore_sales
          total_2002_year.append(total_y1[j])
      elif lifestore_sales[j][3][6:10]=='2019' and lifestore_sales[j][4]==0:
          total_y2=lifestore_sales
          total_2019_year.append(total_y2[j])

  #print(len(total_2020_year))
  #print(len(total_2019_year))
  #print(len(total_2002_year))

  i=0
  for i in range(len(total_2020_year)):

      if total_2020_year[i][3][3:5]=='01' and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202001.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='02'and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202002.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='03' and total_2020_year[i][4]==0:
         total_y=total_2020_year
         total_202003.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='04' and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202004.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='05' and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202005.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='06' and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202006.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='07' and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202007.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='08' and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202008.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='09' and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202009.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='10' and total_2020_year[i][4]==0:
         total_y=total_2020_year
         total_202010.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='11' and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202011.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='12' and total_2020_year[i][4]==0:
          total_y=total_2020_year
          total_202012.append(total_y[i][1])
  #print(len(total_202001))
  #print(len(total_202002))
  #print(len(total_202003))
  #print(len(total_202004))
  #print(len(total_202005))
  #print(len(total_202006))
  #print(len(total_202007))
  #print(len(total_202008))
  #print(len(total_202009))
  #print(len(total_202010))
  #print(len(total_202011))
  #print(len(total_202012))

  #Creación de lista ventas en dinero de enero 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202001:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  print("""Esta es la tabla de ventas promedio por mes, solo
  hay un mes para los años de 2019 y 2002 por lo que no se
  incluyo todos los meses de esos años.\n""")
  
  #Año 2002
  total_2002=lifestore_products[total_2002_year[0][1]-1][2]
  promedio=lifestore_products[total_2002_year[0][1]-1][2]/len(total_2002_year)
  print("|Promedio del total de ventas mayo 2002      |"+"$"+str(promedio)+"  |")

  #Año 2019
  print("|Promedio del total de ventas noviembre 2019 |"+"$0"+"      |")

  #Tabla enero 2020
  promedio=round(sum(total_month)/len(total_month),2)
  print("|Promedio del total de ventas enero 2020"+"     |$"+str(promedio)+"|")

  #Creación de lista ventas en dinero de febrero 2020
  j=0
  i=0
  total_month2=[]
  for j in range(len(lifestore_products)):
      for i in total_202002:
          if lifestore_products[j][0]==i:
              total_02=lifestore_products[j][2]
              total_month2.append(total_02)
              #print(lifestore_products[j][2])
              #print()

  #Tabla febrero 2020
  promedio=0
  promedio=round(sum(total_month2)/len(total_month2),2)
  print("|Promedio del total de ventas febrero 2020   |"+"$"+str(promedio)+"|")
  #Creación de lista ventas en dinero de marzo 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202003:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla marzo 2020
  promedio=0
  promedio=round(sum(total_month)/len(total_month),2)
  print("|Promedio del total de ventas marzo 2020     |"+"$"+str(promedio)+"|")

  #Creación de lista ventas en dinero de abril 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202004:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla abril 2020
  promedio=0
  promedio=round(sum(total_month)/len(total_month),2)
  print("|Promedio del total de ventas abril 2020     |"+"$"+str(promedio)+"|")

  #Creación de lista ventas en dinero de mayo 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202005:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla mayo 2020
  promedio=0
  promedio=round(sum(total_month)/len(total_month),2)
  print("|Promedio del total de ventas mayo 2020      |"+"$"+str(promedio)+"|")

  #Creación de lista ventas en dinero de junio 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202006:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla junio 2020
  promedio=0
  promedio=round(sum(total_month)/len(total_month),2)
  print("|Promedio del total de ventas junio 2020     |"+"$"+str(promedio)+" |")

  #Creación de lista ventas en dinero de julio 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202007:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla agosto 2020
  promedio=0
  promedio=round(sum(total_month)/len(total_month),2)
  print("|Promedio del total de ventas julio 2020     |"+"$"+str(promedio)+"|")

  #Creación de lista ventas en dinero de agosto 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202008:
         if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla sep 2020
  promedio=0
  promedio=round(sum(total_month)/len(total_month),2)
  print("|Promedio del total de ventas agosto 2020    |"+"$"+str(promedio)+"|")
  #Creación de lista ventas en dinero de sep 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202009:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla sep 2020
  promedio=0
  if sum(total_month)!=0:
      promedio=round(sum(total_month)/len(total_month),2)
      print("|Promedio del total de ventas septiembre 2020|"+"$"+str(promedio)+" |")
  else:
      print("|Promedio del total de ventas septiembre 2020|"+"$0      |")

  #Creación de lista ventas en dinero de octubre 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202010:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla oct 2020
  promedio=0
  if sum(total_month)!=0:
      promedio=round(sum(total_month)/len(total_month),2)
      print("|Promedio del total de ventas octubre 2020   |" +"$"+str(promedio)+"|")
  else:
      print("|Promedio del total de ventas octubre 2020   |"+"$0      |")

  #Creación de lista ventas en dinero de noviembre 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202011:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla nov 2020
  promedio=0
  if sum(total_month)!=0:
      promedio=round(sum(total_month)/len(total_month),2)
      print("|Promedio del total de ventas noviembre 2020  |"+"$"+str(promedio)+"|")
  else:
      print("|Promedio del total de ventas noviembre 2020 |" +"$0      |")

  #Creación de lista ventas en dinero de diciembre 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in total_202012:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()

  #Tabla dic 2020
  promedio=0
  if sum(total_month)!=0:
      promedio=round(sum(total_month)/len(total_month),2)
      print("|Promedio del total de ventas diciembre 2020 |"+"$"+str(promedio)+"      |")
  else:
      print("|Promedio del total de ventas diciembre 2020 |" +"$0      |")

  enter=input("\nAprieta enter para continuar.")

  #Total anual 2020, 2019 lo saque desde el mensual solo hice una variable para cada total anual
  total_all_2020=[]
  i=0

  for i in range(len(total_2020_year)):
      total=total_2020_year[i][1]
      total_all_2020.append(total)
  # print(total_2020_year[i][1])
  #print(len(total_2020_year))
  #print(len(total_all_2020))

  j=0
  i=0
  total=[]
  for j in range(len(lifestore_products)):
      for i in total_all_2020:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              # print(total_01)
              total.append(total_01)

  print("\nTotal anual entre los tres años de ventas.\n")
  print("|Total de ventas 2002      |"+"$"+str(total_2002)+"   |")
  print("|Total de ventas 2019      |"+"$0     |")
  print("|Total de ventas 2020      |"+"$"+str(sum(total))+"|")
  print("\n")
 

def total_de_ventas():
  #Total de ventas
  #acomodar las 284 ventas con cada id product para saber que producto se vendio más
  sold_product=[]
  j=0
  i=0
  h=0
  for j in range(1,(len(lifestore_products)+1)):#hay 96 id_product
      for i in range (len(lifestore_sales)):
          if lifestore_sales[i][1]==j and lifestore_sales[i][4]==0:
              #print(h)
              h+=1
      #print("id product: "+ str(j)+" " +str(h))
      sold_product.append(h)

      h=0

  #print(sold_product)


  i=0
  total_fin=[]
  for i in range(len(lifestore_products)):
      #print(lifestore_products[i])
      prod_tot1=(lifestore_products[i][2]*sold_product[i])
      #print(prod_tot1)
      total_fin.append(prod_tot1)
  #print(len(total_fin))
  print("""|El total de dinero obtenido por todas las ventas|""")
  print("|                     $"+str(sum(total_fin))+"                    |\n")
def meses_con_mas_ventas():
  sold_product=[]
  j=0
  i=0
  h=0
  for j in range(1,(len(lifestore_products)+1)):#hay 96 id_product
      for i in range (len(lifestore_sales)):
          if lifestore_sales[i][1]==j and lifestore_sales[i][4]==0:
              #print(h)
              h+=1
      #print("id product: "+ str(j)+" " +str(h))
      sold_product.append(h)

      h=0

  #print(sold_product)


  i=0
  total_fin=[]
  for i in range(len(lifestore_products)):
      #print(lifestore_products[i])
      prod_tot1=(lifestore_products[i][2]*sold_product[i])
      #print(prod_tot1)
      total_fin.append(prod_tot1)
  
  total_2020_year=[]
  total_2019_year=[]
  total_2002_year=[]

  #Variables de todos los meses de 2020
  total_202001=[]
  total_202002=[]
  total_202003=[]
  total_202004=[]
  total_202005=[]
  total_202006=[]
  total_202007=[]
  total_202008=[]
  total_202009=[]
  total_202010=[]
  total_202011=[]
  total_202012=[]

  copy_sold_prod=[]
  sold_prod=[]
  j=0

  #ejemplo de mes impreso
  #print(lifestore_sales[1][3][2:6])

  for j in range(len(lifestore_sales)):
      if lifestore_sales[j][3][6:10]=='2020' and lifestore_sales[i][4]==0:
          total_y=lifestore_sales
          total_2020_year.append(total_y[j])
      elif lifestore_sales[j][3][6:10]=='2002' and lifestore_sales[i][4]==0:
          total_y1=lifestore_sales
          total_2002_year.append(total_y1[j])
      elif lifestore_sales[j][3][6:10]=='2019' and lifestore_sales[i][4]==0:
          total_y2=lifestore_sales
          total_2019_year.append(total_y2[j])

  #print(len(total_2020_year))
  #print(len(total_2019_year))
  #print(len(total_2002_year))

  i=0
  for i in range(len(total_2020_year)):

      if total_2020_year[i][3][3:5]=='01'and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202001.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='02' and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202002.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='03' and lifestore_sales[i][4]==0:
         total_y=total_2020_year
         total_202003.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='04' and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202004.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='05' and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202005.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='06' and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202006.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='07' and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202007.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='08' and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202008.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='09' and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202009.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='10' and lifestore_sales[i][4]==0:
         total_y=total_2020_year
         total_202010.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='11' and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202011.append(total_y[i][1])
      elif total_2020_year[i][3][3:5]=='12' and lifestore_sales[i][4]==0:
          total_y=total_2020_year
          total_202012.append(total_y[i][1])
      
  promedio_total=round(sum(total_fin)/len(total_fin),2)
  suma_2019=total_2019=lifestore_products[total_2019_year[0][1]-1][2]
  suma_2002=total_2002=lifestore_products[total_2002_year[0][1]-1][2]
  suma_01=suma_de_mes(total_202001)
  suma_02=suma_de_mes(total_202002)
  suma_03=suma_de_mes(total_202003)
  suma_04=suma_de_mes(total_202004)
  suma_05=suma_de_mes(total_202005)
  suma_06=suma_de_mes(total_202006)
  suma_07=suma_de_mes(total_202007)
  suma_08=suma_de_mes(total_202008)
  suma_09=suma_de_mes(total_202009)
  #print(suma_01)
  #print(suma_02)
  #print(suma_03)
  #print(suma_04)
  #print(suma_05)
  #print(suma_06)
  #print(suma_07)
  #print(suma_08)
  #print(suma_09)

  todas_sumas=[suma_01,suma_02,suma_03,suma_04,suma_05,suma_06,suma_07,suma_08,suma_09]
  mayor_2020=max(todas_sumas)
  mayor_2019=suma_2019
  mayor_2002=suma_2002

  print("Tabla de meses al año con más ventas.\n ")
  print("""|Año |Mes      |Total  | """)
  print("|2002|Mayo     |$" +str(mayor_2002) +"   |")
  print("|2019|Noviembre|$"  +"0   |")
  print("|2002|Abril    |$" +str(mayor_2020) +"|")

def suma_de_mes(lista_ids):
  #Creación de lista ventas en dinero de enero 2020
  j=0
  i=0
  total_month=[]
  for j in range(len(lifestore_products)):
      for i in lista_ids:
          if lifestore_products[j][0]==i:
              total_01=lifestore_products[j][2]
              total_month.append(total_01)
              #print(lifestore_products[j][2])
              #print()
  promedio=round(sum(total_month),2)            
  return(promedio)

#productos_mayores_ventas_busquedas()
#productos_menores_ventas_busquedas()
#lista_20()
#ventas_prom_mensuales_y_anual()
#total_de_ventas()
#meses_con_mas_ventas()

print("""¡Hola!, bienvenido al portal de consultas,
por favor inserta un usuario y contraseña valido

si prefieres salir del programa inserta salir en cualquiera de las dos entradas: usuario o contraseña
""")
put_user= str(input("Usuario: "))
put_password= str(input("Contraseña: "))

while put_user!="admin" or put_password!="admin":
    #condición de salida
    if put_user=="salir" or put_password=="salir":
        print("saliendo del programa.")
        break
    else:
      #mensaje de error
      os.system("clear")
      print("\n")
      print("usuario o contraseña incorrecta,inserta otra vez tus datos: ")
      print("\n")

      #entrada de datos
      put_user= str(input("Usuario: "))
      put_password= str(input("Contraseña: "))




while put_user=="admin" and put_password=="admin":
    #Mensaje de bienvenida
    os.system("clear")
    print("\n")
    print("""¡Bienvenido administrador!
  ¿Qué estás buscando ver en la plataforma?
      
  [1] Productos más vendidos y productos rezagados
  [2] Productos por reseña en el servicio
  [3] Total de ingresos y ventas promedio
  [4] Salir del usuario""")

    #Variable de opcion menu principal
    opcion_a_realizar=input("Ingresa la opción que se quiera realizar (1-2-3-4): ")

    #CONDICION PRINCIPAL PARA SALIR DEL PRIMER WHILE
    if opcion_a_realizar=='4':
        print("Saliendo")
        put_user="salir"

    #Condición submenu 1:
    elif opcion_a_realizar=='1':
        os.system("clear")
        print("""Tipo de clasificación de datos disponibles:
    [1] 10 productos con mayores ventas y 20 con mayores busquedas.
    [2] 50 productos con menores ventas y 50 productos con menores búsquedas, por categoria.
    [3] Salir al menu principal""")


        #Variable submenu1
        opcion_a_realizar_sbm1=input("Ingresa la opción que se quiera realizar (1-2-3): ")

        #Loop de opciones submenu 1
        while opcion_a_realizar_sbm1!='3':
            if opcion_a_realizar_sbm1=='3':
                print("Saliendo al menu principal.")
                continue


        #Condicion 1 da los 50 productos con mayores ventas
            elif opcion_a_realizar_sbm1=='1':
                
                productos_mayores_ventas_busquedas()
                enter=input("Presiona enter para continuar:")
                os.system("clear")
                print("""Tipo de clasificación de datos disponibles:
    [1] 10 productos con mayores ventas y 20 con mayores busquedas.
    [2] 50 productos con menores ventas y 50 productos con menores búsquedas, por categoria.
    [3] Salir al menu principal""")
                print("\nDeseas consultar otro dato o salir\n")
                opcion_a_realizar_sbm1=input("Ingresa la opción que se quiera realizar (1-2-3): ")
                continue


            #Condición 2 da los 100 productos con mayores busquedas
            elif opcion_a_realizar_sbm1=='2':
                productos_menores_ventas_busquedas()
                os.system("clear")
                print("""Tipo de clasificación de datos disponibles:
    [1] 10 productos con mayores ventas y 20 con mayores busquedas.
    [2] 50 productos con menores ventas y 50 productos con menores búsquedas, por categoria.
    [3] Salir al menu principal""")
                print("\nDeseas consultar otro dato o salir\n")
                opcion_a_realizar_sbm1=input("Ingresa la opción que se quiera realizar (1-2-3): ")
                continue

            else:
                os.system("clear")
                
                print("\nOpcion incorrecta intentalo de nuevo\n")
                print("""Tipo de clasificación de datos disponibles:
    [1] 10 productos con mayores ventas y 20 con mayores busquedas.
    [2] 50 productos con menores ventas y 50 productos con menores búsquedas, por categoria.
    [3] Salir al menu principal""")
                opcion_a_realizar_sbm1=input("Ingresa la opción que se quiera realizar (1-2-3): ")


            continue

    elif opcion_a_realizar=='2':
        #Matematicas

        #Impresión de resultados
        lista_20()

        #Variable submenu2
        opcion_a_realizar_sbm2=input("Aprete enter para regresar al menu principal: ")
        continue

    elif opcion_a_realizar=='3':
        os.system("clear")

        print("""Tipo de clasificación de datos disponibles
    [1] Total de ingresos.
    [2] Ventas promedio mensuales, total anuales.
    [3] Meses con más ventas al año
    [4] Salir al menu principal""")
        #Variable submenu3
        opcion_a_realizar_sbm3=input("Ingresa la opción que se quiera realizar (1-2-3-4): ")

        #Loop de opción incorrecta submenu principal
        while opcion_a_realizar_sbm3!='4':
            if opcion_a_realizar_sbm3=='4':
                print("Saliendo al menu principal.")
                continue
            #Condicion 1
            elif opcion_a_realizar_sbm3=='1':
                total_de_ventas()
                enter=input("Inserta un enter para continuar")
                os.system("clear")

                print("""Tipo de clasificación de datos disponibles
    [1] Total de ingresos.
    [2] Ventas promedio mensuales, total anuales.
    [3] Meses con más ventas al año
    [4] Salir al menu principal""")
                opcion_a_realizar_sbm3=input("Ingresa otra opción que desees realizar: (1-2-3-4)")
                continue
            #Condicion 2
            elif opcion_a_realizar_sbm3=='2':

                ventas_prom_mensuales_y_anual()
                enter=input("Inserta un enter para continuar")
                os.system("clear")

                print("""Tipo de clasificación de datos disponibles
    [1] Total de ingresos.
    [2] Ventas promedio mensuales, total anuales.
    [3] Meses con más ventas al año
    [4] Salir al menu principal""")

                opcion_a_realizar_sbm3=input("Ingresa otra opción que desees realizar: (1-2-3-4)")
                continue
            #Condicion 3
            elif opcion_a_realizar_sbm3=='3':
                meses_con_mas_ventas()
                enter=input("Inserta un enter para continuar")
                os.system("clear")

                print("""Tipo de clasificación de datos disponibles
    [1] Total de ingresos.
    [2] Ventas promedio mensuales, total anuales.
    [3] Meses con más ventas al año
    [4] Salir al menu principal""")
                opcion_a_realizar_sbm3=input("Ingresa otra opción que desees realizar: (1-2-3-4)")
                continue
            else:
              
                os.system("clear")

                print("""Tipo de clasificación de datos disponibles
    [1] Total de ingresos.
    [2] Ventas promedio mensuales, total anuales.
    [3] Meses con más ventas al año
    [4] Salir al menu principal""")
                opcion_a_realizar_sbm3=input("Opcion incorrecta.\nIngresa otra opción que desees realizar: (1-2-3-4)")
            continue



    else:
        print("Opción incorrecta intenta de nuevo.")
        continue


print("finalizo el programa buen dia")
