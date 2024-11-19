import socket
import threading
import os

# Caminho para o socket local
SOCKET_PATH = "/tmp/server_socket"

# Dicionário para armazenar identificadores dos clientes
clients = {}

def handle_client(conn, addr):
    try:
        # Recebe o identificador único do cliente
        identifier = conn.recv(1024).decode("utf-8")
        clients[conn] = identifier
        print(f"Cliente conectado: {identifier} (endereço: {addr})")

        while True:
            # Recebe mensagens do cliente
            message = conn.recv(1024).decode("utf-8")
            if not message:  # Cliente desconectado
                break
            print(f"[{identifier}] {message}")
    except Exception as e:
        print(f"Erro com o cliente {clients.get(conn, addr)}: {e}")
    finally:
        # Remove cliente ao desconectar
        print(f"Cliente desconectado: {clients.get(conn, addr)}")
        clients.pop(conn, None)
        conn.close()

def main():
    # Apaga o socket anterior, se existir
    try:
        os.unlink(SOCKET_PATH)
    except OSError:
        if os.path.exists(SOCKET_PATH):
            raise

    # Cria o socket local
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(SOCKET_PATH)
    server.listen()
    print("Servidor iniciado e aguardando conexões...")

    try:
        while True:
            conn, addr = server.accept()
            # Cria uma nova thread para cada cliente
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        server.close()

if __name__ == "__main__":
    main()
