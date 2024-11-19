import socket
import uuid

# Caminho para o socket local
SOCKET_PATH = "/tmp/server_socket"

def main():
    # Cria o socket local
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect(SOCKET_PATH)

    try:
        # Envia um identificador único para o servidor
        identifier = f"client-{uuid.uuid4()}"
        client.sendall(identifier.encode("utf-8"))
        print(f"Conectado ao servidor como {identifier}")

        while True:
            # Aguarda input do usuário
            message = input("Digite uma mensagem (ou 'sair' para encerrar): ")
            if message.lower() == "sair":
                break
            client.sendall(message.encode("utf-8"))
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        print("Encerrando cliente...")
        client.close()

if __name__ == "__main__":
    main()
