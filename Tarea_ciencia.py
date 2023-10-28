#!/usr/bin/env python
# coding: utf-8

# ## Rango intercualtil

# In[1]:


def IQR(d):
    """
    Calcula el rango intercuartílico (IQR) de una lista de datos.
    Args:
    - d (list): Una lista de datos numéricos.
    Returns:
    - float: El valor del rango intercuartílico.

    El rango intercuartílico se calcula como la diferencia entre el tercer cuartil (Q3)
    y el primer cuartil (Q1) de los datos. Los cuartiles se calculan de la siguiente manera:
    1. Ordena la lista de datos de forma ascendente.
    2. Divide la lista en cuatro partes iguales (si el número de datos es divisible por 4) o
       en tres partes aproximadamente iguales (si no es divisible por 4).
    3. Calcula Q1 como la mediana de la primera mitad de datos y Q3 como la mediana de la última
       mitad de datos.
    4. El IQR es la diferencia entre Q3 y Q1.
    """
    n = len(d)
    d.sort()
    if n%4 == 0:
        es = n/4
        q1 = (d[es+1]+d[es])/2
        ter = es*3
        q3 = (d[ter+1]+d[ter])/2
        dq = q3-q1
    else:
        f = n//4
        a = f+1
        q1 = d[a]
        ra = a*3
        q3 = d[ra]
        dq = q3-q1
    return dq


# ## Percentiles

# In[11]:


def Percentil(n):
    """
    Calcula los cuartiles Q1 (25%) y Q3 (75%) de un conjunto de datos.

    Parámetros:
        data (list): Una lista de datos para los que se calcularán los cuartiles.

    Retorna:
        q1 (float): El cuartil Q1 (25%).
        q3 (float): El cuartil Q3 (75%).
    """
    n = len(d)
    d.sort()
    if n%4 == 0:
        es = n/4
        q1 = (d[es+1]+d[es])/2
        ter = es*3
        q3 = (d[ter+1]+d[ter])/2
    else:
        f = n//4
        a = f+1
        q1 = d[a]
        ra = a*3
        q3 = d[ra]
    return q1 , q3


# ## Varianza

# In[3]:


def Varianza(o):
    """
    Calcula la varianza de una lista de datos.
    
    Args:
    - o (list): Una lista de datos numéricos.
    
    Returns:
    - float: El valor de la varianza.
    
    La varianza se calcula como la media de los cuadrados de las diferencias entre cada dato
    y la media aritmética de los datos. El proceso para calcular la varianza se divide en los siguientes pasos:
    1. Calcula la media aritmética de los datos.
    2. Resta la media a cada dato, eleva al cuadrado el resultado y suma todos los cuadrados.
    3. Divide la suma de los cuadrados por el número de datos para obtener la varianza.
    """
    x = Promedio(o)
    n = len(o)
    suma = 0
    for k in o:
        r = (k-x)**2
        suma = suma + r
    var = suma/n
    return var


# ## Desviaciòn estandar

# In[ ]:


def Desviaciòn_est(u):
    """
    Calcula la desviación estándar de una lista de datos.

    Args:
    - u (list): Una lista de datos numéricos.

    Returns:
    - float: El valor de la desviación estándar.

    La desviación estándar se calcula como la raíz cuadrada de la varianza de los datos. Para ello, primero se
    calcula la varianza de los datos y luego se toma la raíz cuadrada del resultado.
    """
    desv = (Varianza(u))**(1/2)
    return desv


# ## Promedio

# In[6]:


def Promedio(x):
    """
    Calcula el promedio (media aritmética) de una lista de datos.

    Args:
    - x (list): Una lista de datos numéricos.

    Returns:
    - float: El valor del promedio.

    El promedio se calcula como la suma de todos los datos dividida por el número de datos en la lista.
    """
    n = len(x)
    prom = (sum(x)/n)
    return prom


# ## Mediana

# In[2]:


def mediana(g):
    """
    Calcula la mediana de una lista de datos.

    Args:
    - m (list): Una lista de datos numéricos.

    Returns:
    - float: El valor de la mediana.

    La mediana se calcula de la siguiente manera:
    1. Se ordena la lista de datos en orden ascendente.
    2. Si la lista tiene un número impar de elementos, la mediana es el valor en el centro.
    3. Si la lista tiene un número par de elementos, la mediana es el promedio de los dos valores en el centro.
    """
    n = len(g)

    if n % 2 != 0:
        return g[n // 2]
    else:
        c1 = g[(n - 1) // 2]
        c2 = g[n // 2]
        med = (c1 + c2) / 2         
    
            
    return med


# ## Moda

# In[ ]:


def moda(mm):
    """
    Calcula la moda de una lista de datos.

    Args:
    - mm (list): Una lista de datos numéricos.

    Returns:
    - int, list o None: La moda o una lista de modas si hay empate, o None si no hay moda.

    La moda es el valor que aparece con mayor frecuencia en la lista de datos. Si hay un empate en la frecuencia
    entre varios valores, la función devuelve una lista de esos valores.
    """
    if len(mm) == 0:
        return None  # Devuelve None si la lista está vacía.

    cuenta = {}  # Diccionario para almacenar las frecuencias de los elementos.
    
    # Contar las frecuencias de los elementos en la lista.
    for n in mm:
        if n in cuenta:
            cuenta[n] += 1
        else:
            cuenta[n] = 1

    # Encontrar el elemento con la frecuencia máxima.
    moda = None
    max_cuenta = 0
    for n, frec in cuenta.items():
        if frec > max_cuenta:
            moda = n
            max_cuenta = frec
        elif frec == max_cuenta and n != moda:
            # En caso de empate, si hay múltiples modas, devuelve una lista de las modas.
            if not isinstance(moda, list):
                moda = [moda]
            moda.append(n)
    
    if max_cuenta == 1:
        return None  # Si todas las frecuencias son 1, no hay moda.
    elif isinstance(moda, list):
        return moda
    else:
        return moda


# ## Rango

# In[ ]:


def rango(x):
    """
    Calcula el rango de una lista de datos.

    Args:
    - x (list): Una lista de datos numéricos.

    Returns:
    - int: El valor del rango.

    El rango se calcula como la diferencia entre el valor máximo y el valor mínimo en la lista de datos.
    """
    x.sort()
    ran = abs(x[-1]-x[0])
    return ran


# ## Desviaciòn mediana absoluta

# In[ ]:


def MAD(r):
    """
    Calcula la desviación media absoluta (MAD) de una lista de datos.

    Args:
    - r (list): Una lista de datos numéricos.

    Returns:
    - float: El valor de la MAD.

    La MAD se calcula de la siguiente manera:
    1. Calcula la media aritmética de los datos.
    2. Para cada dato en la lista, calcula la diferencia absoluta entre el dato y la media.
    3. Calcula la mediana de las diferencias absolutas.
    """
    r.sort()
    for w in r:
        u = []
        a = abs(w-(Promedio(r)))
        u.append(a)
    loco = mediana(u)
    return loco

