import socket
from datetime import datetime

alvo = input("Digite o IP ou site para escanear: ")
portas = [21, 22, 23, 25, 53, 80, 443, 8080]

print(f"\nEscaneando {alvo}...")
print(f"Iniciado em: {datetime.now()}")
print("-" * 50)

try:
    for porta in portas:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((alvo, porta))
        if resultado == 0:
            print(f"Porta {porta}: ABERTA")
        s.close()
except KeyboardInterrupt:
    print("\nSaindo...")
except socket.gaierror:
    print("Host não encontrado.")
except socket.error:
    print("Erro ao conectar ao servidor.")

print("-" * 50)
print("Escaneamento concluído!")
