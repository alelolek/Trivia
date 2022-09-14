RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

class Categoria: 
    def __init__(self, id, nombre): 
        self.id = id
        self.nombre = nombre
   
# creating list       
categorias = [] 
  
# appending instances to list 
categorias.append( Categoria(1,'Historia') )
categorias.append( Categoria(2,'Algoritmia') )
categorias.append( Categoria(3,'Sintaxis') )

class Pregunta: 
    def __init__(self, id, descripcion,respuesta,idCat): 
        self.id = id
        self.descripcion = descripcion
        self.respuesta = respuesta
        self.idCat = idCat

preguntas = [] 
  
# appending instances to list 
preguntas.append(Pregunta(1,'1) ¿Desde cuándo podemos copiar y pegar?','a',1) )
preguntas.append(Pregunta(2,'2) ¿Recuerdas cuál fue el primer navegador de la historia?','c',1) )
preguntas.append(Pregunta(3,'3) En qué año se desarrolló el lenguaje de programación C?','d',1) )

preguntas.append(Pregunta(4,'1) ¿Cual es  la representación textual de un algoritmo?','b',2) )
preguntas.append(Pregunta(5,'2) ¿Que es un algoritmo?','a',2) )
preguntas.append(Pregunta(6,'3) Son bloques o simbolos que representan cada una de las etapas de un algoritmo, siguiendo estandares que permita a cualquier persona comprenderlos','d',2) )

preguntas.append(Pregunta(7,'1) La carpeta creada por Python utilizada para almacenar archivos pyc se llama :','c',3) )
preguntas.append(Pregunta(8,'2) Es un operador capaz de verificar si dos valores son diferentes :','b',3) )
preguntas.append(Pregunta(9,'3) ¿Que hace len()?','a',3) )

class Alternativa: 
    def __init__(self, id, descripcion,idPre): 
        self.id = id
        self.descripcion = descripcion
        self.idPre = idPre

alternativas = [] 
  
# appending instances to list 
alternativas.append(Alternativa(1,'a) 1981',1) )
alternativas.append(Alternativa(2,'b) 1986',1) )
alternativas.append(Alternativa(3,'c) 1982',1) )
alternativas.append(Alternativa(4,'d) 1984',1) )

alternativas.append(Alternativa(5,'a) Netscape Navigator',2) )
alternativas.append(Alternativa(6,'b) Safari',2) )
alternativas.append(Alternativa(7,'c) World Wide Web',2) )
alternativas.append(Alternativa(8,'d) Internet Explorer',2) )

alternativas.append(Alternativa(9,'a) 1968',3) )
alternativas.append(Alternativa(10,'b) 1970',3) )
alternativas.append(Alternativa(11,'c) 1974',3) )
alternativas.append(Alternativa(12,'d) 1972',3) )

alternativas.append(Alternativa(13,'a) Algoritmo',4) )
alternativas.append(Alternativa(14,'b) Pseudoocodigo',4) )
alternativas.append(Alternativa(15,'c) Diagrama de flujo',4) )
alternativas.append(Alternativa(16,'d) Cadena',4) )

alternativas.append(Alternativa(17,'a) Un conjunto de instrucciones o reglas bien definidas y ordenadas que permiten realizar una actividad mediante pasos sucesivos.',5) )
alternativas.append(Alternativa(18,'b) Es una igualdad entre dos expresiones algebraicas, denominadas miembros, en las que aparecen valores conocidos o datos.',5) )
alternativas.append(Alternativa(19,'c) Es una relación de variables que pueden ser cuantificadas para calcular el valor de otras de muy difícil calculo.',5) )
alternativas.append(Alternativa(20,'d) Todas las anteriores.',5) )

alternativas.append(Alternativa(21,'a) Simbologia de diagramas de Arbol',6) )
alternativas.append(Alternativa(22,'b) Simbologia de Diagramas de bloque',6) )
alternativas.append(Alternativa(23,'c) Simbologia de Diagramas de Entidad Relacion',6) )
alternativas.append(Alternativa(24,'d) Simbologia de Diagramas de flujo',6) )

alternativas.append(Alternativa(25,'a) _pyc_',7) )
alternativas.append(Alternativa(26,'b) _pycfiles_',7) )
alternativas.append(Alternativa(27,'c) _pycache_',7) )
alternativas.append(Alternativa(28,'d) _cache_',7) )

alternativas.append(Alternativa(29,'a) =/=',8) )
alternativas.append(Alternativa(30,'b) !=',8) )
alternativas.append(Alternativa(31,'c) <>',8) )
alternativas.append(Alternativa(32,'d) not ==',8) )

alternativas.append(Alternativa(33,'a) Se utiliza para determinar la longitud',9) )
alternativas.append(Alternativa(34,'b) Se utiliza para separar una cadena ',9) )
alternativas.append(Alternativa(35,'c) Se utiliza para devolver un objeto que no tiene características',9) )
alternativas.append(Alternativa(36,'d) Se utiliza para poner en mayuscula todos los caracteres',9) )

def obtenerCategorias():
    return categorias

def obtenerPreguntasPorCategoria(categoriaId):
    return list(filter(lambda x: (x.idCat == categoriaId), preguntas))

def obtenerAlternativasPorPreguntas(preguntaId):
    return list(filter(lambda x: (x.idPre == preguntaId), alternativas))

import random

def obtenerAlternativaDeBot():
    alternativasDeBot = ['a','b','c','d']
    respuestaRandom = random.randint(0,3)
    return alternativasDeBot[respuestaRandom]

import time

def main():
    listaCategorias = obtenerCategorias()
    respuestaNombre = input('Ingresa tu nombre :')
    print('Recuerda que estas compitiendo contra un jugador de otra parte de este mundo!!')
    time.sleep(2)
    print('\n¡Bienvenido',respuestaNombre,'! La trivia iniciará en...')
    for i in range (5,0,-1):
        print(i, '...')
        time.sleep(1)
    print(CYAN,'\n******* EMPEZEMOS LA TRIVIA ********\n',RESET)
    while True:
        puntaje = []
        puntajeBot = []
        for categoria in listaCategorias:
            print(categoria.id,categoria.nombre)
        respuestaCategoria = input('\nIngresa una categoria :')
        while respuestaCategoria not in  ('1','2','3'):
                respuestaCategoria = input('\nIngresa una categoria válida :')
          
        listaPreguntas = obtenerPreguntasPorCategoria(int(respuestaCategoria))

        for pregunta in listaPreguntas:
            print('\n'+pregunta.descripcion)
            listaAlternativas = obtenerAlternativasPorPreguntas(pregunta.id)
            for alternativa in listaAlternativas:
                print(alternativa.descripcion)

            respuestaAlternativa = input('\nIngresa una alternativa :')
            while respuestaAlternativa.lower() not in ('a','b','c','d'):
                respuestaAlternativa = input('\nIngresa una alternativa válida :')
            if respuestaAlternativa == pregunta.respuesta:
                print(GREEN+'Respuesta correcta',RESET)
                puntaje.append(1)
            else:
                puntaje.append(0)
                print(RED+'Respuesta incorrecta',RESET)

            respuestaDeBot = obtenerAlternativaDeBot()
            if respuestaDeBot == pregunta.respuesta:
                puntajeBot.append(1)
            else:
                puntajeBot.append(0)

            time.sleep(1)

        if sum(puntaje) > sum(puntajeBot): 
            print('\n'+GREEN+'Felicitaciones!! Ganaste con',sum(puntaje),' puntos y tu rival perdió con',sum(puntajeBot),'puntos',RESET)
        elif sum(puntaje) == sum(puntajeBot): 
            print('\n'+YELLOW+'Tu rival y Tu empataron con',sum(puntaje),'pt',RESET)
        else: 
            print('\n'+RED+'Lo siento. Perdiste con',sum(puntaje),' puntos y tu rival ganó con',sum(puntajeBot),'puntos',RESET)

        respuestaReintentar = input('Deseas intentarlo otra vez? Si o No : ')
        print()
        if( respuestaReintentar.lower() != 'si'):
            break

if __name__ == "__main__":
    main()