from cpf_generator import CPF

print('Bem-vindo ao programa de validação de CPF!')

cpf = input('Digite um CPF (apenas números): ')

if CPF.validate(cpf):
    print(f'\nO CPF \033[3m{CPF.format(cpf)}\033[m é válido')
else:
    print(f'\nO CPF \033[3m{CPF.format(cpf)}\033[m NÃO é válido')
