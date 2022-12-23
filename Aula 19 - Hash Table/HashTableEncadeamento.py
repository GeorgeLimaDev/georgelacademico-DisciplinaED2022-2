
#Uma classe privada utilizada para armazenar os pares chave:valor. É chamada no método put da Hash Table.
class Entry:

    __slots__ = ( "key", "value" )

    def __init__( self, entryKey, entryValue ):
        self.key = entryKey
        self.value = entryValue
        
    def __str__( self ):
        return "(" + str( self.key ) + ", " + str( self.value ) + ")"

class chainHashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = list([] for i in range (self.size))
    
    #Função hash para determinar a posição onde a inserção será feita. Divide a chave passada pelo tamanho da tabela.
    def hash(self,key:int)->int:
        return key % self.size
    
    #Método de inserção na tabela.
    def put(self, key:int, data:object)->int:
        slot = self.hash(key) #Passa pela função hash.
        print(f'Chave {key} no slot {slot}')

        if key in self.table[slot]:
            return -1 #Caso a chave já tenha sido utilizada não a insere novamente.
        else:
            self.table[slot].append(Entry(key, data)) #Caso a chave seja nova é efetuada a inserção através da classe privada Entry.
            return slot

    #Método de leitura da tabela.
    def get(self, key:int):
        slot = self.hash(key)
        if key not in self.table[slot]:
            return -1 #Caso a chave não exista na tabela.
        else:
            return self.table[slot] #Retorna o slot onde a chave está localizada.
            
    def __str__(self):
        info = ''
        for items in self.table: #Primeiro laço itera sobre os slots.
            if items == None:
                continue
            for entry in items: #Segundo laço itera sobre os itens dentro do slot.
                info +=(entry)
        return info

    def __len__(self):
        return self.size
    
    def keys(self):
        result = []
        for primeiro in self.table: #Primeiro laço itera sobre os slots.
            if primeiro != None:
                for entry in primeiro: #Segundo laço itera sobre os itens dentro do slot.
                    result.append(entry.key)
        return result

    #Porque os métodos a seguir funcionam mesmo apontando itens não definidos?
    def getr(hashtable, key):
        entry = _locate(hashtable, key)
        return entry.value
    
    def locate(hashtable, key):
        index = self.hash(key)

        if self.table[index] == None:
            return

        for i, entry in enumerate(self.table[index]):
            if entry.key == key:
                return i

        return -1

    def contains(self, key):
        entry = _locate(hashtable, key)
        return isinstance(entry, Entry)
    
    def displayTable(self):
        entrada = -1
        for items in self.table: #Primeiro laço itera sobre os slots.
            entrada += 1
            print(f'Entrada {entrada:2d}: ', end='')
            if len(items) == 0:
                print('None')
                continue
            for entry in items: #Segundo laço itera sobre os itens dentro do slot.
                print(f'[{entry.key}, {entry.value}] ', end='')
                print()



#Testagem (Usar tamanho 3 para verificar o encadeamento):

tamanho = int(input('Digite o tamanho da Hash Table: '))
table = chainHashTable(tamanho)

table.put(1, 'George')
table.get(1)
table.displayTable()

print()
input('Pressione Enter para continuar')
print()

table.put(2, 'Teste')
table.displayTable()

print()
input('Pressione Enter para continuar')
print()

table.put(3, 'Aluno')
table.displayTable()

print()
input('Pressione Enter para continuar')
print()

table.put(4, 'Professor')
table.displayTable()

print()
input('Pressione Enter para continuar')
print()

table.put(5, 'ED')
table.displayTable()