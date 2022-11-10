from enum import Enum

class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None
    
    def __str__(self):
        return str(self.carga)
    
class ArvoreBinaria:
    def __init__(self, cargaRaiz:any = None):
        self.__raiz = No(cargaRaiz) if cargaRaiz != None else cargaRaiz
    
    def criarRaiz(self, cargaRaiz:any):
        if self.__raiz is None:
            self.__raiz = No(cargaRaiz)
    
    def estaVazia(self)->bool:
        return self.__raiz == None
    
    def getRaiz(self)->any:
        if self.__raiz is not None:
            return self.__raiz.carga
        else:
            return None

    def preordem(self):
        self.__preordem(self.__raiz)
    
    def __preordem(self, no):
        if no is None:
            return
        print(f'{no.carga}', end=' ')
        self.__preordem(no.esq)
        self.__preordem(no.dir)

    def emordem(self):
        self.__emordem(self.__raiz)
    
    def __emordem(self, no):
        if no is None:
            return
        self.__emordem(no.esq)
        print(f'{no.carga}', end=' ')
        self.__emordem(no.dir)

    def posordem(self):
        self.__posordem(self.__raiz)
    
    def __posordem(self, no):
        if no is None:
            return
        self.__posordem(no.esq)
        self.__posordem(no.dir)
        print(f'{no.carga}', end=' ')

    def add(self, carga:any):
        if (self.__raiz == None):
            self.__raiz = No(carga)
        else:
            self.__add(carga, self.__raiz)

    def __add(self, carga:any, node:'No'):
        if (carga < node.carga):
            if (node.esq != None):
                self.__add(carga, node.esq)
            else:
                node.esq = No(carga)
        else:
            if (node.dir != None):
                self.__add(carga, node.dir)
            else:
                node.dir = No(carga)

    def __count(self, no:No)->int:
        if no is None:
            return 0
        return 1 + self.__count(no.esq) + self.__count(no.dir)

    def __len__(self):
        return self.__count(self.__raiz)

    def busca(self, chave:any):
        return self.__busca(chave, self.__raiz)
    
    def __busca(self, chave, no:No):
        if no is None:
            return False
        if (chave == no.carga):
            return True
        elif (chave < no.carga and no.esq != None):
            return self.__busca(chave, no.esq)
        elif (chave > no.carga and no.dir != None):
            return self.__busca(chave, no.dir)
        else:
            return False
        
    def removeNo(self, chave:any)->any:
        if self.__raiz is None:
            return None
        if chave == self.__raiz.carga:
            if self.__raiz.esq is None and self.__raiz.dir is None:
                self.__raiz = None
                return None
            if self.__raiz.esq is None:
                self.__raiz = self.__raiz.dir
                return self.__raiz.carga
            elif self.__raiz.dir is None:
                self.__raiz = self.__raiz.esq
                return self.__raiz.carga
        retorno = self.__removeNo(self.__raiz, chave)
        return retorno.carga

    def __removeNo(self, node, chave):
        if node is None:
            return None
        if chave < node.carga:
            node.esq = self.__removeNo(node.esq, chave)
        elif (chave > node.carga):
            node.dir = self.__removeNo(node.dir, chave)
        else:
            if node.esq is None:
                temp = node.dir
                node = None
                return temp
            elif node.dir is None:
                temp = node.esq
                node = None
                return temp
            
            temp = self.__minValueNode(node.dir)
            node.carga = temp.carga
            node.dir = self.__removeNo(node.dir, temp.carga)
        return node
    
    def __minValueNode(self, node:'No'):
        current = node
        while (current.esq  is not None):
            current = current.esq
        return current

    def __maxValueNode(self, node:'No'):
        current = node
        while (current.dir is not None):
            current = current.dir
        return current

    def __go(self, chave:int, no:No)->No:
        if no is None:
            return None
        if no.carga == chave:
            return no
        resultado = self.__go(chave, no.esq)
        if (resultado):
            return resultado
        else:
            return self.__go(chave, no.dir)

    def removeRaiz(self)->bool:
        if (len(self) == 1):
            self.__raiz = self.__cursor = None
            return True
        else:
            return False
