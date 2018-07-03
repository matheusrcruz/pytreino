#if (True) se for verdadeiro
#else (se não)
#elif(faça isso)
"""
a = 10
if(a==10):
    print("o valor é igual a 10")
"""

acao = int(input("digite '1' para sim e '2' para não "))
if(acao==1):
    print("voce disse sim!")
else:
    if(acao==2):
        print("voce disse não!!!")
    else:
        print("Erro o numero que voce digitou é invalido certifique-se que voce digitou 1 ou 2 ")
