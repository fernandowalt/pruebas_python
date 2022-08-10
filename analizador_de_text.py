texto = input('ingresa un text: ').lower().strip().strip('.')
letra_1 = input('ingresa la primera letra: ').lower()
letra_2 = input('ingresa la segunda letra: ').lower()
letra_3 = input('ingresa la tercera letra: ').lower()

palabras = len(texto.split())

lista_texto = list(texto)
lista_texto.reverse()

si_o_no = "si" if 'python' in texto else "no"

print(f""" 
 el texto: "{texto}"

 tinen {palabras} palabras
 tiene {texto.count(letra_1)} {letra_1}(s)
 tiene {texto.count(letra_2)} {letra_2}(s)
 tiene {texto.count(letra_3)} {letra_3}(s)

 la primera letra del texto es una {texto[0]}
 la ultima letra es una {texto[-1]}

 el texto invertido luce de la siguinte manera: "{"".join(lista_texto)}"

 la palabra python {si_o_no} se encuentra en el texto.
""")
