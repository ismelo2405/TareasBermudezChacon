def multiplo_2(base, multiplo):
    """
    El código retona una tupla (codigo, resultado).
    Los codigos de error se le especifican al usuario, de la siguiente manera:
    0 -> Éxito
    1 -> 'base' o 'multiplo' no son enteros positivos
    2 -> 'multiplo' no es uno de [1, 2, 4, 8, 16]
    En caso que se de un código distinto a 0, se devuelve el parametro cantidad como NONE
    """

    # --- Verificación 1 ---
    if not (isinstance(base, int) and isinstance(multiplo, int)) or base <= 0 or multiplo <= 0:  # Se verifica que ambos parametros de entrada sean datos de tipó integer, además se verifica que estos sean enteros positivos.
        return (1, None)  # En caso de que al menos uno de los parametros no sean enteros positivos se devuelve un código de error confome a lo especificado anteriormente
    
    # --- Verificación 2 ---
    if multiplo not in [1, 2, 4, 8, 16]: # Se verifica que multiplo sea 1, 2, 4, 8 o 16
        return (2, None)  # En caso de que no lo sea, se devuelve un codigo de error conforme a lo establecido anteriormente

    # --- Cálculo sin suma, multiplicación o for ---
    """
    La multiplicación se va a hacer similar a multiplicar un numero binario por dos.
    Esto se logra trasladando en este caso la base un espacio a la derecha por cada 2 que ha en el multiplo,
    Esto se demuestra a continuación con la multiplicación 5*4:
    Como 4 es igual a 2^2, En otras palabra la multiplicación es 5*2*2, es decir el 5 se desplaza dos espacios.
    101 -> 5 en binario
    1010 -> 5 desplazado un espacio, es decir 5*2 o bien, 10
    10100 -> 5 desplazado dos espacios, es decir 5*2*2 o bien, 20
    """
    shift_amount = {1: 0, 2: 1, 4: 2, 8: 3, 16: 4}[multiplo]  # Se crea un diccionario el cual va a definir la cantidad de espacios que se va a desplazar la base relativo al valor de múltiplo, este valor se guarda bajo la variable shift_amount.
    resultado = base << shift_amount  # Se desplaza la base por la cantidad almacenada en shift_amount, el resultado de la multiplicación se almacena en la variable resultado.

    # --- Retorno ---
    return (0, resultado)


# Ejemplos de uso
print(" ------------------------------------------------------------ ")
print("|************************************************************|")
print("|************************************************************|")
print("|**************************Códigos:**************************|")
print("|*************************0 -> Éxito*************************|")
print("|*****1 --> 'base' o 'multiplo' no son enteros positivos*****|")
print("|*******2 --> 'multiplo' no es uno de [1, 2, 4, 8, 16]*******|")
print("|************************************************************|")
print("|************************************************************|")
print(" ------------------------------------------------------------ ")
print(multiplo_2(5, 4))     # (0, 20) -> Éxito
print(multiplo_2("5", 4))   # (1, None) -> no es entero positivo
print(multiplo_2(5, 3))     # (2, None) -> múltiplo no válido
