
class Cartao:
    def __init__(self,nome,nrconta,saldo):
        self.nome = nome
        self.nrconta = nrconta
        self.__saldo = 0
        
   


    @property
    def saldo(self):
        return self.__saldo 
    
    @saldo.setter
    def saldo(self,novovalor):
        raise ValueError("nao e posivel alterar o valor da carterinha, use o metodo carregar carterinha ")


    def carregarcarterinha(self,aumento):
        self.aumento = aumento
        novovalor = self.saldo + aumento
        print(self.nome,"seu aumento foi de ",novovalor)

    def passagem (self,diminuir):
        self.diminuir = diminuir
        valor_pos_passagem =  10 - diminuir
        print("seu novo valor na carterinha é de R$ ",valor_pos_passagem)

class Estudante(Cartao):
    def __init__(self,nome,nrconta,saldo,escola):
        super().__init__(nome,nrconta,saldo)
        self.escola = escola

    def passagemestudante (self,diminuir):
        self.diminuir = diminuir
        valor_pos_passagem =  20 - diminuir
        print("seu novo valor na carterinha é de R$ ",valor_pos_passagem)
        i = input("VC vai viajar para onde?")

    


    
            
    