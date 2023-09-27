# UNITTEST ####################################################################

### Introdução ======================================================

"""
O que é unittest?

    Unittest é um módulo python que permite escrever test cases em classes.

Por que usar unittest em python?

    Unittest é uma ferramenta simples e eficiente para testar funções e métodos em python. É uma ferramenta que permite escrever testes automatizados de forma simples e rápida.

    Os testes são simples e estão descritos dentro de classes, facilitando a interpretação e manutenção dos testes.

    Além disso, em comparação ao doctest, o unittest permite testar funções de maneira mais completa devido aos tipos de assertivas disponíveis.

"""

### Como escrever test cases =========================================

"""
Qual a estrutura de um test case?

    class NOME DA CLASSE(unittest.TestCase):
    
        def setUpClass(cls):
            '''
            Método executado antes de todos os test cases.
            '''
            ...

        def setUp(self):
            '''
            Método executado antes de cada test case.
            '''
            ...

        def tearDown(self):
            '''
            Método executado depois de cada test case.
            '''
            ...

        def tearDownClass(cls):
            '''
            Método executado depois de todos os test cases.
            '''
            ...

        def test_NOME DO TEST CASE(self):
            '''
            DOCSTRING DO TEST CASE
            '''
            CORPO DO TEST CASE

Como escrever test cases para funções simples?

    Você pode levar com consideração as mesmas orientações do doctest.

    Porém, você pode utilizar mais de uma assertiva por test case, o que permite testar mais de um caso por test case.

    Além disso, você pode utilizar os métodos setUpClass e tearDownClass para definir o estado inicial e final de um conjunto de testes, além do setUp e tearDown para definir o estado inicial e final de cada teste.

"""

### Como executar test cases =========================================

"""
Como executar test cases usando o módulo unittest?

    import unittest

    unittest.main() # Executa todos os testes de um módulo

Como executar test cases pelo terminal?

    python -m unittest NOME_DO_ARQUIVO.py

"""

### Verbose ==========================================================

"""
Como executar test cases em modo verbose?

    Níveis de verbosidade do unittest:
    
        0 (quiet): você só recebe o número total de testes executados e o resultado final do teste.

        1 (default): Você recebe um "." para cada teste passado e um "F" para cada teste falhado, além do número total de testes executados e o resultado final do teste.

        2 (verbose): Você recebe a string de ajuda de cada teste e o resultado final do teste.

"""

### Como lidar com falhas ============================================

"""
Como as mensagens de erro são exibidas?

    As mensagens de erro são exibidas de forma clara e objetiva, indicando o nome do teste que falhou, o nome da classe e o nome do módulo.

    Contudo, pode ser útil aumentar a verbosidade do unittest para exibir mais informações e, assim, facilitar a interpretação dos erros que ocorreram nos testes que não passaram

"""

### Tópicos avançados ==========================================

"""
Como testar exceções?

    Você pode usar a diretiva assertRaises para indicar que uma exceção deve ser lançada durante a execução da função.

    Ex:
        def test_divide_by_zero(self):
            with self.assertRaises(ZeroDivisionError):
                divide(10, 0)

É possível testar a partir de um arquivo externo?

    Sim, você pode utilizar o método loadTestsFromModule para carregar os testes de um módulo externo.

    Ex:

        import unittest

        import test_module

        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_module)
        unittest.TextTestRunner().run(suite)


Diretivas do unittest:

    skip: ignora o teste
    skipIf: ignora o teste se a condição for verdadeira
    skipUnless: ignora o teste se a condição for falsa
    expectedFailure: marca o teste como falha esperada
    unexpectedSuccess: marca o teste como sucesso inesperado

    Ex:

        import unittest

        class Test(unittest.TestCase):
            @unittest.skip("demonstrating skipping")
            def test_nothing(self):
                self.fail("shouldn't happen")

            def test_something(self):
                self.assertEqual(1 + 1, 2)

        if __name__ == '__main__':
            unittest.main()
            
Como escrever test cases pra funções com input (funções interativas)?

    Você pode utilizar o método patch do módulo unittest.mock para simular a entrada do usuário. O método patch permite que você substitua temporariamente um objeto por outro durante a execução do teste.

    Ex:

        import unittest
        from unittest.mock import patch
        from minha_funcao import ler_numero

        class TestLerNumero(unittest.TestCase):
            @patch('builtins.input', side_effect=['10'])
            def test_ler_numero(self, mock_input):
                self.assertEqual(ler_numero(), 10)

    Neste exemplo, a função ler_numero lê um número inteiro do usuário e o retorna. O exemplo de teste usa o método patch para substituir temporariamente a função input pelo valor '10'. O método side_effect é usado para especificar uma lista de valores que serão retornados a cada vez que a função input for chamada.

    Ao executar o teste, o método patch substituirá temporariamente a função input pelo valor '10' e a função ler_numero será executada com a entrada simulada. O teste verificará se a saída da função corresponde à saída esperada.
"""
