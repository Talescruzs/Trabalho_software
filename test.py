import unittest
import time
import machine
import framebuf
from inspect import signature
from micropython import pomodoro
from micropython import pomodoro as func


class testador_pomodoro(unittest.TestCase):
    def testa_timer(self):
        """
        Função para testar o temporizador do pomodoro.
        """

        params = signature(func).parameters
        self.assertEqual(len(params), 2, "A função deveria possuir 2 parâmetros, tempo de estudo e tempo de descanso")
        test1 = pomodoro(tempo_estudo=3, tempo_descanso=2)
        test2 = pomodoro(tempo_estudo=8, tempo_descanso=5)
        self.assertIsNotNone(test1.tela_estudo, "Alguma tela de estudo deve ser implementada")
        self.assertIsNotNone(test1.tela_descanso,"Alguma tela de descanso deve ser implementada")
        self.assertIsNotNone(test1.volta,"o numero de voltas deve ser implementado")
        self.assertEqual(test1.tempo_descanso, 2, "O temporizador de descanso não está implementado corretamente")
        self.assertEqual(test1.tempo_estudo, 3, "O temporizador de estudo não está implementado corretamente")
        self.assertEqual(test2.tempo_descanso, 5, "O temporizador de descanso não está implementado corretamente")
        self.assertEqual(test2.tempo_estudo, 8, "O temporizador de estudo não está implementado corretamente")

if __name__ == '__main__':
    unittest.main()