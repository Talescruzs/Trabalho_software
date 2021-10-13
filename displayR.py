import machine
import framebuf

scl = machine.Pin('X9')
sda = machine.Pin('X10')
i2c = machine.I2C(scl=scl, sda=sda)

fbuf = framebuf.FrameBuffer(bytearray(64 * 32 // 8), 64, 32, framebuf.MONO_HLSB)

fbuf.fill(1)

fbuf.text('relax', 11, 7, 0)
fbuf.text('time', 16, 17, 0)

i2c.writeto(8, fbuf)
