from pycep import PyCep

print('Bem vindo ao programa de validação de CEP!')

cep = PyCep(input('Digite um CEP (apenas números): '))

print('\nCEP:', cep.dadosCep['cep'],
      '\nLogradouro:', cep.dadosCep['logradouro'],
      '\nComplemento:', cep.dadosCep['complemento'],
      '\nBairro:', cep.dadosCep['bairro'],
      '\nCidade:', cep.dadosCep['localidade'], '/', cep.dadosCep['uf'],
      '\nDDD:', cep.dadosCep['ddd'])
