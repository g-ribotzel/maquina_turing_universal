#Maquina de turing
#recibe: una lista de listas "delta" que se trabaja como hashing 
#que contiene a todas las funciones de transicion,
#el string "word" que contiene la palabra leída por la MT,
#los enteros "ini" y "fin" como estado inicial y final respectivamente
def turing(delta ,word ,ini ,fin):
  #inicialización de variables
  acepta = False
  rechaza = False
  currentState = ini
  cinta = list()
  #creación de la "cinta"
  for x in range(0,len(word)):
    cinta.append(word[x])
  #llena la cinta de blancos "#"
  for y in range(0,len(cinta)+6):
    cinta.append("#") 
  cabezal = 0
  #Inicializando la MT
  while( not rechaza and not acepta ):
    busca = 0
    #Busca la función de transición correspondiente
    while( busca < len(delta[currentState]) and delta[currentState][busca].startSymbol != cinta[cabezal] ):
      busca = busca + 1
    #si no encuentra la función de transición la palabra es rechazada
    if( busca >= len(delta[currentState]) ):
      rechaza = True
    #de lo contrario se halló una función de transición que coincide con
    #el estado actual y con el caracter que se está leyendo en el momento
    else:
      #se actualiza el símbolo que está en la cinta
      cinta[cabezal] = delta[currentState][busca].endSymbol
      #se verifica hacia dónde se tiene que mover el cabezal en la cinta
      #si el símbolo es "D" el cabezal se mueve a la derecha
      if( delta[currentState][busca].move == "D" ):
        cabezal = cabezal + 1
      #de lo contrario, el cabezal se mueve a la izquierda
      else:
        cabezal = cabezal - 1
      #se actualiza el estado actual
      currentState = delta[currentState][busca].end
      #se verifica si el estado actual es el estado final
      #si lo es, la palabra es aceptada, de lo contrario
      #se sigue iterando en el bucle
      if( currentState == fin ):
        acepta = True
  #retorna el boleano acepta
  return acepta

