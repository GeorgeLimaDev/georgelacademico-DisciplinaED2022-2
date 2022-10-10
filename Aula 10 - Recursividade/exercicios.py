def fatorial (numero)->int:
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial (numero -1)

def fatorialCompactado (numero)->int:
    return 1 if numero == 0 or numero == 1 else numero * fatorialCompactado(numero -1)


def fibonacci (numero)->int:
    if numero < 0:
        return -1
    elif numero == 0 or numero == 1:
        return numero
    else:
        return (fibonacci(numero-1) + fibonacci(numero-2))

def tamanhoRecursivo(string)->int:
    if string == '':
        return 0
    else:
        return 1 + tamanhoRecursivo(string[1:])

def imprimirString(string)->str:
    if string == '':
        return string
    else:
        print(string[0], end='')
        imprimirString(string[1:])

#Testes:
print(fatorial(5))
print(fatorialCompactado(5))

# n = int(input('Valor de n: '))
# for t in range(0,n+1):
#     print( fibonacci(t), end=',' )

print(tamanhoRecursivo('george lima'))
print(imprimirString('teste')) #Dúvida: pq tá imprimindo um None no final?