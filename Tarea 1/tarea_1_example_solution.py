def count_char(cadena, caracter):
    """
    El código retona (Código, Cantidad).
    El codigo se le especifica al usuario, de la siguiente manera:

    0 -> Éxito
    -100 -> 'cadena' no es string
    -200 -> 'cadena' contiene caracteres no permitidos
    -300 -> 'caracter' no es un único carácter válido

    En caso que se de un código distinto a 0,
    se devuelve el parametro cantidad como NONE
    """
    # --- Verificación 1 ---
    # Esta función se encarga de verificar que la cadena sea un string
    if not isinstance(cadena, str):
        return (-100, None)
    # En caso que la cadena no sea un string se retorna error

    # --- Verificación 2 ---
    # Esta función se encarga de verificar que el parámetro cadena
    # contenga solamente caracteres alfanumericos
    if not cadena.isalnum():
        return (-200, None)
    # En caso que la cadena no esté conformada puramente por caracteres
    # alfanumericos se retorna un código de error

    # --- Verificación 3 ---
    # Esta línea cumple con dos condiciones distintas, la primera funcion
    # verifica que el parámetro caracter sea un string, la segunda función
    # se encarga de verificar que la longitud de caracted no sea mayor que 1
    if (
        not isinstance(caracter, str)
        or len(caracter) != 1
        or not caracter.isalnum()
    ):
        return (-300, None)
    # En caso de que no se cumplan las condiciones de tipo de dato y tamaño
    # se devuelve un codigo de error conforme a lo especificado anteriormente

    # --- Conteo ---
    # Cuenta la cantidad de veces que un caracter aparece en la cadena
    cantidad = cadena.count(caracter)
    # Retorna el código cero el cual especifica que se ejecutó con éxito
    return (0, cantidad)


def multiplo_2(base, multiplo):
    """
    El código retona (codigo, resultado).
    Los codigos de error se le especifican al usuario, de la siguiente manera:
    0 -> Éxito
    -400 -> 'base' o 'multiplo' no son enteros positivos
    -500 -> 'multiplo' no es uno de [1, 2, 4, 8, 16]
    En caso que se de un código distinto a 0,
    se devuelve el parametro cantidad como NONE
    """

    # --- Verificación 1 ---
    # Se verifica que ambos parametros de entrada sean datos de tipó integer,
    # además se verifica que estos sean enteros positivos.
    if (
        not (isinstance(base, int) and isinstance(multiplo, int))
        or base <= 0
        or multiplo <= 0
    ):
        return (-400, None)
    # En caso de que al menos uno de los parametros no sean enteros positivos
    # se devuelve un código de error confome a lo especificado anteriormente

    # --- Verificación 2 ---
    # Se verifica que multiplo sea 1, 2, 4, 8 o 16
    if multiplo not in [1, 2, 4, 8, 16]:
        return (-500, None)
    # En caso de que no lo sea, se devuelve un codigo de error

    # --- Cálculo sin suma, multiplicación o for ---
    """
    La multiplicación se va a hacer similar a
    multiplicar un numero binario por dos.
    Esto se logra trasladando en este caso la base un espacio a la derecha por
    cada 2 que ha en el multiplo.

    Esto se demuestra a continuación con la multiplicación 5*4:
    Como 4 es igual a 2^2, En otras palabra la multiplicación es 5*2*2,
    es decir el 5 se desplaza dos espacios.
    101 -> 5 en binario
    1010 -> 5 desplazado un espacio, es decir 5*2 o bien, 10
    10100 -> 5 desplazado dos espacios, es decir 5*2*2 o bien, 20
    """
    # Se crea un diccionario el cual va a definir la cantidad de espacios que
    # se desplazara la base, relativo al valor de múltiplo, este valor se
    # almacena bajo la variable shift_amount.
    shift_amount = {1: 0, 2: 1, 4: 2, 8: 3, 16: 4}[multiplo]
    # Se desplaza la base por la cantidad almacenada en shift_amount,
    # el resultado de la multiplicación se almacena en la variable resultado.
    resultado = base << shift_amount

    # --- Retorno ---
    return (0, resultado)
