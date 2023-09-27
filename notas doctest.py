# DOCTEST ###########################################################

### Introdução ======================================================

"""
O que é doctest?

    Doctest é um módulo python que permite escrever test cases dentro
    da docstring de uma função, método ou classe.

Por que usar doctest em python?

    Doctest é uma ferramenta simples e eficiente para testar funções
    e métodos em python. É uma ferramenta que permite escrever testes
    automatizados de forma simples e rápida.

    Os testes são simples e estão descritos junto da função, facilitando a interpretação e manutenção dos testes.

"""

### Como escrever test cases =========================================

"""
Qual a estrutura de um test case?

    def NOME DA FUNÇÃO(ARGUMENTOS):
        '''

        DOCSTRING DA FUNÇÃO

        TITULO...
        >>> CHAMADA DA FUNÇÃO(ARGUMENTOS DE TESTE)
        SAÍDA ESPERADA (CASO O TESTE PASSE)

        '''

        CORPO DA FUNÇÃO

        return SAÍDA DA FUNÇÃO


Como escrever test cases para funções simples?

    Primeiro, pense em casos em que a função deve funcionar corretamente e escreva testes para esses casos. Você pode utilizar esses casos como referência para desenvolver a sua função.

    Depois, pense em casos em que a função deve falhar e escreva testes para esses casos.
    Esses casos podem se basear em entradas inválidas ou em situações em que a função não deve funcionar corretamente (como divisão por zero).

    Um conjunto de test cases coerente deve cobrir todos os casos possíveis de uso da função. Além disso, todos os testes devem ser independentes, ou seja, a falha de um teste não deve afetar o resultado dos outros testes. Dado um conjunto de testes, é esperado que a função, quando bem implementada, passe em todos os testes (seja um teste de uma situação comum ou uma situação de contorno).
"""

### Como executar test cases =========================================

"""
Como executar test cases usando o módulo doctest?

    import doctest

    doctest.testmod() # Executa todos os testes de um módulo

Como executar test cases pelo terminal?

    python -m doctest NOME_DO_ARQUIVO.py

"""

### Verbose ==========================================================

"""
Como configurar a verbosidade do doctest?

    vebose = False
        Dessa forma, o doctest não exibirá os testes que passaram.

    verbose = True
        Dessa forma, o doctest exibirá também os testes que passaram.
"""

### Como lidar com falhas ============================================

"""
Como as mensagens de erro são exibidas?

    Quando um teste falha, o doctest exibe uma mensagem de erro que inclui o exemplo de teste que falhou, a saída esperada e a saída real. 

Como interpretar e corrigir falhas?

    Para interpretar a falha, você deve examinar cuidadosamente a mensagem de erro(observando a saída esperada e a saída real) e determinar por que elas são diferentes.

    Para corrigir uma falha, você pode alterar a implementação da função ou alterar o teste.

    Se o teste passar, você pode continuar a escrever mais testes para garantir que a função esteja funcionando corretamente em todas as situações.

"""

### Tópicos avançados ==============================================
"""
Como testar exceções?
    
    Você pode usar a diretiva raises para indicar que uma exceção deve ser lançada durante a execução da função.
    Ao executar o doctest, o teste com a diretiva raises verificará se a exceção esperada é lançada durante a execução da função.

    Ou você pode usar elipses (...) para ignorar a exceção (ou parte dela).

    Ex:
    def dividir(a, b):
        '''
        Retorna o resultado da divisão de a por b.

        Exemplo:
        >>> dividir(10, 2)
        5.0
        >>> dividir(10, 0)  # doctest: +raises ZeroDivisionError
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
        '''
        return a / b


Como descrever um testfile?

    Basta criar um arquivo de texto com a extensão .txt e escrever os testes (test cases) dentro dele. 

    Para executar test cases de um testfile, basta usar o comando:

    doctest.testfile("NOME DO ARQUIVO.txt")

    
SKIP e ELLIPISIS

    SKIP - Pula um teste
    Ao executar o doctest, o teste marcado com SKIP será pulado e não será considerado na verificação do resultado.
    Ex:
    def exemplo():
        '''
        >>> exemplo()
        Olá, meu nome é João e eu tenho 30 anos.
        >>> exemplo() #doctest: +SKIP
        Olá, meu nome é Maria e eu tenho 20 anos.
        '''
        return "Olá, meu nome é João e eu tenho 30 anos."


    ELLIPISIS - Ignora uma parte do resultado
    Para usar o doctest ELLIPSIS, basta adicionar "..." na parte do resultado que você deseja ignorar.
    Ex:
    def exemplo():
        '''
        >>> exemplo()
        Olá, meu nome é ... e eu tenho ... anos.
        '''
        return "Olá, meu nome é João e eu tenho 30 anos."


Como escrever test cases pra funções com input (funções interativas)?

    Para executar o doctest para funções com input, você pode usar a função DocTestRunner do módulo doctest. A função DocTestRunner permite que você forneça entradas para a função sendo testada e verifique se a saída corresponde à saída esperada.

    Ex:

    import doctest

    def ler_numero():
        '''
        Lê um número inteiro do usuário.

        Exemplo:
        >>> ler_numero()
        Digite um número inteiro: 10
        10
        '''
        num = int(input("Digite um número inteiro: "))
        return num

    runner = doctest.DocTestRunner()
    runner.run(ler_numero)
"""



