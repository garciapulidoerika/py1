contador = {}

class Archivo:

    def __init__(self):
        self.nombre = input('escriba el nombre del archivo sin ".txt": ')
        print('se creo un archivo')
        
    def buscar(self):
        print('buscando info en el archivo:', self.nombre,)

    def filtrar(self):
        print('filtrando las 10 palabras mas comunes en el archivo:', self.nombre,)
        try:
            texto = open(self.nombre +'.txt').read().replace('\n', '')
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


    def __del__(self):
        print('se actualizó y finalizó la información de:', self.nombre,)

archivo_1 = Archivo()
archivo_1.buscar()
archivo_1.filtrar()
