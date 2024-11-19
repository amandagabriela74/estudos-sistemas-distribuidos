## 📚 Estudos - Sistemas Distribuídos

Este repositório contém meus estudos e implementações práticas sobre os tópicos abordados na disciplina de **Sistemas Distribuídos**. Aqui, você encontrará códigos e explicações de conceitos importantes sobre sistemas distribuídos.

### 📂 Estrutura do Repositório

**01-sockets-locais-e-threads**: Implementação de um servidor e cliente utilizando **sockets locais (AF_UNIX)** e **threads** para suportar múltiplos clientes simultaneamente.
  
### 📝 Descrição do Estudo

#### 01 - Sockets Locais e Threads

Este estudo abrange a implementação de um servidor e um cliente em Python para comunicação via **socket local (AF_UNIX)**. Através do uso de **threads**, o servidor é capaz de aceitar conexões de múltiplos clientes de forma simultânea. 

### ⚙️ Funcionalidade:
1. **Servidor**:
   - Aceita múltiplos clientes simultaneamente.
   - Cada cliente é tratado em uma **thread** separada.
   - Utiliza **socket local** para comunicação.
   
2. **Cliente**:
   - Conecta-se ao servidor via **socket local**.
   - Envia mensagens para o servidor, que as processa.

### 🚀 Como Rodar

🔧 **Pré-requisitos**
   - Python 3.x instalado.

🖥️ **Rodando o Servidor**
1. Navegue até a pasta do servidor:
   ```bash
   cd 01-sockets-locais-e-threads

2. Execute o servidor:
   ```bash
   python3 server.py

3. Execute o cliente:
   ```bash
   python3 client.py
