import socket

def cliente():
    # Cria um socket TCP/IP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Endereço IP do servidor (localhost) e porta 5000
    servidor_ip = 'localhost'  # Pode ser '127.0.0.1' também
    servidor_porta = 5000
    
    try:
        # Conecta ao servidor
        cliente_socket.connect((servidor_ip, servidor_porta))
        print(f"Conectado ao servidor {servidor_ip} na porta {servidor_porta}.")
    except ConnectionRefusedError:
        print("Falha ao conectar ao servidor. Certifique-se de que o servidor está em execução.")
        return
    
    while True:
        # Envia mensagem para o servidor
        mensagem = input("Cliente: ")
        if mensagem.lower() == 'sair':
            print("Encerrando conexão.")
            break
        
        # Codifica a mensagem em bytes
        mensagem_bytes = mensagem.encode('utf-8')
        # Converte os bytes em bits
        bits_enviados = ''.join(format(byte, '08b') for byte in mensagem_bytes)
        print(f"Bits enviados para o servidor: {bits_enviados}")
        # Envia os bytes para o servidor
        cliente_socket.sendall(mensagem_bytes)
        
        # Recebe resposta do servidor
        dados = cliente_socket.recv(1024)
        if not dados:
            print("Servidor desconectado.")
            break
        # Converte os bytes recebidos em bits
        bits_recebidos = ''.join(format(byte, '08b') for byte in dados)
        print(f"Bits recebidos do servidor: {bits_recebidos}")
        # Decodifica os bytes em string
        resposta = dados.decode('utf-8')
        print(f"Servidor: {resposta}")
    
    # Fecha o socket do cliente
    cliente_socket.close()

if __name__ == '__main__':
    cliente()
