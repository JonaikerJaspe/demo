# listaDeCadenas = ["Helo","my","Friend"]
 
# miCadena = " ".join(listaDeCadenas)
# print(miCadena)

# d1 = {"nombre": "Jonaikr", "edad":22}
# d2= {"nombre": "Jonaiker","city":"San juan"}


# conbinar = {**d1,**d2}
# print(conbinar)

# colores = ["rojo","verde","blue"]
# c = "rojo"

# if c in colores:
#     print("el color esta alli")

# lista = []
# # Forma normal
# for i in range(10):
#     lista.append(i*i)
# print(lista)


# # Forma recomendada
# lista2 = [i * i for i in range(10)]
# print("*" * 100)
# print(lista2) 
#-------------------------------------------------------
# data = [
#     {"nombre":"Jonaiker", "edad":22},
#     {"nombre":"Jhon","edad":23},
#     {"nombre":"Jaspe","edad":42},
#     {"nombre":"Primers","edad":12},
#     {"nombre":"Jonas","edad":72},
#     {"nombre":"Jhos","edad":52}
#         ]



# dataOrdenada = sorted(data, key=lambda x: x["edad"])
# print(dataOrdenada)

#--------------------------------------------------------


#definir valores predeterminados en diccionarios 
# myDict ={"nombre":"Jony", "apellido":"roberto"}


# #normal 

# apellido = myDict["apellido"]
# print(apellido)

#----------------------------------------------------------

# from collections import Counter


# lista = [1,2,3,1,2,1,4,3,5,6,5,4,3,1]
# counter = Counter(lista)
# print(counter)
# print(counter[1])

#-----------------------------------------------------------

# Cadenas de formato con f-Strings

# name = "Jon"
# miCadena = f"Hello , my is name {name}"
# print(miCadena)


# lastName = "Omar"
# miOtraCadena = f"Hola, Como has estados {lastName}"
# print(miOtraCadena)