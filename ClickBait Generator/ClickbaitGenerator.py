import random

pronombres =  ['El','Ella','Nosotros']
posesivo = ['Su','Nuestra','Las']
paises = ['Peru','Colombia','Mexico','Estados Unidos','Rusia','Brasil','China','Noruega','Panama','Argentina','Chile']
sustantivos = ['Perro','Gato','Videojuego','Doctores','Carros','Motos','Robot','Padres','Asesino Serial','Militar','Policias','Familia']
cuando = ['Pronto','Este Año','Mañana','AHORA','La Semana Que Viene']

def assasinsGenerator():
    sust = random.choices(sustantivos)[0]
    return f'La pandemia ha desatado una serie de asesinatos de {sust}'

def curiosidadGenerator():
    sust = random.choices(sustantivos)[0]
    pais = random.choices(paises)[0]
    return f'Oh! Mira como hacen {sust} en {pais} sorprendente!'

def noticiasEmpresasGenerator():
    pos = random.choices(posesivo)[0]
    pais = random.choices(paises)[0]
    sust = random.choices(sustantivos)[0]
    return f'Maravilloso, {pos} Empresa De {pais} Fabrican {sust} Muy Baratos'
    
def increiblesCosasGenerator():
    pais = random.choices(paises)[0]
    sust = random.choices(sustantivos)[0]
    return f'Wow Que Manera Tan Increible De Crear {sust} en {pais}'

def noQuieresSaberGenerator():
    pais = random.choices(paises)[0]
    sust = random.choices(sustantivos)[0]
    return f'Que Horrible!! Como acaban con {sust} en {pais}, no puede ser!!!'

def ideaRegalosGenerator():
    sust = random.choices(sustantivos)[0]
    return f'OMG! Que Ideas Tan Geniales Par Hacer {sust} Y Dar De Regalo'


def main():
    print('ClickBait Generator')

    while (True):
        print('Introduzca la cantidad de headline a generar : ')
        cantidad = input('>> ')
        if not cantidad.isdecimal():
            print('Debe de ser un numero Entero...')
        else:
            numHeadline = int(cantidad)
            break

    for i in range(numHeadline):
        tipo = random.randint(1,6)
        if tipo == 1 :
            headline = assasinsGenerator() 
        elif tipo == 2 :
            headline = curiosidadGenerator() 
        elif tipo == 3 :
            headline = noticiasEmpresasGenerator() 
        elif tipo == 4 :
            headline = increiblesCosasGenerator() 
        elif tipo == 5 :
            headline = noQuieresSaberGenerator() 
        elif tipo == 6 :
            headline = ideaRegalosGenerator() 

        print('\n')
        print(headline)

        website = random.choice(['Website','Blog','FaceBook','Twitter','Instagram','Google','Quora'])
        when = random.choice(cuando)
        print(f'Debes publicar este titulo en {website}{when}')

if __name__ == '__main__':
    main()