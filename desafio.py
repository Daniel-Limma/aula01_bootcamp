CONSTANTE_BONUS = 1000


nome_usuario = input("insira seu nome: ")

salario_usuario = float(input("insira o seu salario: "))

bonus_usuario = float(input("insira seu bônus: "))

valor_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario
print(f"O {nome_usuario} possui o bonus de {valor_bonus}")