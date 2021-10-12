import time

class pomodoro(object):
    def __init__(self):
        self.estudar() # chama o temporizador do estudo
    def estudar(self): # temporizador do estudo
        print('Vai estudar') # aparece oq tem que aparecer quando estiver na hr de estudar
        time.sleep(1500) # espera 25 minutos
        self.descansar() # chama o temporizador do descanso
    def descansar(self): # temporizador do descanso
        print('Vai descansar') # aparece oq tem que aparecer quando estiver na hr de descansar
        time.sleep(300) # espera 5 minutos
        self.estudar() # chama o temporizador do estudo
# e fechou o pastel do timer em looping, agr é só add a telinha do micropy falando os negocios :)

def main():
    #teste de uso que liga o temporizador, se tu tiver 30 minutos 
    # pra ver funcionando pode tentar mas confia que ta certo
    timer=pomodoro()
    timer.estudar()

if __name__ == '__main__':
    main()
