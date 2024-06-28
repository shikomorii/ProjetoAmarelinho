from cartao import Cartao,Estudante

sebastian= Cartao("sebastian",465,0) 
sebastian.carregarcarterinha(10)
sebastian.passagem(4.50)


Filipe= Cartao("Filipe",777,0) 
Filipe.carregarcarterinha(10)
Filipe.passagem(4.50) 

messi= Cartao("messi",666,0)  
messi.carregarcarterinha(10)
messi.passagem(4.50)

Salomao =Estudante("Salomão",564,0,"Satc") 
print(Salomao.nome,Salomao.nrconta,Salomao.saldo,Salomao.escola)
Salomao.carregarcarterinha(10)
print(Salomao.nome,"da matricula",Salomao.nrconta,"seu saldo é de R$",Salomao.saldo,"estuda na escola",Salomao.escola)
Salomao.carregarcarterinha(20)
Salomao.passagemestudante(2.50)
