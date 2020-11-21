import random
import numpy as np
import math
import sys 

class Funciones:

    def Mostrar(matriz):
        #print("La matriz es la siguiente:")
        for fila in matriz:
            for valor in fila:
                print("\t", valor, end=" ")
            print()
    
    def Mostrar_arreglo(arreglo):
        #print("La matriz es la siguiente:")
        for fila in arreglo:
            print("\t", fila, end=" ")
            print()    

    def binarizar(decimal):
        binario = ''
        while decimal // 2 != 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        return str(decimal) + binario

    #Funcion que devuelve una lista de randoms diferentes entre si, recibe m ya que esta definido por el ciclo
    def unico(m,num_poblacion):
        L=[m] #este es L[0]
        i=1
        while i<4:
            x=random.randint(0,num_poblacion-1)
            for j in range(0, len(L)):
                if L[j]==x:
                    break
            else:
                L.append(x)
                i+=1
        return L
    #--------------------------------------------------------------

    #--------------------------------------------------------------

    def creacion_de_poblacion(num_poblacion,num_variables,lim_inf,lim_sup):
        poblacion = []
        for i in range(num_poblacion):
            poblacion.append([(int(bin(random.randint(2**17,2**18))[2:]) ),(int(bin(random.randint(2**17,2**18))[2:]) )])
        return poblacion
    #--------------------------------------------------------------

    #--------------------------------------------------------------

    def aptitud(poblacion,num_poblacion):
        aptitud_pobla=[]
        #print("\tx\t\t\ty")
        for i in range(num_poblacion):
            #funcion = -()
            a=int(str(poblacion[i][0]), 2)
            b=int(str(poblacion[i][1]), 2)

            x=-100+a*(100-(-100))/((2**18)-1) #El original es a 18
            y=-100+b*(100-(-100))/((2**18)-1) #El original es a 18
            #print("[",x,"\t",y,"]")
            
            funcion = 1/(1+(-(math.cos(x))*math.cos(y)*math.exp(-(math.pow((x-math.pi),2))-(math.pow((y-math.pi),2))))) #Funcion de aptitud

            aptitud_pobla.append(funcion)
        return aptitud_pobla
    #--------------------------------------------------------------


    def nex_generacion(aptitudes,modo,poblacion,num_poblacion):
        elegidos = []
        
        if modo == "Ruleta":
            probabilidad_indiv = []
            probabilidad_acom = []
            ruleta = []
            promedio = sum(aptitudes)
            for i in range(num_poblacion):
                probabilidad = aptitudes[i] / promedio
                ruleta.append(random.uniform(0, 1))
                probabilidad_indiv.append(probabilidad)
                if i == 0:
                    probabilidad_acom.append(probabilidad)
                else:

                    probabilidad_acom.append(probabilidad + probabilidad_acom[i-1])
            for j in range(num_poblacion):
                for l in range(num_poblacion):
                    if ruleta[j] < probabilidad_acom[l]:
                        #print(l)
                        elegidos.append([poblacion[l][0],poblacion[l][1]])
                        break
            #print("Probabilidad individual: \n",probabilidad_indiv)
            #print("RULETA\n",ruleta)
            #print("Probabilidad Acomulada: \n", probabilidad_acom)
            #print("Los elegidos son : \n",elegidos)
            return elegidos
       
        if modo == "Torneo":
            for a in range(num_poblacion):
                L=Funciones.unico(a,num_poblacion)
                m=L[0]
                i=L[1]
                j=L[2]
                k=L[3]
                #Primer pelea de pareja
                if(aptitudes[m]<aptitudes[i]):
                    primer_Ganador= m
                else:
                    primer_Ganador=i
                #Segunda pelea
                if(aptitudes[j]<aptitudes[k]):
                    segundo_Ganador=j
                else:
                    segundo_Ganador=k
                #Pelea final
                if(aptitudes[primer_Ganador]<aptitudes[segundo_Ganador]):
                    ganador_final=primer_Ganador
                else:
                    ganador_final=segundo_Ganador
                elegidos.append([poblacion[ganador_final][0],poblacion[ganador_final][1]])
            return elegidos

    def cruza_Punto(elegidos,num_poblacion,pos_Elegido): #elegidos,poblacion
        cruzado = []
        x_elegido=str(elegidos[pos_Elegido][0])
        y_elegido=str(elegidos[pos_Elegido][1])
        r=random.randint(1,17) #Aleatorio original es 17
        aux=""
        aux=aux.replace("",x_elegido[r-1:len(x_elegido)])
        #print("aqui corto",r," ",pos_Elegido)
        #print("Aux",aux)
        #print(x_elegido)
        #print(y_elegido)
        x_elegido=x_elegido.replace(x_elegido[r-1:len(x_elegido)],y_elegido[r-1:len(x_elegido)])
        y_elegido=y_elegido.replace(y_elegido[r-1:len(x_elegido)],aux)
        cruzado.append(x_elegido)
        cruzado.append(y_elegido)
        #print(x_elegido)
        #print(y_elegido)
        #print(cruzado)
        return cruzado
    

    def cruza_Puntos(elegidos,num_poblacion,pos_Elegido):
        x_elegido=str(elegidos[pos_Elegido][0])
        y_elegido=str(elegidos[pos_Elegido][1])
        #print(x_elegido)
        #print(y_elegido)
        r1=random.randint(1,17) #Aleatorio original es 17
        r2=random.randint(1,17) #Aleatorio original es 17
        while(r1==r2):
            r2=random.randint(1,17)
            
        #print("aqui corto",r1," ",pos_Elegido)
        #print("aqui corto",r2," ",pos_Elegido)  
        if(r1>r2):
            aux=r2
            r2=r1
            r1=aux
        aux=x_elegido[r1:r2]
        x_elegido=x_elegido.replace(x_elegido[r1:r2],y_elegido[r1:r2])
        y_elegido=y_elegido.replace(y_elegido[r1:r2],aux)
        cruzado=[]
        cruzado.append(x_elegido)
        cruzado.append(y_elegido)
        #print(cruzado)
        return cruzado

    def cruzamiento(elegidos,num_poblacion,modo):
        probabilidad_cruza=0.5
        lista_cruzados=[]
        if(modo=="Punto"):
            for i in range(num_poblacion):
                if(random.uniform(0,1)<probabilidad_cruza):
                    cruzado=Funciones.cruza_Punto(elegidos,num_poblacion,i)
                    lista_cruzados.append(cruzado)
                else:
                    lista_cruzados.append([str(elegidos[i][0]),str(elegidos[i][1])])
            return lista_cruzados
        else:
            for i in range(num_poblacion):
                if(random.uniform(0,1)<probabilidad_cruza):
                    cruzado=Funciones.cruza_Puntos(elegidos,num_poblacion,i)
                    lista_cruzados.append(cruzado)
                else:
                    lista_cruzados.append([str(elegidos[i][0]),str(elegidos[i][1])])
            return lista_cruzados        
                
    def muta(lista_cruzados,num_poblacion,prob_muta):
        muta=[]
        for i in range(num_poblacion):
            r=random.uniform(0,1)
            #print("Random",r)
            if(r<prob_muta):
                #print("Muto")
                r_bit= random.randint(0,17) #Aqui modificar por su numero de bits
                x=list(lista_cruzados[i][0]) 
                #print("cadena separada por posiciones",x)
                #print("bit a modificar",r_bit)
                if(x[r_bit]=='1'):
                    x[r_bit]='0'
                else:
                    x[r_bit]='1'
                y=list(lista_cruzados[i][1])
               # print("cadena separada por posiciones",y)
               # print("bit a modificar",r_bit)
                if(y[r_bit]=='1'):
                    y[r_bit]='0'
                else:
                    y[r_bit]='1'
                #x=str(x)
                #y=str(y)
                muta.append(["".join(x),"".join(y)])
            else:
                #print("No muto :(")  
                x=lista_cruzados[i][0]
                y=lista_cruzados[i][1]
                muta.append([x, y])  
        return muta

    def regresa_Mejor_generacion(muta,num_poblacion):
        resultados=[]
        mejor_resultado=sys.maxsize
        x_mejor=0.0
        y_mejor=0.0
        for i in range(num_poblacion):     
            a=int(muta[i][0],2) 
            b=int(muta[i][1],2) 
            x=-100+a*(100-(-100))/((2**18)-1) #El original es a 18
            y=-100+b*(100-(-100))/((2**18)-1) #El original es a 18
            #print("variables antes de evaluar ",x,y)
            funcion = (-(math.cos(x))*math.cos(y)*math.exp(-(math.pow((x-math.pi),2))-(math.pow((y-math.pi),2))))
            #print("Valores de evaluar f(x)",funcion)
            if(funcion<mejor_resultado):
                mejor_resultado=funcion
                x_mejor=x
                y_mejor=y
        resultados.append([x_mejor,y_mejor])
        resultados.append(mejor_resultado)
        return resultados