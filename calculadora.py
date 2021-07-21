from PyQt5 import uic, QtWidgets
import math
num = num1 = num2 = operacao = historico = memoria = ultimo_resultado = ''
modo_calculadora = 'graus'


def adiciona_digito(digito):
    """
    Adiciona o digito informado a variavel global 'num', que contém o número que será usado na conta, e atualiza
    o display da calculadora com esse número
    :param digito: Dígito que será adicionado
    :return: Nenhum
    """
    global num
    num += digito

    if num == '00':
        num = '0'
    else:
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


def adiciona_pi():
    """
    Adiciona o valor de Pi a variável 'num'
    :return: Nenhum
    """
    global num
    num = ''
    adiciona_digito(str(round(math.pi, 8)))


def adiciona_virgula():
    """
    Adiciona a vírgula a variável 'num'
    :return: Nenhum
    """
    global num
    if '.' in num:
        return
    if num == '':
        num = '0'
    adiciona_digito('.')


def preenche_memoria(numero, operacao):
    """
    Preenche o número e a operação a ser realizada no campo de memória
    :param numero: Número a ser inserido
    :param operacao: Operação a ser inserida
    :return: Nenhum
    """
    global memoria
    memoria += str(numero)

    if operacao == 'soma':
        memoria += ' + '
    elif operacao == 'subtrai':
        memoria += ' - '
    elif operacao == 'multiplica':
        memoria += ' * '
    elif operacao == 'divide':
        memoria += ' / '
    elif operacao == 'potencia':
        memoria += ' ^ '

    calculadora.Memoria.clear()
    calculadora.Memoria.addItem(memoria)
    memoria = ''


def calcula(tipo):
    """
    Calcular a operação a ser realizada
    :param tipo: Tipo de operação que será realizada
    :return: Nenhum
    """
    global num, num1, num2, operacao, historico, ultimo_resultado

    if num == '':
        if ultimo_resultado != '':
            num1 = ultimo_resultado
            preenche_memoria(num1, tipo)
        else:
            preenche_memoria(num1, '')
        operacao = tipo
        return

    if num1 == '':
        ultimo_resultado = num1 = float(num) if float(num) % 1 != 0 else int(float(num))
        preenche_memoria(num1, tipo)
        historico = num
        num = ''
        operacao = tipo
        return

    num2 = float(num) if float(num) % 1 != 0 else int(float(num))
    if operacao == 'soma':
        historico += f' + {num2}'
        num1 = (num1 + num2) if (num1 + num2) % 1 != 0 else int(num1 + num2)
    elif operacao == 'subtrai':
        historico += f' - {num2}'
        num1 = (num1 - num2) if (num1 - num2) % 1 != 0 else int(num1 - num2)
    elif operacao == 'multiplica':
        historico += f' * {num2}'
        num1 = (num1 * num2) if (num1 * num2) % 1 != 0 else int(num1 * num2)
    elif operacao == 'divide':
        try:
            historico += f' / {num2}'
            num1 = (num1 / num2) if (num1 / num2) % 1 != 0 else int(num1 / num2)
        except ZeroDivisionError:
            num = num1 = num2 = operacao = historico = ultimo_resultado = ''
            preenche_memoria(num, '')
            print('Divisão por zero')
            calculadora.DisplayLCD.display('ERRO')
            return
    elif operacao == 'potencia':
        historico += f' ^ {num2}'
        num1 = num1 ** num2

    preenche_memoria(num1, tipo)

    if tipo == 'calcula':
        historico += f' = {num1}'
        try:
            with open('.\\historico.txt', 'a', encoding='utf8') as arquivo:
                arquivo.writelines(historico + '\n')
        except:
            pass
        historico = str(num1)
        ultimo_resultado = num1
        calculadora.DisplayLCD.display(num1)
        operacao = num1 = num2 = num = ''
    else:
        operacao = tipo
        num2 = num = ''
        calculadora.DisplayLCD.display(num1)


def soma():
    """
    Seleciona a operação de soma
    :return: Nenhum
    """
    calcula('soma')


def subtrai():
    """
    Seleciona a operação de subtração
    :return: Nenhum
    """
    calcula('subtrai')


def divide():
    """
    Seleciona a operação de divisão
    :return: Nenhum
    """
    calcula('divide')


def multiplica():
    """
    Seleciona a operação de multiplicação
    :return: Nenhum
    """
    calcula('multiplica')


def potenciacao():
    """
    Seleciona a operação de exponenciacao
    :return: Nenhum
    """
    calcula('potencia')


def calcula_resultado():
    """
    Seleciona a operação de multiplicação
    :return: Nenhum
    """
    calcula('calcula')


def funcao_trigonometrica(funcao):
    """
    Realiza uma operação trigonométrica desejada
    :param funcao: Operação a ser realizada (seno, cosseno ou tangente)
    :return: Nenhum
    """
    global modo_calculadora, num, ultimo_resultado

    if num == '':
        if ultimo_resultado != '':
            num = str(ultimo_resultado)
        else:
            return

    if modo_calculadora == 'radianos':
        num = str(funcao(float(num)))
    elif modo_calculadora == 'graus':
        num = str(funcao(math.radians(float(num))))
    calculadora.DisplayLCD.display(float(num))


def seno():
    """
    Calcula o seno de um ângulo
    :return: Nenhum
    """
    funcao_trigonometrica(math.sin)


def cosseno():
    """
    Calcula o cosseno de um ângulo
    :return: Nenhum
    """
    funcao_trigonometrica(math.cos)


def tangente():
    """
    Calcula a tangente de um ângulo
    :return: Nenhum
    """
    funcao_trigonometrica(math.tan)


def inverte_sinal():
    """
    Inverter o sinal da variável 'num'
    :return: Nenhum
    """
    global num, ultimo_resultado

    lista_num = list(num)
    if len(num) > 0 and num[0] != '-':
        lista_num.insert(0, '-')
        num = ''
        lista_num = ''.join(lista_num)
        adiciona_digito(lista_num)
    elif len(num) > 0 and num[0] == '-':
        lista_num.pop(0)
        num = ''
        lista_num = ''.join(lista_num)
        adiciona_digito(lista_num)
    else:
        if num == '':
            if ultimo_resultado != '':
                num = str(-1 * float(ultimo_resultado) if float(ultimo_resultado) % 1 != 0
                          else -1 * int(ultimo_resultado))
                calculadora.DisplayLCD.display(float(num))
                print(f'f{num}')
            else:
                num = ''
                adiciona_digito('-0')


def inverte_numero():
    """
    Inverte o número (num = 1/num)
    :return: Nenhum
    """
    global num, num1, num2, operacao, historico, ultimo_resultado

    if num == '':
        if ultimo_resultado != '':
            num = ultimo_resultado
        else:
            return
    try:
        num = str(1 / float(num))
        calculadora.DisplayLCD.display(float(num))
    except ValueError:
        try:
            num1 = 1 / num1
            num = str(num1)
            calculadora.DisplayLCD.display(float(num))
        except ZeroDivisionError:
            num = num1 = num2 = operacao = historico = ''
            preenche_memoria(num, '')
            print('Divisão por zero')
            calculadora.DisplayLCD.display('ERRO')
    except ZeroDivisionError:
        num = num1 = num2 = operacao = historico = ultimo_resultado = ''
        preenche_memoria(num, '')
        print('Divisão por zero')
        calculadora.DisplayLCD.display('ERRO')
        return


def apaga_digito():
    """
    Apaga o ultimo dígito do número. Nessa função já ocorre a tratativa caso o último digito seja uma vírgula ou
    um zero pós a vírgula
    :return: Nenhum
    """
    global num, num1, ultimo_resultado

    if num == '':
        if ultimo_resultado != '':
            num = str(float(ultimo_resultado) if float(ultimo_resultado) % 1 != 0 else int(float(ultimo_resultado)))
            print(f'f{num}')
        else:
            return

    lista_num = list(num)
    if len(num) == 1:
        num = '0'
    elif len(num) > 0:
        lista_num.pop(len(lista_num) - 1)
        print(lista_num)
        num = ''.join(lista_num)

    calculadora.DisplayLCD.display(float(num))


def apaga_numero():
    """
    Apaga a variável número e mostra no display o valor zero
    :return: Nenhum
    """
    global num
    num = ''
    calculadora.DisplayLCD.display(0)


def apaga_tudo():
    """
    Apaga/Zera todas as variáveis usadas
    :return: Nenhum
    """
    global num, num1, num2, operacao, historico, memoria, ultimo_resultado
    num = num1 = num2 = operacao = historico = memoria = ultimo_resultado = ''
    calculadora.Memoria.clear()
    calculadora.DisplayLCD.display(0)


def logaritmo():
    """
    Calcula o logaritmo do número informado
    :return: Nenhum
    """
    global num, historico, ultimo_resultado, num1, num2, operacao

    if num == '':
        if ultimo_resultado != '':
            num = str(ultimo_resultado)
        else:
            return

    try:
        num = str(math.log10(float(num)))
        calculadora.DisplayLCD.display(float(num))
    except ValueError:
        print('Erro ao calcular Logaritmo')
        num = num1 = num2 = operacao = historico = ultimo_resultado = ''
        preenche_memoria(num, '')
        calculadora.DisplayLCD.display('ERRO')


def mostra_tela_versao():
    """
    Mostra a tela 'Versão'
    :return: Nenhum
    """
    versao.show()


def mostra_tela_configurar():
    """
    Mostra a tela 'Configurar'
    :return: Nenhum
    """
    configurar.show()


def verificar_modo_calculadora():
    """
    Define se a calculadora irá considerar os ângulos em Graus ou Radianos
    :return: Nenhum
    """
    global modo_calculadora
    if configurar.Graus.isChecked():
        modo_calculadora = 'graus'
        calculadora.Modo_Calculadora.setText('G')
    elif configurar.Radianos.isChecked():
        modo_calculadora = 'radianos'
        calculadora.Modo_Calculadora.setText('R')
    configurar.close()


def apaga_historico():
    """
    Apaga o conteúdo do arquivo 'historico.txt'
    :return: Nenhum
    """
    try:
        with open('.\\historico.txt', 'w', encoding='utf8') as arquivo:
            arquivo.write('')
    except:
        pass


# Main
# Inicia a aplicação
app = QtWidgets.QApplication([])
# Carrega o layout da tela
calculadora = uic.loadUi("calculadora.ui")
versao = uic.loadUi("versao.ui")
configurar = uic.loadUi("configurar.ui")
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
calculadora.Pi.clicked.connect(adiciona_pi)
calculadora.Virgula.clicked.connect(adiciona_virgula)
calculadora.Somar.clicked.connect(soma)
calculadora.Subtrair.clicked.connect(subtrai)
calculadora.Dividir.clicked.connect(divide)
calculadora.Multiplicar.clicked.connect(multiplica)
calculadora.Calcular.clicked.connect(calcula_resultado)
calculadora.Inverter_sinal.clicked.connect(inverte_sinal)
calculadora.Fracao.clicked.connect(inverte_numero)
calculadora.Apaga_Digito.clicked.connect(apaga_digito)
calculadora.Apagar_Numero.clicked.connect(apaga_numero)
calculadora.Apagar_Tudo.clicked.connect(apaga_tudo)
calculadora.Logaritmo.clicked.connect(logaritmo)
calculadora.Elevado.clicked.connect(potenciacao)
calculadora.Seno.clicked.connect(seno)
calculadora.Cosseno.clicked.connect(cosseno)
calculadora.Tangente.clicked.connect(tangente)
calculadora.Versao.triggered.connect(mostra_tela_versao)
calculadora.Apagar_Historico.triggered.connect(apaga_historico)
calculadora.Configurar.triggered.connect(mostra_tela_configurar)
configurar.Confirmar.clicked.connect(verificar_modo_calculadora)
calculadora.show()
app.exec()
