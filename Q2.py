from datetime import date

def calcular_idade_em_dias(ano_nascimento):

    ano_atual = date.today().year
    
    if ano_nascimento > ano_atual or ano_nascimento <= 0:
        return None 

    idade_em_anos = ano_atual - ano_nascimento
    idade_em_dias = idade_em_anos * 365
    
    return idade_em_dias

try:
    nascimento = int(input("Digite o seu ano de nascimento (com 4 dígitos): "))
    
    idade_dias = calcular_idade_em_dias(nascimento)

    if idade_dias is not None:
      
        print(f"Você tem aproximadamente {idade_dias:,d} dias de vida.".replace(',', '.'))
        print("\nNota: Este é um valor aproximado que não considera os dias extras de anos bissextos.")
    else:
        print("Ano de nascimento inválido.")

except ValueError:
    print("Erro: Por favor, digite um ano válido (somente números).")
