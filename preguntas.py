"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    
    cantidad= len(tbl0)
    print(cantidad)
    
    
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    return cantidad


def pregunta_02():
    import numpy as np
    lista =[]
    lista=tbl0.shape
    col=int(lista[1])
    print(col)
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    return col


def pregunta_03():
    numRegister=tbl0.groupby("_c1")["_c0"].count()
    print(numRegister)
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    return numRegister


def pregunta_04():    
    pom_letras=tbl0.groupby("_c1")["_c2"].mean()
    print(pom_letras)    
    
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    return pom_letras


def pregunta_05():
    max_letras=tbl0.groupby("_c1")["_c2"].max()
    print(max_letras)
    
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    return max_letras


def pregunta_06():
    regUnicos= tbl1["_c4"].unique().tolist()
    print(regUnicos)
    registros=[x.upper() for x  in regUnicos]
    registros=sorted(registros)
    print(sorted(registros))
    
    
    
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    return registros


def pregunta_07():
    sum_letras=tbl0.groupby("_c1")["_c2"].sum()
    print(sum_letras)
    
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    return sum_letras


def pregunta_08():
    tblResp=tbl0.copy()
    tblResp["suma"]= tblResp["_c0"]+tblResp["_c2"]
    print(tblResp)
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    return tblResp


def pregunta_09():
    tblResp=tbl0.copy()
    tblResp["year"]= [x[:4] for x in tblResp["_c3"]]
    print(tblResp)
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    return tblResp


def pregunta_10():
    
    
    DT0 =  tbl0.copy().sort_values(by="_c2")
    DT0["lista"] = DT0["_c2"].astype(str)
    DT0 = DT0.drop(["_c0","_c2","_c3"], axis=1).rename(columns={"_c1":"_c0"})

    #letras=pd.DataFrame()
    #letras.append(nueva_fila, ignore_index=True)
    letras = DT0[["_c0"]]
    letras = letras["_c0"].astype(str).sort_values().drop_duplicates()

    numeros = []
    for i in letras:
        y = DT0[DT0["_c0"] == i] #todos los resultados donde aparezca la i
        z = y["lista"].values.tolist()       
        z = ':'.join(z)
        #z=z.sort_values
    
        numeros.append(z)

    letras = letras.values.tolist()

    print(letras)
    print("")
    print(numeros)
    DT0 = pd.DataFrame({' ':letras,'_c1':numeros})
    nueva_fila={"_c0": " " ,"_c1":""}
    
    
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    return nueva_fila


def pregunta_11():
    DT1 = tbl1.copy().sort_values(by="_c4")
    DT1["lista"] = DT1["_c4"].astype(str)
    DT1 = DT1.drop("_c4", axis=1)


    numeros = DT1[["_c0"]]
    numeros = numeros["_c0"].sort_values().drop_duplicates()

    letras = []
    for i in numeros:
        y = DT1[DT1["_c0"] == i]
        z = y["lista"].tolist()
        z = ','.join(z)
    
        letras.append(z)

    letras

    numeros = numeros.values.tolist()
    DT1 = pd.DataFrame({'_c0':numeros,'_c4':letras})
    print(DT1)
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    return DT1


def pregunta_12():
    DT2 = tbl2.copy()
    DT2["_c5b"] =DT2["_c5b"].astype(str)
    DT2["lista"] = (DT2["_c5a"] + ":" + DT2["_c5b"]).astype(str)
    DT2 = DT2.sort_values(by="_c5a")
    DT2 = DT2.drop(["_c5a","_c5b"], axis=1)

    numeros = DT2[["_c0"]]
    numeros = numeros["_c0"].sort_values().drop_duplicates()

    letras = []
    for i in numeros:
        y = DT2[DT2["_c0"] == i]
        z = y["lista"].tolist()
        z = ','.join(z)
        
        letras.append(z)

    letras

    numeros = numeros.values.tolist()
    DT2 = pd.DataFrame({'_c0':numeros,'_c5':letras})
    print(DT2)    
    
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    return DT2


def pregunta_13():
    Data2_0 = pd.merge(tbl2,tbl0)
    suma_c5b = Data2_0.groupby("_c1")["_c5b"].sum()
    print(suma_c5b)
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    return suma_c5b
