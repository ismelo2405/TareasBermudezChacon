def count_char(cadena, caracter):
    """
    El código retona una tupla (Código, Cantidad).
    El codigo se le especifica al usuario, de la siguiente manera:
    0 -> Éxito
    1 -> 'cadena' no es string
    2 -> 'cadena' contiene caracteres no permitidos
    3 -> 'caracter' no es un único carácter válido
    En caso que se de un código distinto a 0, se devuelve el parametro cantidad como NONE
    """
    # --- Verificación 1 ---
    if not isinstance(cadena, str):  #Esta función se encarga de verificar que la cadena sea un string
        return (1, None)  # En caso que la cadena no sea un string se retorna un código conforme al formato especificado anteriormente
    
    # --- Verificación 2 ---
    if not cadena.isalnum():  # Esta función se encarga de verificar que el parámetro cadena contenga solamente caracteres alfanumericos
        return (2, None)  # En caso que la cadena no esté conformada puramente por caracteres alfanumericos se retorna un código conforme al formato especificado anteriormente
    
    # --- Verificación 3 ---
    if not isinstance(caracter, str) or len(caracter) != 1 or not caracter.isalnum():  # Esta línea cumple con dos condiciones distintas, la primera funci´pon verifica que el parámetro caracter sea un string, la segunda función se encarga de verificar que la longitud de caracted no sea mayor que 1
        return (3, None)  # En caso de que no se cumplan las condiciones de tipo de dato y tamaño se devuelve un codigo de error conforme a lo especificado anteriormente
    
    # --- Conteo ---
    cantidad = cadena.count(caracter) # Cuenta la cantiddad de veces que el parametro caracter aparece en el parámetro cadena
    return (0, cantidad)  # Retorna el código cero el cual especifica que el codigo se corrió con exito.


# Ejemplos de uso
print(" ------------------------------------------------------------ ")
print("|************************************************************|")
print("|************************************************************|")
print("|**************************Códigos:**************************|")
print("|*************************0 -> Éxito*************************|")
print("|*****************1 -> 'cadena' no es string*****************|")
print("|******2 --> 'cadena' contiene caracteres no permitidos******|")
print("|*******3 -> 'caracter' no es un único carácter válido*******|")
print("|************************************************************|")
print("|************************************************************|")
print(" ------------------------------------------------------------ ")
print(count_char("Hola123", "1"))    # (0, 1) -> Éxito
print(count_char(12345, "1"))        # (1, None) -> 'cadena' no es string
print(count_char("Hola 123", "1"))   # (2, None) -> contiene espacio no permitido
print(count_char("Hola123", "12"))   # (3, None) -> carácter inválido
