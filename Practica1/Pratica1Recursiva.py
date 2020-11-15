def LeeArchivo(Estados,Alfabeto,EI,EF,TablaTrans,nombreArchivo):
    print("Leer Archivo")
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
    if IndiceCadena>(len(Cadena)-1):
        if EA in EF:
            #print(Camino)
            CaminosValidos.append(Camino[::])
        return 
    else:
        c=Cadena[IndiceCadena]
        for f in TablaT:
            if c == f[1] and EA == f[0]:
                #print("======================================================================")
                #print("Estado actual:",str(EA)+"  caracter actual:"+c +"  Indice actual:"+str(IndiceCadena))
                #print("Usando transicion"+str(f))
                Camino[IndiceCadena]=f[0]+"-"+f[1]+"->"+f[2]
                ProcesaCadena(Cadena,Estados,Alfabeto,EI,EF,TablaT,f[2],Camino,IndiceCadena+1)

print("Programa AFN")#Titulo
#5 tupla de componentes de un AF
Estados = []
Alfabeto = []
EI = ""
EF = []
TablaTrans= []
#Leer Archivo
nombreArchivo="AF.txt"
Estados,Alfabeto,EI,EF,TablaTrans=LeeArchivo(Estados,Alfabeto,EI,EF,TablaTrans,nombreArchivo)
#ESTADO ACTUAL
EA = str(EI)
print("Estados:"+str(Estados))
print("Alfabeto:"+str(Alfabeto))
print("Estado inicial:"+EI)
print("Estado actual:"+EA)
print("Estados Finales:"+str(EF))
print("Tabla de transiciones"+str(TablaTrans))
#Lectura de cadena
print("Introduce una cadena")
Cadena=input()
print("Cadena:"+Cadena)
#print(len(Cadena))
CaminosValidos=[]
Camino=[None]*len(Cadena)
ProcesaCadena(Cadena,Estados,Alfabeto,EI,EF,TablaTrans,EA,Camino,0)
#FINAL ACEPTACION O RECHAZO DE CADENA
if len(CaminosValidos)>0:
    print(">>>>Cadena Aceptada<<<<")
    print("Caminos validos para la cadena :"+Cadena)
    for x in CaminosValidos:
        print(x)
else:
    print(">>>>Cadena Rechzada<<<<")