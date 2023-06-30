from pycep import PyCep

print('Bem-vindo ao programa de validação de CEP!')

cep = PyCep(input('Digite um CEP (apenas números): '))

print('\nCEP:\033[33m', cep.dadosCep['cep'], '\033[m'
      '\nLogradouro:\033[33m', cep.dadosCep['logradouro'], '\033[m'
      '\nComplemento:\033[33m', cep.dadosCep['complemento'], '\033[m'
      '\nBairro:\033[33m', cep.dadosCep['bairro'], '\033[m'
      '\nCidade:\033[33m', cep.dadosCep['localidade'], '/', cep.dadosCep['uf'], '\033[m'
      '\nDDD:\033[33m', cep.dadosCep['ddd'], '\033[m')
