from draw3ratllaAlumnes import draw

def imprimeixllistaJugadors():
    print("Hola")
    #Fer diccionari

def escullJugador():
    print("Escull el jugador que comença ")
    print("1. Jugador")
    print("2. Màquina")
    print("3. Aleatori")
    jug=input("Opció: ")
    while jug!="1" and jug!="2" and jug!="3":
         jug=input("Opció: ")
    return jug


if __name__=="__main__":
    volsFer=input("Vols fer una partida? (S/N): ")
    while volsFer!="S" and volsFer!="N":
         volsFer=input("Vols fer una partida? (S/N): ")
    if volsFer=="S":
        imprimeixllistaJugadors()
        nom=input("Introdueix el teu nom: ")

        metodeJoc=input("Aleatòria o Intel·ligent (A/I): ")
        while metodeJoc!="A" and metodeJoc!="I":
            metodeJoc=input("Aleatòria o Intel·ligent (A/I): ")

        iniciador=escullJugador()
        print("HOLA ALBERT")
        
        


