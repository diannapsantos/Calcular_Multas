print(" Programa de Cálculo de Multas iniciado com sucesso.\n")

def multa_localidade(vel):
    if vel > 120:
        return 320
    elif vel >= 90:
        return 120
    elif vel > 50:
        return 60
    else:
        return 0

def multa_fora_localidade(vel):
    if vel >= 120:
        return 120
    elif vel > 90:
        return 60
    else:
        return 0

def multa_autoestrada(vel):
    if vel > 175:
        return 360
    elif vel > 150:
        return 120
    elif vel > 120:
        return 60
    else:
        return 0

def menu():
    print("\nSelecione o tipo de estrada:")
    print("1 - Localidade")
    print("2 - Fora da localidade")
    print("3 - Autoestrada")
    print("4 - Sair")

def main():
    while True:
        menu()
        escolha = input("Opção: ")
        
        if escolha == "4":
            print("Programa terminado.")
            break

        try:
            velocidade = float(input("Velocidade registada (km/h): "))
        except ValueError:
            print("Erro: Introduza um número válido.")
            continue

        if velocidade < 50:
            print("Velocidade dentro do limite. Sem multa.")
            continue

        if escolha == "1":
            multa = multa_localidade(velocidade)
        elif escolha == "2":
            multa = multa_fora_localidade(velocidade)
        elif escolha == "3":
            multa = multa_autoestrada(velocidade)
        else:
            print("Opção inválida.")
            continue

        if multa == 0:
            print("Sem multa.")
        else:
            print(f"Multa a pagar: {multa}€")

if __name__ == "__main__":
    main()

print("\n Obrigado por utilizar o sistema de cálculo de multas!")

