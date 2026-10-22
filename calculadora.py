def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


def ler_numero(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Digite um número válido.")


def main():
    operacoes = {
        "1": ("Somar", somar),
        "2": ("Subtrair", subtrair),
        "3": ("Multiplicar", multiplicar),
        "4": ("Dividir", dividir),
    }

    while True:
        print("\n=== CALCULADORA ===")
        for chave, (nome, _) in operacoes.items():
            print(f"{chave} - {nome}")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Até mais!")
            break

        if opcao not in operacoes:
            print("Opção inválida.")
            continue

        a = ler_numero("Primeiro número: ")
        b = ler_numero("Segundo número: ")
        nome, funcao = operacoes[opcao]
        print(f"Resultado ({nome}): {funcao(a, b)}")


if __name__ == "__main__":
    main()