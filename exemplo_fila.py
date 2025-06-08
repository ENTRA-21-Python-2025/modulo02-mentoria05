"""
Exemplo de uso de Fila em Python
Demonstração básica para iniciantes
"""

from collections import deque
import time

def atender_fila(fila):
    """
    Método para atender todas as pessoas na fila
    """
    match len(fila):
        case 0:
            print("\nNenhuma pessoa foi adicionada à fila!")
        case _:
            print("\nIniciando atendimento:")
            while fila:
                pessoa_atendida = fila.popleft()
                print(f"\n{pessoa_atendida} foi atendido(a)")
                print("Pessoas restantes na fila:", len(fila))
                time.sleep(2)  # Espera 2 segundos entre cada atendimento
            
            print("\nTodas as pessoas foram atendidas!")

def demonstrar_fila():
    print("\n=== Demonstração de Fila ===")
    print("Uma fila é como uma fila de pessoas: o primeiro que chega é o primeiro a sair")
    print("Digite '0' para parar de adicionar pessoas")
    
    # Criando uma fila vazia
    fila = deque()
    
    # Adicionando pessoas à fila
    print("\nVamos adicionar pessoas à fila:")
    
    while True:
        nome = input("\nDigite o nome da pessoa (ou '0' para sair): ")
        if nome == '0':
            break
        if nome.strip():
            fila.append(nome)
            print(f"{nome} foi adicionado à fila")
        else:
            print("Nome inválido! O nome não pode estar vazio.")
    
    # Mostrando a fila atual
    print("\nPessoas na fila:")
    for i, pessoa in enumerate(fila, 1):
        print(f"{i}. {pessoa}")
    
    # Chamando o método para atender a fila
    atender_fila(fila)

if __name__ == "__main__":
    demonstrar_fila() 