#conding: -UTF8

"""""
 #bloco de instruções é definida pelo espaçamento
#a = 50 #variavel global podendo ser chamada de qualquer bloco
if(true):
 b = (50)#variavel local pertecente a este bloco de instrução
    if(false)#pertence ao bloco de instrução a cima.
print(b)#erro pq não pertence ao mesmo bloco de instrução
"""""

    #escopo global bloco de instruções local e global:
num1 = int(input("Digite um numero: "))
if(num1>10):
    print("O valor é maior que 10")
    if(num1>=15):
        print("O valor é maior que 10, mas é menor que 15")
    else:
        if(num1<=50):
            print("O valor é maior que 10 mas menor que 50")
else:
    if(num1>5):
        print("O numero é maior que 10 mas é menor que 5")
    if(num1==7):
        print("O valor é exatemente 7!")
else:
    print("O valor é menor que 5")