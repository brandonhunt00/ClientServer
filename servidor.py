import socket

def servidor():
    # Cria um socket TCP/IP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Liga o socket ao endereço 'localhost' e à porta 5000
    servidor_socket.bind(('localhost', 5000))
    
    # Escuta por conexões (máximo de 1 conexão pendente)
    servidor_socket.listen(1)
    print("Servidor aguardando conexão na porta 5000...")
    
    # Aceita a conexão de um cliente
    conexao, endereco = servidor_socket.accept()
    print(f"Conectado por {endereco}")
    
    while True:
        # Recebe dados do cliente (até 1024 bytes)
        dados = conexao.recv(1024)
        if not dados:
            # Se não receber dados, encerra a conexão
            print("Cliente desconectado.")
            break
        
        # Converte os dados recebidos de bytes para bits
        bits_recebidos = ''.join(format(byte, '08b') for byte in dados)
        print(f"Bits recebidos do cliente: {bits_recebidos}")
        
        # Decodifica os dados de bytes para string
        mensagem = dados.decode('utf-8')
        print(f"Cliente: {mensagem}")
        
        # Lê a resposta do servidor via terminal
        resposta = input("Servidor: ")
        if resposta.lower() == 'sair':
            print("Encerrando conexão.")
            break
        
        # Codifica a resposta de string para bytes
        resposta_bytes = resposta.encode('utf-8')
        # Converte os bytes para bits
        bits_enviados = ''.join(format(byte, '08b') for byte in resposta_bytes)
        print(f"Bits enviados para o cliente: {bits_enviados}")
        # Envia os bytes para o cliente
        conexao.sendall(resposta_bytes)
    
    # Fecha a conexão e o socket do servidor
    conexao.close()
    servidor_socket.close()

if __name__ == '__main__':
    servidor()
