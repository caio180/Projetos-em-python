#Exemplos básicos para não esquecer como funciona.
class Vendedor:
    def __init__(self):
        self.nome = input("Digite o nome do vendedor: ")
        self.vendas = 0
    
    def metas(self):
        self.vendas = int(input("Digite a suas vendas totais: "))

        if self.vendas >= 700:
            print(f"{self.nome}, atingiu a meta de vendas.")
        else:
            print(f"{self.nome}, não atingiu a meta.")

vendedor1 = Vendedor()
vendedor1.metas()
