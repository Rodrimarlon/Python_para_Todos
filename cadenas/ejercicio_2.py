def cuenta(palabra, letra):
    contador = 0
    for caracter in palabra:
        if caracter == letra:
            contador = contador + 1
    print(contador)

cuenta('holaaaa', 'a')