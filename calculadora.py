from PyQt5 import uic, QtWidgets
# Variáveis do sistema
num = ''
resultado = ''
ultima_operacao = ''
conta_realizada = ''
fim_calculo = False


def apaga_numero():
    global num
    num = ''
    calculadora.DisplayLCD.display(0)


def limpar_dados():
    global num, resultado, ultima_operacao, conta_realizada, fim_calculo
    num = ''
    resultado = ''
    ultima_operacao = ''
    conta_realizada = ''
    fim_calculo = False
    calculadora.Memoria.clear()
    calculadora.Memoria.addItem(conta_realizada)
    calculadora.DisplayLCD.display(0)


def adiciona_digito(digito):
    global num, fim_calculo
    if fim_calculo == True:
        limpar_dados()
    num += digito
    calculadora.DisplayLCD.display(float(num))
    print(f'num: {num}')


def adiciona_digito_zero():
    adiciona_digito('0')


def adiciona_digito_um():
    adiciona_digito('1')


def adiciona_digito_dois():
    adiciona_digito('2')


def adiciona_digito_tres():
    adiciona_digito('3')


def adiciona_digito_quatro():
    adiciona_digito('4')


def adiciona_digito_cinco():
    adiciona_digito('5')


def adiciona_digito_seis():
    adiciona_digito('6')


def adiciona_digito_sete():
    adiciona_digito('7')


def adiciona_digito_oito():
    adiciona_digito('8')


def adiciona_digito_nove():
    adiciona_digito('9')


def adiciona_virgula():
    adiciona_digito('.')


def operacao(tipo):
    global num, ultima_operacao, resultado, conta_realizada

    ultima_operacao = ''
    if tipo == 'soma':
        ultima_operacao += 'soma'
        conta_realizada += num + ' + '
    elif tipo == 'subtrai':
        ultima_operacao += 'subtrai'
        conta_realizada += num + ' - '
    elif tipo == 'multiplica':
        ultima_operacao += 'multiplica'
        conta_realizada += num + ' * '
    elif tipo == 'divide':
        ultima_operacao += 'divide'
        conta_realizada += num + ' / '

    calculadora.Memoria.clear()
    calculadora.Memoria.addItem(conta_realizada)

    if resultado == '':
        resultado = float(num)
    else:
        if tipo == 'soma':
            resultado += float(num)
        elif tipo == 'subtrai':
            resultado -= float(num)
        elif tipo == 'multiplica':
            resultado *= float(num)
        elif tipo == 'divide':
            try:
                resultado /= float(num)
            except ZeroDivisionError:
                # todo: Tratar a divisão por zero
                calculadora.DisplayLCD.display(0000)
                print('Divisão por zero')
    num = ''
    print(f'Resultado parcial: {resultado}')


def soma():
    operacao('soma')


def subtrai():
    operacao('subtrai')


def divide():
    operacao('divide')


def multiplica():
    operacao('multiplica')


def calcula():
    global ultima_operacao, conta_realizada, fim_calculo
    fim_calculo = True
    operacao(ultima_operacao)
    calculadora.Memoria.clear()
    conta_realizada = conta_realizada[:-2] + conta_realizada[(-2 + 1):]
    conta_realizada += f'= {resultado}'
    calculadora.Memoria.addItem(conta_realizada)
    calculadora.DisplayLCD.display(resultado)


def apaga_digito():
    global num
    if len(num) > 1:
        num = num[:-1]
        calculadora.DisplayLCD.display(float(num))
    else:
        num = '0'
        calculadora.DisplayLCD.display(float(num))


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
calculadora.show()
app.exec()
