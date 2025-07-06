import string

def verificar_palindromo(frase):
  
    caracteres_a_remover = string.punctuation + string.whitespace
    translator = str.maketrans('', '', caracteres_a_remover)

   
    frase_limpa = frase.lower().translate(translator)
    

    if frase_limpa == frase_limpa[::-1]:
        return "Sim"
    else:
        return "Não"


texto_usuario = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

resultado = verificar_palindromo(texto_usuario)
print(f'"{texto_usuario}" é um palíndromo? {resultado}')


print("\n--- Testes Adicionais ---")
print(f'Anotaram a data da maratona: {verificar_palindromo("Anotaram a data da maratona")}')
print(f'ovo: {verificar_palindromo("ovo")}')
print(f'python: {verificar_palindromo("python")}')
