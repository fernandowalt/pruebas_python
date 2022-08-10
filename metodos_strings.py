from unittest import result


mi_texto = "Esta es una prueba con textos"

print(mi_texto.index('e'))
print(mi_texto.rindex('e'))


palabra = "ordenador"
caracter = palabra[4]
print(caracter)

texto = "ABCDEFGHIJKLMNOPQ"
fragmento = texto[2:10:2]

print(fragmento)

frase = "Controlar la complejidad es la esencia de la programación"
print(frase[:9])

frase2 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"

print(frase2[8::3])

frase3 = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

print(frase3[::-1])

frase4 = "Este es el texto de Federico"

resultado = frase4

print(resultado[:4].upper())
print(resultado.lower())
print(resultado.split())
print(resultado.split('t'))
a = 'aprender'
b = 'python'
c = 'es'
d = 'genial'
e = '-'.join([a, b, c, d])
print(e)

print(frase3.find('o'))
print(frase4.replace('Federico', 'Walter'))
print(frase4.replace('e', 'x'))

frase55 = "Si la implementación es difícil de explicar, puede que sea una mala idea.".replace(
    'difícil', 'fácil').replace('mala', 'buena')

print(frase55)
