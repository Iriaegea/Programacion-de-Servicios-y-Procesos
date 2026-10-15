
nombre_fichero = "aliases.txt"
alias = {} #eso es un map(diccionario en python)

with open(nombre_fichero, "r") as fichero:
    # for linea in fichero.readlines():
    #  k,v=linea.strip("\n").split("=") #la estrellita desempaqueta y lo guarda en los valores de la izda
    #  alias[k] = v
    alias = {k:v for k,v in list(map(lambda linea: linea.strip("\n").split("="),fichero.readlines()))}#strip elimina lo q le pases por paréntesis


respuesta = " "


print("Bienvenido al minishell: ")

while respuesta != "exit": 
    respuesta = input("> ")

    if respuesta != "exit":
        arrayRespuesta = respuesta.split(" ")

        comandoIntroducido = arrayRespuesta[0]
        argumentosIntroducidos = arrayRespuesta[1:]

       print(f"Ejecutando {alias.get(comandoIntroducido)} {' '.join(argumentosIntroducidos)}")


print("Has salido del minishell")

