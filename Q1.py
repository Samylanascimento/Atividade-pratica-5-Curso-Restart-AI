def calcular_gorjeta(valor_total, porcentagem_gorjeta):
 
    if valor_total < 0 or porcentagem_gorjeta < 0:
        return 0 
        
    gorjeta = valor_total * (porcentagem_gorjeta / 100)
    return gorjeta

try:
    conta = float(input("Digite o valor total da conta: R$ "))
    percentual = float(input("Digite a porcentagem da gorjeta desejada (ex: 10, 15): "))

    valor_da_gorjeta = calcular_gorjeta(conta, percentual)

    print(f"\nO valor da gorjeta é: R$ {valor_da_gorjeta:.2f}")
    print(f"O valor total a ser pago (conta + gorjeta) é: R$ {conta + valor_da_gorjeta:.2f}")

except ValueError:
    print("Erro: Por favor, digite valores numéricos válidos.")
