"""
Exemplo de uso de Dicionários em Python
Demonstração básica para iniciantes

Este módulo demonstra operações básicas com dicionários em Python:
- Criação e manipulação de dicionários
- Modificação de valores existentes
- Entrada de dados com validação
- Acesso a valores por chave
- Tratamento de erros

Exemplo de uso:
    python exemplo_dicionario.py
"""

def demonstrar_dicionario():
    """
    Demonstra operações básicas com dicionários.
    
    Esta função:
    1. Cria um dicionário simples com nome e idade
    2. Permite modificar os valores via input
    3. Mostra o dicionário antes e depois das modificações
    4. Trata erros de entrada inválida
    
    Returns:
        None
    """
    # Título e explicação inicial
    print("\n=== Demonstração de Dicionários ===")
    print("Um dicionário guarda informações com um nome (chave) e um valor")
    print("Exemplo: nome = 'João', idade = 20")
    
    # Inicialização do dicionário
    # Usamos {} para criar um dicionário com valores iniciais
    # Cada par chave-valor é separado por vírgula
    pessoa = {
        "nome": "João",  # chave "nome" com valor "João"
        "idade": 20      # chave "idade" com valor 20
    }
    
    # Exibição do dicionário inicial
    # Acessamos valores usando a chave entre colchetes
    print("\nDicionário inicial:")
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    
    # Modificação do nome
    # Solicita e valida a entrada do usuário
    print("\nVamos mudar o nome:")
    novo_nome = input("Digite um novo nome: ")
    # Atualiza o valor da chave "nome"
    pessoa["nome"] = novo_nome
    print("Nome atualizado para:", pessoa["nome"])
    
    # Modificação da idade
    # Usa try/except para tratar erros de conversão
    print("\nVamos mudar a idade:")
    try:
        # Converte a entrada para inteiro
        # int() pode gerar ValueError se a entrada não for um número
        nova_idade = int(input("Digite uma nova idade: "))
        # Atualiza o valor da chave "idade"
        pessoa["idade"] = nova_idade
        print("Idade atualizada para:", pessoa["idade"])
    except ValueError:
        # Tratamento de erro para entradas inválidas
        print("Por favor, digite um número para a idade!")
    

    pessoa["funcao"] = "Programador"


    # Exibição do dicionário final
    # Mostra os valores atualizados
    print("\nDicionário final:")
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])
    print("Função:", pessoa["funcao"])

# Ponto de entrada do programa
# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    demonstrar_dicionario() 