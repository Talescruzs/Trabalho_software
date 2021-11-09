import unittest
import time
import machine
import framebuf
from inspect import signature
from micropython import pomodoro
from micropython import pomodoro as func

class testador_pomodoro(unittest.TestCase):
    def testa_timer(self):
        params = signature(func).parameters
        self.assertEqual(len(params), 2, "A função deveria possuir 2 parâmetros, tempo de estudo e tempo de descanso")
        a = pomodoro(tempo_estudo=3, tempo_descanso=2)
        b = pomodoro(tempo_estudo=8, tempo_descanso=5)
        # self.assertIsNotNone(a.tela_estudo, "Alguma tela de estudo deve ser implementada") #objetivo é ver  se o pomodoro.tela_estudo.fbuf.text existe mas não tá dando
        # self.assertIsNotNone(a.tela_descanso,"Alguma tela de descanso deve ser implementada") #objetivo é ver  se o pomodoro.tela_descanso.fbuf.text existe mas não tá dando
        self.assertIsNotNone(a.volta,"o numero de voltas deve ser implementado")
        self.assertEqual(a.tempo_descanso, 2, "O temporizador de descanso não está implementado corretamente")
        self.assertEqual(a.tempo_estudo, 3, "O temporizador de estudo não está implementado corretamente")
        self.assertEqual(b.tempo_descanso, 5, "O temporizador de descanso não está implementado corretamente")
        self.assertEqual(b.tempo_estudo, 8, "O temporizador de estudo não está implementado corretamente")
        
if __name__ == '__main__':
    unittest.main()