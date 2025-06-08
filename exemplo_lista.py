"""
Exemplo de uso de Listas em Python
Demonstração básica para iniciantes
"""

def demonstrar_lista():
    print("\n=== Demonstração de Listas ===")
    print("Uma lista é como uma coleção de itens em ordem")
    
    # Criando uma lista vazia
    numeros = []
    
    # Adicionando números à lista
    print("\nVamos adicionar alguns números à lista:")
    
    while True:
        try:
            numero = input("\nDigite um número (ou 's' para sair): ")
            if numero.lower() == 's':
                break
            numero = float(numero)
            numeros.append(numero)
            print(f"Número {numero} adicionado à lista")
        except ValueError:
            print("Por favor, digite um número válido!")
    
    # Mostrando a lista atual
    print("\nNúmeros na lista:")
    for i, num in enumerate(numeros, 1):
        print(f"{i}. {num}")
    
    # Calculando a média
    if numeros:
        media = sum(numeros) / len(numeros)
        print(f"\nMédia dos números: {media:.2f}")
        
        # Mostrando números maiores que a média
        print("\nNúmeros maiores que a média:")
        for num in numeros:
            if num > media:
                print(f"- {num}")
    else:
        print("\nNenhum número foi adicionado à lista!")

if __name__ == "__main__":
    demonstrar_lista() 