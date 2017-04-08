def éPrimo(num):
    divisores = 0
    i = 1
    while i <= num:
        if num % i == 0 :
            divisores = divisores + 1
        i = i + 1
    if divisores == 2:
         return True
    else:
        return False
def maior_primo(x):
        if x < 2:
            print("O número digitado deve ser maior ou igual a 2")
        else:
            while éPrimo(x) == False :
                x = x - 1
            return x
                
