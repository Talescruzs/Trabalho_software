import time
import machine
import framebuf


class pomodoro(object):
    # em Java ou C++ os atributos ficariam contidos nessa área; porém como estamos em Python, eles são definidos no construtor

    def __init__(self, tempo_estudo, tempo_descanso):

        # diferente de Java ou C++, os atributos em Python são sempre definidos dentro do construtor

        self.tempo_estudo = tempo_estudo
        self.tempo_descanso = tempo_descanso

        # é no construtor também que nós "construímos" o objeto. Logo, se existem coisas a serem inicializadas, a hora
        # é agora!

        self.scl = machine.Pin('X9')
        self.sda = machine.Pin('X10')
        self.i2c = machine.I2C(scl=self.scl, sda=self.sda)
        self.fbuf = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB, 64)
        self.volta = 1

    def inicia_estudos(self):
        self.estudar()

    def estudar(self):
        self.tela_estudo()
        time.sleep(self.tempo_estudo)
        self.descansar()

    def descansar(self):
        self.tela_descanso()
        time.sleep(self.tempo_descanso)
        self.volta += 1
        self.estudar()

    def tela_estudo(self):
        self.fbuf.fill(0)
        self.fbuf.text('WORK', 16, 3, 1)
        self.fbuf.text('TIME', 16, 12, 1)
        self.fbuf.text('VOLTA:%d' % self.volta, 0, 22, 1)
        self.i2c.writeto(8, self.fbuf)

    def tela_descanso(self):
        self.fbuf.fill(1)
        self.fbuf.text('RELAX', 12, 3, 0)
        self.fbuf.text('TIME', 16, 12, 0)
        self.fbuf.text('VOLTA:%d' % self.volta, 0, 22, 0)
        self.i2c.writeto(8, self.fbuf)


def main():
    timer = pomodoro(tempo_estudo=5, tempo_descanso=3)
    # timer.__init__()  # desnecessário: quando fazemos pomodoro(), ele já chama automaticamente o __init__ da classe
    timer.inicia_estudos()


if __name__ == '__main__':
    main()
