##################################################################################
#Lo primero a entender son los date type o dicho de otra forma los tipo de datos #
##################################################################################

 #Strings (texto):
 #para utilizar un Strings se le nesecitan poner las (" ") aqui muestro las distintas formas 
 print("hola")
 print('hola')
 print("""hola""")
 print('''hola''')

 #con el comando type te demuestro que esta clase de archivos son Strings
 print(type("hola"))

 #puedes enlazar Strings por ejemplo "adios" + "mundo" (recuerda poner el espacio)
 print("adios" + "mundo")

 #Integer (enteros):
 #Aqui te demustro con el comado type que este archivo es un interger (numero entero)
 print(type(3+3))

 #Float(decimales):
 #Aqui te demuestro que este archivo es un float(numero decimal) con el comado type
 print(type(3.5+3))

 #Bolean(Verdadero o Falso)
 #Los Bolean son tipos de archivos que son lo pueden ser verdaderos o falsos
 True
 False

 #List(listas):
 #Las listas son tipos de archivos que gardan una serie de elemntos dentro de si (Strings,float,Interger,etc) 
 [10,20,30,50]
 ["hola", "adios"]
 ["hola",20,1.5,"true"]
 []

 #Tuplas:
 #Las duplas son como las listas con la diferencia de que estas son invariables osea que no se pueden cambiar 
 print((10,20,30,50))

 #Diccionarios
 #Los diccionarios tambien son como las listas con deferncia de que en estos puedes hacer una especificacion de cada elemento dentro del dicionario
 print(type({ 
 "name":"Rayan",
 "last_name":"Ray",
 "nick_name":"LOL" 
 }))
 
 #nada
 None


#################################### 
# OK ahora veremos las : VARIABLES #
####################################
 #Las variables son un tipo de archivo al cual le asignamos un nombre y un valor con un (=)


 #Case Sensitive( Las variables pueden tener cualquier nombre)
 Name = "Simon"
 name = "Simon"


 #se puede hacer asi 
 #Se puedenhacer dos variables en una sola linae de codigo poniendo : NombreVarible1 , NombreVarible2 = Valor1 , Valor2
 x , book= 10,"Los estrañamientos"
 print(x , book)

 #o asi 
 #Tambien se pueden hacer en dos lineas de codigo separadas asi : NombreVariable1 = Valor1
 #                                                                NombreVariable2 = Valor2
 x = 10 
 book = "Los estrañamientos"
 print(x)
 print(book)


 #Convensiones
 #Las conveciones exsisten para poner el nombre a una variables y que sea mas legible (esto no es bligatorio) acomtinuacion te muestro las convenciones:

 book_name = "Yoloman"    #Snake Case
 Bookname = "trolman"     #Camel Case
 BookName = " holaquehace"#Pascal Case
 PI = 3.1416              #constantes


##################################
#OK ahora veremos los : STRINGS  #
##################################
 
 
 #Los Strings son archivos de texto

 #estos archivos se le puden asignar a una variables de esta manera
 myStr = "Hello World"

 # y tambien se pueden imprimir por pantalla con la funcion print
 print(myStr)

 #ademas se pueden juntar y imprimir en la pantalla con otras palabre de 3 maneras diferentes

 print(myStr + " hola")#puedes juntar una vaqriable con un texto o numero pero simpre utilizando las ("")

 (f"hola {myStr }")#tambien se puede ejecutar asi (lo que hace la F es dicirle al archivo que busque la variable que esta entre {}
 
 ("hola {0}",format(myStr))#o tambien asi la diferenci es que asi le decimos posicion en la cual colocar el texto asi {}


 #hay diferentes comados para que los nuestro Strings tengan propiedades particulares 
 #hay muhos mas que estos buscalo con el comando dir por jemplo: print (dir(myStr))

 print(myStr.upper())#todo en mayusculas 
 print(myStr.lower())#todo en miniculas
 print(myStr.swapcase())#cambia las mayuculas y minusculas
 print(myStr.capitalize())#pone la primera latra en mayusacula

 print(myStr.replace('Hello', 'hola'))#cambia un palabra por otra  
 print(myStr.count('l'))#saber cuantas vesces sale cada caracter

 print(myStr.startswith('H'))#sirve para saber con cual caracter comienza el texto
 print(myStr.endswith('d'))#sirve para saber con cual carater temna mi texto

 print(myStr.split(' '))#separa a partir de un caracter
 print(myStr.find(" "))#te dice la posicion del caracter del caracter 

 print(len(myStr))#dice la longitud del texto
 print(myStr.index(" "))#te dice la posicion del caracter

 print(myStr.isnumeric())#pregunta si el codigo es numerico 
 print(myStr.isalnum())#pregunta si el codigo no es numerico 

 print(myStr[5])#te dice el simbolo que hay en una determinada posicion en este caso es " "
 print(myStr[-5])#si lo pones en negativo cuenta alreves en esta caso w "w"


########################
# LOS NUMEROS EN PYTHON #
#######################

 #tipos de numeros mas comunes 
 print(type(10))#enterosw 
 print(type(10.1))#decimales
 
 #tipos de operaciones que odemos hacer

 print(3-2)#resta
 print(3+2)#suma
 print(3/2)#divison
 print(3*2)#multiplicacion
 print(3%2)#para el residuo de una division
 print(3**2)#potenciacion
 print(3//2)#hace que la division te de un entero
 print((5*2)-5+5)#este es un ejemplo para que sepas que operaciones se hacen primero (siempre primero se hacer las multiplicacionesw y diviciones como si fuerea una ecuacion)

 print(input("insert your age :"))#el imput sirve para que la consola tipee algo que usuasrio escriba y se le puede dejar un mensaje al uasurio
 
 age = input("insert your age:")#tambien puedes poner el input como una variable asi manipularlo como tal 
 
 new_age = int (age) + 5 #bien lo que hacesmos aqui es hacer una nueva variable llamada new_age esta sera equivlaente a age+5 y con el comando int transformamos age a nuemero por que el progrma lo ve como texto 
 
 print(new_age)#por ejemplo 
 
 print(new_age) 

 #exsisten distintos tipos de comandos para cambiar una variable o un texto con forma de numero 
 #int (convierte un texo a un numero entero)
 #floaat (convierte un texto a un numero flotante o decimal)
 #INPORTANTE: esto solo convierte a numeros los textos que se puedan entender como nuemros ejemplo: NO comvetiria a un hola a numeros , si no mas bien un numero que este escrito como texto lo convirta a numeros para la maquina ejemplo: este "10"no es un numero pero este si 10 esto tambien pasa en las variables como vemos en el ejemplo anterior


####################
#LIATAS EN PYTHON  #
#################### 

 #las listas se crena con [] y sirven para almacenar un listado de cosas (se le pueden poner distintos tipos de archivos como en esta y tambien se le puede asignar a una variablecomo en ente ejemplo)
 
 demo_lists=[1,"hello",1.0,[1,2,3], True]
 
 
 #exsisten listas que contienen un solo tipo de archico por ejemplo
 colors = ["blue", "red" , "green"]
 
 
 #tambien se puede hacer una lista de esta forma PERO SOLO SE PUEDE PONER UN DATO si quieres poner mas de uno como en este caso que tendrias conjuntar los en una dupla osea esto (()) para que asi lo cuente como un jemplo 1,2,3 estamal pero (1,2,3) se cunta como un solo dato
 number_list = list((1,2,3))
 
 #aqui imprimimos la variable a la cual le asignamos la lista
 print(number_list)
 
 
 #exsiste eta funcion denominada rango que te da todos los numeros de un rango que tu definas en esta caso del 1-10(tambien se pueden hacer listas con esta funcion para ahorar tiempo)
 range(1, 10) 


 #una cosista el comado solo cunta asta un numero antes del que le marcaste en esta caso deria 1-9 enves de 1-10. En este caso lo imprimo directamente pero si gustas lo puedes declarar como una variable
 print(list(range(1,10))) 
 
 
 #las [] sirven para al progrma busque dentro de una duplas un determinado archivo [blu,red,green] cuentan como un solo archivo pero cuando le digo que busque [1] me da solo el archivo que este en la posicion que li digo que busque
 print(colors[0])

 # es lo mismo pero cuenta alreves (de derecha a izquierda)(otra cosa se cuenta el 0)
 print(colors[-0])
 # "in"  es un booleano y su funcion es preguntar si determinado archivo esta un una variable o lista (solo de tru o false es lo que significa booleano)
 print( "red" in colors)

 print(colors)
 #lo que hace esto es cambiar un determinado dato de una lista (recuerda que su cuenta el 0) asi que cambio red (que estaba en la posision 1) por "yellow"
 colors[1] = "yellow"
 
 print(colors)


 #METODOS
 colors.append(("blacK", "violet"))#el append sirve para agregar algo a un archivo en esta caso el negro y el violeta al archivo de colores, pero solo se puede pasar un archivo asi que en esta caso lo que ariamos es paserlo como tupla osea poniendo ()
 
 colors.extend(["black","violet"])#esto hace la misma funcion que el otro con la diferencia de que en bes de pasarlo como un solo archivo los pasa como dos indeviduales (paro igual hay que ahcerlo como un solo archivo)
 
 colors.insert(1,"white")#esto inserta un determinado aechivo en la lista colors la diferencia es que aqui le dices la poscion en la cual quieres insertar el nuevo archivo(siempre se cunta desde 0)
 
 colors.insert(len(colors),"white")#utilizamos el len para medir la longitud de colors (que por eso lo agregamos entre parentesis)y asi poner a "white" al final
 
 colors.pop()#quita el ultimo elemente de la lista en este caso colors o bien si se le asigna un indice quita el elemento que esta hay
 
 colors.remove("blue")  #lo que hace es quitar un elemento de la lista en esta caso quita el red de colors
 
 colors.clear()#su funcion es vaciar por completo la lista
 
 colors.sort()#lo que hace es ordenar la lista alfabeticamente
 
 colors.sort(reverse = True)# lo que hace es ordenarlos alfabeticamente pero a la inversa
 
 colors.index("yellow")# te dice el indice de un archivo en una lista  (contando desde 0)
 
 print(colors)
 
 colors.count("yellow")#cuenta las veces que se repite un archivo en la lista
 

####################
#     TUBLES       #
####################

 #la duplas son como las lista con dos grades differencias 1: tienden a ejecutarse mas rapido y a ser un poco mas seguras 2:este tipo de listas no son modificable
 x = (1,2,3)#se puede hacer con numeros 

 #aqui te muestro con type que es una tuple
 months = ("Janaury","Februari","March","April","May","June","August","September","October","November","Decenber")#  se pude con letras 

 #aqui te muestro conson duplas con type
 print(type(x))

 print(type(months))
 # Las tuples tienen que tener mas de un elemento si no el lenguaje no lo considerara una tuple si no como otro dato mira este ejemplo
 y = (1)
 c  = (1,)

 #si te fijas (y) no es una tuple pero (c) si para que sepas una forma de poner un solo archivo y que el lenguaje te lo cuente como tuple es poniendo una (,) por eso si si es una tuple
 print(type(c))
 print(type(y))

 print(x[1])# en la tuples el [] sirve para saber en que indice esta el archivo

 del x # el del sirve paa borra la tupla a la mitad del archivo por jemplo si ejecuto x me ba a dar un erro

 print(x)



####################
#       set        #
####################
 # Los set son paracidos a las litas de tados con la diferencia de que este no tiene ningun orden osea indice
 colors = {"blue", "red", "green"}
 #aqui podemos fonfirmar que colors es un set
 print(type(colors))
 
 #se pude hacer mucho mas buscalo con dir asi
 print(dir(colors))
 
 #estos son algunos ejemplos
 colors.add("Vieolet")#add es para añadir un archico al set 
 colors.remove("red")#remove espara quitar un archivo de del set



####################
#    Diccionarios  #
####################
 
 #el diccionario es como una lista con la diferencia de que en este se pueden guardar descriciones o valores de cada producto jemplo : ponemos en la lista nema : bokk lo que significa que el archivo name es equivalente a book
 producto = {"name":"book",
 "quantity": 3,
 "price ": 4.23}

 person = {
 "first_name ":"Rallan",
 "last_name": "juan"  }
 
 #aqui te muestro que tanto producto como person son diccionarios 
 print(type(person))
 print(type(producto))
 
 #esta es una lista de lo que puedes hacer 
 print(dir(producto))
 
 #te voy a dar algunos ejemplos :
 print(person.keys())#con esto solo vas a obtener el valor de las llaves
 print(person.items())#con esto te va el diccionario completo
 print(person.clear())#con el comado clear linpias lo que sea que este adentro 

 del producto #tambien se puede eliminar los diccionarios como en cualquier otra lista CON EL DEL

 #tambien se pude hacer un lista de diccionarios 
 diccionari_list = [ 
 {"first_name ":"Rallan","last_name": "juan" },
 {"name":"book","quantity":3,"price ":4.23}
 ]


#####################
#   Condicionales   #
#####################
 #como su nombre lo dice las condicionales es un tipo de archivo que actua en consecuensia de un sierto echo .Tambien tienes que saber que se maneja por boleanos osea true y false , otra cosa es como se hace la operaciones aqui son por >,< osea meyor o menor que y la igualdad se escribe con doble signo de igual == y no conun solo =  

 x = 20
 y = 10

 if x < 30 :
     print("x is less than 30")#el if se usa para decir que esto es una condicional se ponen las condiciones seguido de : para incar la accion (notapresiona la letra tabular alprincipio de la accion o si no te va a dar error)

 else:
      print("x is greater than 30")#el else es un sino por ejemplo si esta condicional no se cumple poner este otro texto
      #tanbien se puede hacer con texto no solo con numeros como muestro en este ejmplo

 color = "blue"

 if color == "red" :
     print("the color is red")
    
 elif color == "blue":#la elif es el punto medio entre el if (si) y el else (no) aqui por ejemplo lo utilizo para preguntar por un 3 color (el blue)
     print("the color is blue")
    
 else:
     print("any color")


 #tanbien se pueden usa variables dentro de otra varible como en este ejemplo
 name = "simon"
 last_name = "lozada"

 #IMPORTANTE , recuerda que se deja un espacio con el tabular para designar la gerarquia o orden de acciones como ves aqui se deja el espacio dependiendo del orden de sucesos
 if name == "simon":
     if last_name == "lozada":
         print("you are simon lozada")
     else:
         print("are you not simon lozada")
 else :
     print("you are not simon")

 #Exsiste el comando and que es para agreagar una condicion a la variable es este caso si x es mayor que 9 Y  menor o igual que 20 veinte escribir esto
 if x > 9 and x <= 20:
     print("x is greater than 9 and less than 21")

 #Exsiste el comando or y su funcion es agregar una conicion a la variable en este caso es si x es mayor que 2 O x es menor o igual que 20 x es un numero mayor que dos o menor que veinte
 if x > 2 or x <= 20:
     print("x is a number greater than 2 or equal to 20")

 # Exsiste el comado not este sirve para hacer una accion si dos cosas no son de cierto modo en este caso si x NO es igual que y dice x no es igual que y
 if (not(x == y)) :
     print("x is not equal y")