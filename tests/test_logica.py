# tests/tests_logica.py
import unittest
import sys
import os

# Ajuste no caminho para que a pasta 'tests' consiga importar a pasta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logica import verificar_resposta, calcular_pontos

class TestesDoJogo(unittest.TestCase):

    def test_verificar_resposta_correta(self):
        """Verifica se o sistema ignora espaços extras e letras maiúsculas/minúsculas."""
        self.assertTrue(verificar_resposta("harry potter", "Harry Potter"))
        self.assertTrue(verificar_resposta("INTERSTELLAR", "Interstellar"))
        self.assertTrue(verificar_resposta(" cidade de deus ", "Cidade de Deus"))

    def test_verificar_resposta_incorreta(self):
        """Verifica se o sistema rejeita respostas totalmente erradas."""
        self.assertFalse(verificar_resposta("Avatar", "Matrix"))
        self.assertFalse(verificar_resposta("O Rei Leão", "It"))

    def test_calcular_pontos(self):
        """Verifica se a dedução de pontos por dicas solicitadas está correta."""
        # Nenhuma dica = 100 pontos
        self.assertEqual(calcular_pontos(0), 100)
        # 1 dica = 75 pontos
        self.assertEqual(calcular_pontos(1), 75)
        # 2 dicas = 50 pontos
        self.assertEqual(calcular_pontos(2), 50)
        # Garantir que não fica negativo (caso sejam pedidas mais de 4 dicas)
        self.assertEqual(calcular_pontos(5), 0)

if __name__ == '__main__':
    unittest.main()