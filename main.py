from funciones import Funciones
import random
t=0 #Contador
num_poblacion = 10
Ngeneraciones=10
proba_muta=0.5
Mejor_resultado=[]
#Inicializa P(t)
a = Funciones.creacion_de_poblacion(num_poblacion,2,-100,100)
#print("Creando la poblacion \n")
#Funciones.Mostrar(a)
#-----------------------------

#Evaluamos P(t)
b=Funciones.aptitud(a,num_poblacion)
#print("Aptitudes\n")
#Funciones.Mostrar_arreglo(b)
#-------------------

while (t<Ngeneraciones):
    t+=1
    torneo_o_ruleta=random.randint(0,1)
    #Seleccionamos ya sea por torneo o ruleta
    if(torneo_o_ruleta==0):

        elegidos=Funciones.nex_generacion(b,"Ruleta",a,num_poblacion)
        #print("Seleccionados por ruleta\n",len(elegidos))
        
        #Funciones.Mostrar(elegidos)
    else:
        elegidos=Funciones.nex_generacion(b,"Torneo",a,num_poblacion)
        #print("Seleccionados por torneo\n",len(elegidos))
        #Funciones.Mostrar(elegidos)
    #-----------------------------------------
    
    punto_o_puntos=random.randint(0,1)
    if(punto_o_puntos==0):
        cruza=Funciones.cruzamiento(elegidos,num_poblacion,"Punto")
        #print("Cruzados por un punto\n",len(cruza))
        #Funciones.Mostrar(cruza)
    else:
        cruza=Funciones.cruzamiento(elegidos,num_poblacion,"Puntos")
        #print("Cruzados por un puntos\n",len(cruza))
        #Funciones.Mostrar(cruza)

    
    #Mutamos
    muta=Funciones.muta(cruza,num_poblacion,proba_muta)
    #print("Muta\n")
    #Funciones.Mostrar(muta)
    print("Resultados",Funciones.regresa_Mejor_generacion(muta,num_poblacion))

    if(t==1):
        Mejor_resultado=Funciones.regresa_Mejor_generacion(muta,num_poblacion)
    else:
        Contendiente=Funciones.regresa_Mejor_generacion(muta,num_poblacion)
        if(Contendiente[1]<Mejor_resultado[1]):
            Mejor_resultado=Contendiente
        
    #------------------------------------------------------------------------

    #Evaluamos P(t)
    b=Funciones.aptitud(muta,num_poblacion)
    #print("Aptitudes\n",len(b))
    #Funciones.Mostrar_arreglo(b)
    #-------------------

print("El mejor resultado es: \n",Mejor_resultado[1],"\nCon coordenadas \n",Mejor_resultado[0])