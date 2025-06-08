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
    
    # Inicialização da lista vazia
    # Usamos [] para criar uma lista vazia que será preenchida pelo usuário
    numeros = []
    
    # Loop principal para adicionar números
    # Continua até que o usuário digite 's' para sair
    print("\nVamos adicionar alguns números à lista:")
    
    while True:
        try:
            # Solicita entrada do usuário
            # Usamos lower() para aceitar 'S' ou 's' para sair
            numero = input("\nDigite um número (ou 's' para sair): ")
            if numero.lower() == 's':
                break
                
            # Converte a entrada para float e adiciona à lista
            # float() pode gerar ValueError se a entrada não for um número
            numero = float(numero)
            numeros.append(numero)
            print(f"Número {numero} adicionado à lista")
            
        except ValueError:
            # Tratamento de erro para entradas inválidas
            print("Por favor, digite um número válido!")
    
    # Exibição da lista completa
    # enumerate() retorna pares de (índice, valor) começando de 1
    print("\nNúmeros na lista:")
    for i, num in enumerate(numeros, 1):
        print(f"{i}. {num}")
    
    # Cálculos e análise da lista
    # Verifica se a lista não está vazia antes de fazer cálculos
    if numeros:
        # Calcula a média usando sum() e len()
        # sum() soma todos os elementos
        # len() retorna o número de elementos
        media = sum(numeros) / len(numeros)
        print(f"\nMédia dos números: {media:.2f}")
        
        # Mostra números maiores que a média
        # Itera sobre a lista e compara cada número com a média
        print("\nNúmeros maiores que a média:")
        for num in numeros:
            if num > media:
                print(f"- {num}")
    else:
        # Mensagem para lista vazia
        print("\nNenhum número foi adicionado à lista!")

# Ponto de entrada do programa
# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    demonstrar_lista() 