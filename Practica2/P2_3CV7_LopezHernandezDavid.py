def LeeArchivo(Estados,Alfabeto,EI,EF,TablaTrans,nombreArchivo):
    with open(nombreArchivo) as fname:
        LineasArchivo = [i.strip('\n') for i in fname.readlines()]        #Separa el archivo de entrada por lineas
        Estados=LineasArchivo[0].split(',')#Estados
        Alfabeto=LineasArchivo[1].split(',')#Alfabeto
        EI=str(LineasArchivo[2])#Estado Inicial
        EF=LineasArchivo[3].split(',')#Estados Finales
        for x in range(4, len(LineasArchivo), 1):#Transiciones
            temp=[LineasArchivo[x]]
            TablaTrans.append(temp[0].split(','))
    return Estados,Alfabeto,EI,EF,TablaTrans

def ProcesaCadena(Cadena,Estados,Alfabeto,EI,EF,TablaT,EA,Camino,IndiceCadena):
    global CaminosValidos
    bandera = False
    if IndiceCadena>(len(Cadena)-1) and (EA in EF):#si ya se recorrio la cadena y ademas el estado actual es de aceptacion , lo agrega a un camino valido
        CaminosValidos.append(Camino[::])
    else:
        if IndiceCadena < len(Cadena):#si es un caracter toma el indice valido
            c=Cadena[IndiceCadena]
        else:#cuando ya acabo la cadena pero no necesariamente es estado de aceptaciones , sigue buscando transiciones via epsilon por lo que asignamos none al valor del caracter
            c=None
        for f in TablaT:
            if bandera:#esta bandera esta para borrar el ultimo elemento de un camino almacenado ya que si recorrio el for agrego un camino en la primera iteracion por ejemplo y para la segunda tiene que borrar ese ultimo elemento , esto no afecta la funcion ya que mandamos una copia de la lista , no  la misma lista
                Camino.pop()
                bandera=False
            if (c == f[1] and EA == f[0]) or ("E" == f[1] and EA == f[0]):  #agrega transiciones epsilon
                Camino.append(f[0]+"-"+f[1]+"->"+f[2])
                print(f[0]+"-"+f[1]+"->"+f[2])
                bandera = True
                if("E" == f[1]):#busca los caminos pa la transicion epsilon
                    ProcesaCadena(Cadena,Estados,Alfabeto,EI,EF,TablaT,f[2],Camino[::],IndiceCadena)
                else:
                    ProcesaCadena(Cadena,Estados,Alfabeto,EI,EF,TablaT,f[2],Camino[::],IndiceCadena+1)

print(">>>>>>>>>>>>>>>>>>>Programa AFN<<<<<<<<<<<<<<<<<<<")#Titulo
#5 tupla de componentes de un AF
Estados = []
Alfabeto = []
EI = ""
EF = []
TablaTrans= []
CaminosValidos=[]#Almacenara los caminos
#Leer Archivo
nombreArchivo="AF.txt"
Estados,Alfabeto,EI,EF,TablaTrans=LeeArchivo(Estados,Alfabeto,EI,EF,TablaTrans,nombreArchivo)#Manda a leer el archivo
EA = str(EI)#ESTADO ACTUAL
print("Estados:"+str(Estados))
print("Alfabeto:"+str(Alfabeto))
print("Estado inicial:"+EI)
print("Estados Finales:"+str(EF))
print("Tabla de transiciones")
for x in TablaTrans:
    print("\t"+str(x))
#Lectura de cadena
print("Introduce una cadena")
Cadena=input()
print("Cadena:"+Cadena)
#Camino=[None]*len(Cadena)
Camino=[]
ProcesaCadena(Cadena,Estados,Alfabeto,EI,EF,TablaTrans,EA,Camino[::],0)
#FINAL ACEPTACION O RECHAZO DE CADENA
if len(CaminosValidos)>0:
    print(">>>>Cadena Aceptada<<<<")
    print("Caminos validos para la cadena :"+Cadena)
    for x in CaminosValidos:
        print(x)
else:
    print(">>>>Cadena Rechzada<<<<")