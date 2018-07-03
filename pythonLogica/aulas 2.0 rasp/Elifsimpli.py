#coding: -UTF8
idade = int(input("Digite sua idade: "))
if(idade<=0):
    print("Idade invalida!!!")
elif(idade<18):
    print("Você  não pode ter menos de 18 anos!!!")
elif(idade>150):
    print("Erro idade incompativel, maior que 150 anos !!!")
