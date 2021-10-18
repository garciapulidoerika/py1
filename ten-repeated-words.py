doc = input('escriba el nombre del archivo sin ".txt": ')

contador = {}

def filterfile(texto):
    try:
        texto = open(doc+'.txt').read().replace('\n', '')
        palabras = texto.split()
        for palabra in palabras:
            contador[palabra] = contador.get(palabra, 0) +1

        palabras_por_valor = []

        for key, value in contador.items():
            conjunto = (value, key)
            palabras_por_valor.append(conjunto)  

        palabras_por_valor = sorted(palabras_por_valor, reverse=True)    

        for value, key in palabras_por_valor[:10]:
            print(key, value) 
     
    except FileNotFoundError:
        print('error')

filterfile(doc)
