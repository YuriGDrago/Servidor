import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5000         # Porta que o Servidor esta

# Lista de itens para votação
itens = ['Pizza', 'Hambúrguer', 'Sushi', 'Taco']

# Dicionário de votos
votos = {item: 0 for item in itens}

# Cria o socket do servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Associa o socket do servidor com o endereço e porta
servidor.bind((HOST, PORT))

# Escuta por conexões
servidor.listen()

print('Servidor aguardando conexões...')

while True:
    # Aceita uma nova conexão
    conexao, cliente = servidor.accept()
    print(f'Cliente conectado: {cliente}')

    while True:
        # Recebe a mensagem do cliente
        mensagem = conexao.recv(1024).decode()

        # Verifica se a mensagem não está vazia
        if mensagem:
            # Processa a mensagem do cliente
            comando, *argumentos = mensagem.split()

            if comando == 'LIST':
                # Envia a lista de itens para votação
                lista_itens = ', '.join(itens)
                conexao.send(lista_itens.encode())

            elif comando == 'VOTE':
                # Registra o voto do cliente
                item = ' '.join(argumentos)
                if item in itens:
                    votos[item] += 1
                    conexao.send('Voto registrado com sucesso.'.encode())
                else:
                    conexao.send(f'O item "{item}" não está na lista de votação.'.encode())

            elif comando == 'RANK':
                # Envia o ranking atualizado
                ranking = sorted(votos.items(), key=lambda x: x[1], reverse=True)
                ranking_str = '\n'.join([f'{item}: {votos}' for item, votos in ranking])
                conexao.send(ranking_str.encode())

            else:
                # Comando inválido
                conexao.send('Comando inválido.'.encode())
        else:
            # Se a mensagem estiver vazia, a conexão foi fechada pelo cliente
            print(f'Cliente desconectado: {cliente}')
            conexao.close()
            break
