import os

#essa função retorna o caminho completo até onde eu estou
os.getcwd()

#me retorna uma lista de todos arquivos dentro de uma pasta
os.listdir()

#trocar o diretório padrão
os.chdir()

#criar uma pasta
os.mkdir()

#renomear nome de um arquivo
os.rename('de', 'para')

#remover um diretório
os.remove()

#removendo um diretório
os.rmdir()

#ele executa terminal do sistema
#ele vai executar o comando date dentro do cmd do windows nesse caso
cmd = 'date'
os.system(cmd)