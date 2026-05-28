import socket
from datetime import datetime

alvo = input("Digite o IP ou site para escanear: ")
portas = [21, 22, 23, 25, 53, 80, 443, 8080]

print(f"\nIniciando scan em {alvo}")
print(f"Data/Hora: {datetime.now()}")
print("-" * 50)

for porta in portas:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((alvo, porta))
    
    if resultado == 0:
        print(f"Porta {porta}: ABERTA")
    else:
        print(f"Porta {porta}: FECHADA")
    s.close()

print("-" * 50)
print("Scan finalizado!")
