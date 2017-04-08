fim=int(input("Digite o valor de n: "))
string = str(fim)
soma = 0
for ch in string:
    if ch.isdigit():
        soma += int(ch)
print(soma)  
