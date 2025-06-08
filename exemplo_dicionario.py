"""
Exemplo de uso de Dicionários em Python
Demonstração básica para iniciantes
"""

def demonstrar_dicionario():
    print("\n=== Demonstração de Dicionários ===")
    print("Um dicionário guarda informações com um nome (chave) e um valor")
    print("Exemplo: nome = 'João', idade = 20")
    
    # Criando um dicionário simples
    pessoa = {
        "nome": "João",
        "idade": 20
    }
    
    print("\nDicionário inicial:")
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    
    # Modificando o nome
    print("\nVamos mudar o nome:")
    novo_nome = input("Digite um novo nome: ")
    pessoa["nome"] = novo_nome
    print("Nome atualizado para:", pessoa["nome"])
    
    # Modificando a idade
    print("\nVamos mudar a idade:")
    try:
        nova_idade = int(input("Digite uma nova idade: "))
        pessoa["idade"] = nova_idade
        print("Idade atualizada para:", pessoa["idade"])
    except ValueError:
        print("Por favor, digite um número para a idade!")
    
    # Mostrando o dicionário final
    print("\nDicionário final:")
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])

if __name__ == "__main__":
    demonstrar_dicionario() 