import time
import machine
import framebuf

scl = machine.Pin('X9')
sda = machine.Pin('X10')
i2c = machine.I2C(scl=scl, sda=sda)
fbuf = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)

class pomodoro(object):
    def __init__(self):
        self.estudar()
    def estudar(self):
        self.tela_estudo()
        time.sleep(1500)
        self.descansar()
    def descansar(self):
        self.tela_descanso()
        time.sleep(300)
        self.estudar()
    def tela_estudo(self):
        fbuf.fill(0)
        fbuf.text('WORK', 16, 7, 1)
        fbuf.text('TIME', 16, 17, 1)
        return i2c.writeto(8, fbuf)
    def tela_descanso(self):
        fbuf.fill(1)
        fbuf.text('RELAX', 12, 7, 0)
        fbuf.text('TIME', 16, 17, 0)
        return i2c.writeto(8,fbuf)

def main():
    timer=pomodoro()
    timer.__init__()


if __name__ == '__main__':
    main()
