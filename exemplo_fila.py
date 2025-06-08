"""
Exemplo de uso de Fila em Python
Demonstração básica para iniciantes

Este módulo demonstra operações básicas com filas (deque) em Python:
- Criação e manipulação de filas
- Adição e remoção de elementos
- Verificação de fila vazia usando match
- Atendimento sequencial com delay
- Tratamento de erros

Exemplo de uso:
    python exemplo_fila.py
"""

from collections import deque
import time

def atender_fila(fila):
    """
    Atende todas as pessoas na fila com um intervalo entre atendimentos.
    
    Esta função:
    1. Verifica se a fila está vazia usando match
    2. Atende cada pessoa sequencialmente
    3. Adiciona um delay entre atendimentos
    4. Mostra o progresso do atendimento
    
    Args:
        fila (deque): A fila de pessoas a ser atendida
        
    Returns:
        None
    """
    # Usa match para verificar o estado da fila
    # case 0: fila vazia
    # case _: qualquer outro tamanho (tem pessoas na fila)
    match len(fila):
        case 0:
            print("\nNenhuma pessoa foi adicionada à fila!")
        case _:
            print("\nIniciando atendimento:")
            # Loop de atendimento
            # Continua até que a fila esteja vazia
            while fila:
                # Remove e retorna a primeira pessoa da fila
                # popleft() é mais eficiente que pop(0) para filas
                pessoa_atendida = fila.popleft()
                print(f"\n{pessoa_atendida} foi atendido(a)")
                print("Pessoas restantes na fila:", len(fila))
                # Adiciona um delay de 2 segundos entre atendimentos
                # time.sleep() pausa a execução do programa
                time.sleep(2)
            
            print("\nTodas as pessoas foram atendidas!")

def demonstrar_fila():
    """
    Demonstra operações básicas com filas.
    
    Esta função:
    1. Cria uma fila vazia
    2. Permite adicionar pessoas via input
    3. Mostra a fila completa
    4. Atende todas as pessoas
    
    Returns:
        None
    """
    # Título e explicação inicial
    print("\n=== Demonstração de Fila ===")
    print("Uma fila é como uma fila de pessoas: o primeiro que chega é o primeiro a sair")
    print("Digite '0' para parar de adicionar pessoas")
    
    # Inicialização da fila vazia
    # deque() é uma estrutura de dados otimizada para operações nas extremidades
    fila = deque()
    
    # Loop principal para adicionar pessoas
    # Continua até que o usuário digite '0' para sair
    print("\nVamos adicionar pessoas à fila:")
    
    while True:
        # Solicita entrada do usuário
        nome = input("\nDigite o nome da pessoa (ou '0' para sair): ")
        if nome == '0':
            break
        # Verifica se o nome não está vazio
        # strip() remove espaços em branco no início e fim
        if nome.strip():
            # Adiciona a pessoa ao final da fila
            fila.append(nome)
            print(f"{nome} foi adicionado à fila")
        else:
            print("Nome inválido! O nome não pode estar vazio.")
    
    # Exibição da fila completa
    # enumerate() retorna pares de (índice, valor) começando de 1
    print("\nPessoas na fila:")
    for i, pessoa in enumerate(fila, 1):
        print(f"{i}. {pessoa}")
    
    # Chama o método para atender a fila
    atender_fila(fila)

# Ponto de entrada do programa
# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    demonstrar_fila() 