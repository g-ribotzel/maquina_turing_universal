#Registro de transiciones
class transicion:
  pass

#función principal de la lectura de las transiciones
def workString(word):
  #Estructura hashing
  delta = list()
  
  #Separa las transiciones por cada salto de linea
  workSplit = word.split("\n")

  #arma el hashing
  for y in range(0,len(workSplit)):
    delta.append(list())

  #Crea los registros de cada función de transicion
  #y los introduce dentro del hashing según la función
  #hashing h(x) = tranStruct.start
  for x in range(0,len(workSplit)):
    tranStruct = transicion()
    tranSplit = workSplit[x].split(",")
    tranStruct.start = int(tranSplit[0])
    tranStruct.startSymbol = tranSplit[1]
    tranStruct.end = int(tranSplit[2])
    tranStruct.endSymbol = tranSplit[3]
    tranStruct.move = tranSplit[4]
    delta[tranStruct.start].append(tranStruct)
    
  #retorna la estructura construida
  return delta
