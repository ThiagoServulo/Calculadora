from PyQt5 import uic, QtWidgets

# Variáveis Globais
num = ''
resultado = ''
ultima_operacao = ''
conta_realizada = ''
fim_calculo = False


def apaga_numero():
    """
    Apaga a variável número e mostra no display o valor zero
    :return: Nenhum
    """
    global num
    num = ''
    calculadora.DisplayLCD.display(0)


def limpar_dados(flag_zera_resultado):
    """
    Apaga todas as variáveis do sistema, além de limpar o bloco de memória e mostrar no display o valor zero
    :param flag_zera_resultado: Se verdadeira a variável 'resultado' será zerada
                                Se falso o valor da variável 'resultado' será mantido
    :return: Nenhum
    """
    global num, resultado, ultima_operacao, conta_realizada, fim_calculo
    print(f'Limpando dados: {flag_zera_resultado}')
    num = ''
    if flag_zera_resultado:
        resultado = ''
    ultima_operacao = ''
    conta_realizada = ''
    fim_calculo = False
    calculadora.Memoria.clear()
    calculadora.Memoria.addItem(conta_realizada)
    calculadora.DisplayLCD.display(0)


def adiciona_digito(digito):
    """
    Adiciona o digito informado a variavel global 'num', que contém o número que será usado na conta, e atualiza
    o display da calculadora com esse número
    :param digito: Dígito que será adicionado
    :return: Nenhum
    """
    global num, fim_calculo
    if fim_calculo:
        limpar_dados(True)
    num += digito
    calculadora.DisplayLCD.display(float(num))
    print(f'num: {num}')


def adiciona_digito_zero():
    """
    Adiciona o dígito 0 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('0')


def adiciona_digito_um():
    """
    Adiciona o dígito 1 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('1')


def adiciona_digito_dois():
    """
    Adiciona o dígito 2 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('2')


def adiciona_digito_tres():
    """
    Adiciona o dígito 3 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('3')


def adiciona_digito_quatro():
    """
    Adiciona o dígito 4 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('4')


def adiciona_digito_cinco():
    """
    Adiciona o dígito 5 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('5')


def adiciona_digito_seis():
    """
    Adiciona o dígito 6 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('6')


def adiciona_digito_sete():
    """
    Adiciona o dígito 7 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('7')


def adiciona_digito_oito():
    """
    Adiciona o dígito 8 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('8')


def adiciona_digito_nove():
    """
    Adiciona o dígito 9 a variável 'num'
    :return: Nenhum
    """
    adiciona_digito('9')


def adiciona_virgula():
    """
    Adiciona a vírgula a variável 'num'
    :return: Nenhum
    """
    global num
    if num == '':
        num = '0'
    adiciona_digito('.')


def operacao(tipo):
    """
    Realiza a operação informada
    :param tipo: Tipo de operação que será realizada
    :return: Nenhum
    """
    global num, ultima_operacao, resultado, conta_realizada, fim_calculo

    if num == '' and resultado == '':
        return

    if fim_calculo:
        limpar_dados(False)
        num = str(resultado)
        resultado = ''

    if resultado == '' or resultado == 'ERRO':
        resultado = float(num)
    else:
        if ultima_operacao == 'soma':
            resultado += float(num)
        elif ultima_operacao == 'subtrai':
            resultado -= float(num)
        elif ultima_operacao == 'multiplica':
            resultado *= float(num)
        elif ultima_operacao == 'divide':
            try:
                resultado = resultado / float(num)
            except ZeroDivisionError:
                resultado = 'ERRO'
                num = ''
                print('Divisão por zero')

    ultima_operacao = ''
    if tipo == 'soma':
        ultima_operacao += 'soma'
        conta_realizada += f'{resultado} + '
    elif tipo == 'subtrai':
        ultima_operacao += 'subtrai'
        conta_realizada += f'{resultado} - '
    elif tipo == 'multiplica':
        ultima_operacao += 'multiplica'
        conta_realizada += f'{resultado} * '
    elif tipo == 'divide':
        ultima_operacao += 'divide'
        conta_realizada += f'{resultado} / '

    calculadora.Memoria.clear()
    calculadora.Memoria.addItem(conta_realizada)
    conta_realizada = ''

    num = ''
    print(f'Resultado parcial: {resultado} {ultima_operacao}')


def soma():
    """
    Seleciona a operação de soma
    :return: Nenhum
    """
    operacao('soma')


def subtrai():
    """
    Seleciona a operação de subtração
    :return: Nenhum
    """
    operacao('subtrai')


def divide():
    """
    Seleciona a operação de divisão
    :return: Nenhum
    """
    operacao('divide')


def multiplica():
    """
    Seleciona a operação de multiplicação
    :return: Nenhum
    """
    operacao('multiplica')


def calcula():
    """
    Calcula o resultado da operação e atualiza o display e a memória coma resposta
    :return: Nenhum
    """
    global ultima_operacao, conta_realizada, fim_calculo

    if num == '':
        return

    operacao(ultima_operacao)
    fim_calculo = True
    calculadora.Memoria.clear()
    conta_realizada = conta_realizada[:-2] + conta_realizada[(-2 + 1):]
    conta_realizada += f'= {resultado}'
    calculadora.Memoria.addItem(conta_realizada)
    calculadora.DisplayLCD.display(resultado)


def apaga_digito():
    """
    Apaga o ultimo dígito do número. Nessa função já ocorre a tratativa caso o último digito seja uma vírgula ou
    um zero pós a vírgula
    :return: Nenhum
    """
    global num
    while True:
        if len(num) > 1:
            if num[-1:-2:-1] == '.' or (num[-1:-2:-1] == '0' and '.' in num):
                num = num[:-1]
            else:
                num = num[:-1]
                calculadora.DisplayLCD.display(float(num))
                break
        else:
            num = ''
            calculadora.DisplayLCD.display(0)
            break


def inverte_numero():
    """
    Inverte o número (num = 1/num)
    :return: Nenhum
    """
    global num, fim_calculo, resultado, conta_realizada

    if fim_calculo or ultima_operacao == '':
        limpar_dados(False)
        print(f'Resultado {resultado}')
        num = str(resultado)
        calculadora.Memoria.clear()

    try:
        aux = 1 / float(num)
        num = str(aux)
        if fim_calculo or ultima_operacao == '':
            resultado = float(num)
    except ZeroDivisionError:
        num = ''
        calculadora.DisplayLCD.display(0)
        return
    except TypeError:
        num = ''
        calculadora.DisplayLCD.display(0)
        return
    except ValueError:
        num = ''
        calculadora.DisplayLCD.display(0)
        return

    calculadora.DisplayLCD.display(float(num))
    print(f'Fração: {num}')


# Main
# Inicia a aplicação
app = QtWidgets.QApplication([])
# Carrega o layout da tela
calculadora = uic.loadUi("calculadora.ui")
calculadora.Digito0.clicked.connect(adiciona_digito_zero)
calculadora.Digito1.clicked.connect(adiciona_digito_um)
calculadora.Digito2.clicked.connect(adiciona_digito_dois)
calculadora.Digito3.clicked.connect(adiciona_digito_tres)
calculadora.Digito4.clicked.connect(adiciona_digito_quatro)
calculadora.Digito5.clicked.connect(adiciona_digito_cinco)
calculadora.Digito6.clicked.connect(adiciona_digito_seis)
calculadora.Digito7.clicked.connect(adiciona_digito_sete)
calculadora.Digito8.clicked.connect(adiciona_digito_oito)
calculadora.Digito9.clicked.connect(adiciona_digito_nove)
calculadora.Virgula.clicked.connect(adiciona_virgula)
calculadora.Somar.clicked.connect(soma)
calculadora.Subtrair.clicked.connect(subtrai)
calculadora.Dividir.clicked.connect(divide)
calculadora.Multiplicar.clicked.connect(multiplica)
calculadora.Calcular.clicked.connect(calcula)
calculadora.Apaga_Digito.clicked.connect(apaga_digito)
calculadora.Apagar_Tudo.clicked.connect(limpar_dados)
calculadora.Apagar_Numero.clicked.connect(apaga_numero)
calculadora.Fracao.clicked.connect(inverte_numero)
calculadora.show()
app.exec()
