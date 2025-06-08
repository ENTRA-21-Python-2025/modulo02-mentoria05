"""
Exemplo de uso de Tuplas em Python
Demonstração de operações básicas e iteração
"""

def demonstrar_tupla():
    print("\n=== Demonstração de Tuplas ===")
    
    # Criando uma tupla com coordenadas de pontos
    ponto_a = (3, 4)
    ponto_b = (5, 2)
    ponto_c = (1, 6)
    
    print("\nCoordenadas dos pontos:")
    print("Ponto A:", ponto_a)
    print("Ponto B:", ponto_b)
    print("Ponto C:", ponto_c)
    
    # Criando um novo ponto com input do usuário
    try:
        print("\nCriando um novo ponto:")
        x = float(input("Digite a coordenada X: "))
        y = float(input("Digite a coordenada Y: "))
        ponto_d = (x, y)
        print("Novo ponto criado:", ponto_d)
        
        # Criando uma nova tupla com todos os pontos
        pontos = (ponto_a, ponto_b, ponto_c, ponto_d)
    except ValueError:
        print("Entrada inválida! Digite números.")
        pontos = (ponto_a, ponto_b, ponto_c)
    
    # Acessando elementos
    print("\nCoordenada X do Ponto A:", ponto_a[0])
    print("Coordenada Y do Ponto A:", ponto_a[1])
    
    # Desempacotando tupla
    x, y = ponto_b
    print("\nDesempacotando Ponto B:")
    print(f"X: {x}, Y: {y}")
    
    # Usando laço for para percorrer a tupla
    print("\nPercorrendo a tupla de pontos:")
    for i, ponto in enumerate(pontos, 1):
        print(f"Ponto {i}: {ponto}")
    
    # Usando enumerate com desempacotamento
    print("\nPercorrendo com desempacotamento:")
    for i, (x, y) in enumerate(pontos, 1):
        print(f"Ponto {i}: X={x}, Y={y}")
    
    # Métodos úteis
    print("\nNúmero de pontos:", len(pontos))
    print("Ponto A aparece", pontos.count(ponto_a), "vezes")
    print("Índice do Ponto B:", pontos.index(ponto_b))
    
    # Tentativa de modificar a tupla (gerará erro)
    print("\nTentando modificar a tupla (isso gerará um erro):")
    try:
        pontos[0] = (2, 2)
    except TypeError as e:
        print("Erro:", e)
        print("Tuplas são imutáveis!")

if __name__ == "__main__":
    demonstrar_tupla() 