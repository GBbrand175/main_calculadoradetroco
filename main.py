#layout
#print("-"*41)
#print("-"*10 + "calculadora de troco" + "-"*11)
#print("-"*41)
#variaveis
contador = 0
sair = str
while contador <= 9:
    print("-"*10 + "calculadora de troco" + "-"*10)
    recebido = float(str(input('Qual o valor recebido?')))
    valor_conta = float(str(input('Qual valor da conta?')))
    troco = recebido - valor_conta
    print('Repasse o Valor de:' +'R${:.2f}'.format(troco) )
    contador = contador + 1