import os

os.getcwd()

#mesclar os caminhos
os.path.join(os.getcwd(), 'pasta')
os.getcwd() + '/pasta'

#retorna apenas a ultima pasta contida no caminho citado
os.path.basename(os.getcwd())
os.getcwd().split('/')[-1]

os.path.split(os.getcwd())[0]

#retorna tudo que tem antes da pasta
os.path.dirname(os.getcwd())

#tempo da ultima modificação
os.path.getmtime('variavel')

from datetime import datetime
datetime.utcfromtimestamp(os.path.getmtime('variavel'))

#vericando se é arquivo
os.path.isfile('variavel')
os.path.isdir('variavel')