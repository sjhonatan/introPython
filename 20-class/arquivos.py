"""
Jhonatan da Silva
Last Updated version :
Tue Jan 31 22:35:52 2017
Number of code lines: 
45
"""
class Arquivos():
    def __init__(self):
        self.path = './arquivosTexto/'
        
    def criarDir(self):
        import os 
        print('criar diretorio : ',self.path)
        print('[s | n]')
        op = input()
        if op == 's':
            f = 'mkdir ' + self.path
            os.system(f)
    
    def lerArquivos(self,nome,p=None):
        if p == None:
            path = self.path
        else:
            path = p
            
        path = path + nome + '.txt'
        with open(path, 'r') as texto:
            dados = texto.read().splitlines()
        
        return dados
    
    def escreverArquivos(self,dados,nome,p=None):
        try:
            if p == None:
                path = self.path
            else:
                path = p
                
            path = path + nome + '.txt'
            with open(path, 'w') as texto:
                if type(dados) == list:
                    for cadaLinha in dados:
                        texto.write(cadaLinha)
                        texto.write('\n')
                else:
                    texto.write(dados)
                    texto.write('\n')
                    
        except FileNotFoundError:
            self.criarDir()
            self.escreverArquivos(dados,nome)
