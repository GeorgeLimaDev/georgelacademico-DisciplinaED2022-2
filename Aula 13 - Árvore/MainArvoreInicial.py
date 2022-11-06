from No import No

def preordem(noInicial):
    if noInicial is None:
        return
    print(f'{noInicial.carga}', end=' ')
    preordem(noInicial.esq)
    preordem(noInicial.dir)

def emordem(noInicial):
    if noInicial is None:
        return
    emordem(noInicial.esq)
    print(f'{noInicial.carga}', end=' ')
    emordem(noInicial.dir)

def posordem(noInicial):
    if noInicial is None:
        return
    posordem(noInicial.esq)
    posordem(noInicial.dir)
    print(f'{noInicial.carga}', end=' ')

def busca(chave, noInicial):
    if noInicial is None:
        return False
    if noInicial.carga == chave:
        return True
    if (busca(chave, noInicial.esq)):
        return True
    else:
        return busca(chave, noInicial.dir)

raiz = No(10)
raiz.esq = No(32)
raiz.dir = No(23)
cursor = raiz.esq #Move o cursor da raiz para o elemento a esquerda.
cursor.esq = No(12)
cursor.dir = No(40)
cursor = cursor.esq
cursor.esq = No(5)
cursor = raiz.dir #Move o cursor da raiz para o elemento a direita.
cursor.dir = No(30)
cursor = cursor.dir #Move o cursor para o nó de valor 30.
cursor.esq = No(60)
cursor = cursor.esq
cursor.dir = No(22)

preordem(raiz)
print()
emordem(raiz)
print()
posordem(raiz)
