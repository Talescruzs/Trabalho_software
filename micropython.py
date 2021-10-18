import time
import machine
import framebuf

class pomodoro(object):
    def __init__(self):
        self.patterns()
        self.estudar()
    def patterns(self):
        global scl
        global sda
        global i2c
        global fbuf
        global volta
        volta = 1
        scl = machine.Pin('X9')
        sda = machine.Pin('X10')
        i2c = machine.I2C(scl=scl, sda=sda)
        fbuf = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB, 64)
    def estudar(self):
        self.tela_estudo()
        time.sleep(1500)
        self.descansar()
    def descansar(self):
        self.tela_descanso()
        time.sleep(300)
        global volta
        volta+=1
        self.estudar()
    def tela_estudo(self):
        fbuf.fill(0)
        fbuf.text('WORK', 16, 3, 1)
        fbuf.text('TIME', 16, 12, 1)
        fbuf.text('VOLTA:%d'%volta, 0, 22, 1)
        return i2c.writeto(8, fbuf)
    def tela_descanso(self):
        fbuf.fill(1)
        fbuf.text('RELAX', 12, 3, 0)
        fbuf.text('TIME', 16, 12, 0)
        fbuf.text('VOLTA:%d'%volta, 0, 22, 0)
        return i2c.writeto(8,fbuf)

def main():
    timer=pomodoro()
    timer.__init__()


if __name__ == '__main__':
    main()
