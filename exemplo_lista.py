"""
Exemplo de uso de Listas em Python
Demonstração básica para iniciantes

Este módulo demonstra operações básicas com listas em Python:
- Criação e manipulação de listas
- Entrada de dados com validação
- Iteração usando for
- Cálculos básicos (média)
- Tratamento de erros

Exemplo de uso:
    python exemplo_lista.py
"""

def demonstrar_lista():
    """
    Demonstra operações básicas com listas.
    
    Esta função:
    1. Cria uma lista vazia
    2. Permite adicionar números via input
    3. Mostra a lista completa
    4. Calcula a média
    5. Mostra números maiores que a média
    
    Returns:
        None
    """
    # Título e explicação inicial
    print("\n=== Demonstração de Listas ===")
    print("Uma lista é como uma coleção de itens em ordem")
    
    # numeros: Inicializa uma lista vazia que será usada para armazenar todos os números digitados pelo usuário
    # Esta lista começa vazia ([]) e será preenchida durante a execução do programa
    numeros = []
    
    print("\nVamos adicionar alguns números à lista:")
    
    while True:
        try:
            # Solicita entrada do usuário
            # Usamos lower() para aceitar 'S' ou 's' para sair
            numero = input("\nDigite um número (ou 's' para sair): ")
            if numero.lower() == 's':
                break
                
            # Converte a entrada para float e adiciona à lista numeros
            # numeros.append(): Adiciona o novo número ao final da lista numeros
            # Cada novo número digitado é convertido para float e adicionado sequencialmente
            numero = float(numero)
            numeros.append(numero)
            print(f"Número {numero} adicionado à lista")
            
        except ValueError:
            # Tratamento de erro para entradas inválidas
            print("Por favor, digite um número válido!")
    
    # Remove todos os números maiores que 10
    i = 0
    while i < len(numeros):
        if numeros[i] > 10:
            numeros.remove(numeros[i])
        else:
            i += 1
    
    print("\nNúmeros maiores que 10 foram removidos da lista.")

    # Exibição da lista numeros completa
    # numeros é iterada usando enumerate para mostrar cada número com seu índice
    # enumerate(numeros, 1): Gera pares de (índice, valor) começando do 1 para cada elemento em numeros
    print("\nNúmeros na lista:")
    for i, num in enumerate(numeros, 1):
        print(f"{i}. {num}")
    
    # Cálculos e análise da lista numeros
    if numeros:
        # numeros é usada para calcular a média:
        # sum(numeros): Soma todos os elementos da lista
        # len(numeros): Retorna o tamanho total da lista
        media = sum(numeros) / len(numeros)
        print(f"\nMédia dos números: {media:.2f}")
        
        # numeros é iterada novamente para encontrar números maiores que a média
        # Cada elemento em numeros é comparado com o valor da média
        print("\nNúmeros maiores que a média:")
        for num in numeros:
            if num > media:
                print(f"- {num}")
    else:
        print("\nNenhum número foi adicionado à lista!")

# Ponto de entrada do programa
# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    demonstrar_lista() 