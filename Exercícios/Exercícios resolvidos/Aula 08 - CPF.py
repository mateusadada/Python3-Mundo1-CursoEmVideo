from cpf_generator import CPF

cpf = CPF.generate()
cpf_formatado = CPF.format(cpf)

print(cpf_formatado)
