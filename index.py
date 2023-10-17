# import asyncio

# async def tarea_1():
#     print("Tarea 1 iniciada")
#     await asyncio.sleep(1) #Esperar 1 segundo
#     print("Tarea 1 finalizada")

# async def tarea_2():
#     print("Tarea 2 iniciada")
#     await asyncio.sleep(2) #Esperar 2 segundo
#     print("Tarea 2 finalizada")


# async def tareaEnParalelo():
#     _tarea_1 = asyncio.create_task(tarea_1())
#     _tarea_2 = asyncio.create_task(tarea_2())


#     await asyncio.gather(_tarea_1,_tarea_2)

# asyncio.run(tareaEnParalelo())    




numeros = [1,2,3,4,5,6,7,8,9,10]
impares = list(filter(lambda x: x %2 != 0 , numeros))
print(impares)
print("*" * 100)
#MAP
# Elevar al cuadrado los  numeros de una lista 
cuadrados = list(map(lambda y:y**2, numeros))
print(cuadrados)
print("*" * 100)
#Redudce

from functools import reduce

suma = reduce(lambda x,y: x+y, numeros)
print(suma)