from pycep import PyCep

cep = PyCep(input('Digite seu CEP (apenas números): '))

print('\nCEP:', cep.dadosCep['cep'],
      '\nLogradouro:', cep.dadosCep['logradouro'],
      '\nComplemento:', cep.dadosCep['complemento'],
      '\nBairro:', cep.dadosCep['bairro'],
      '\nCidade:', cep.dadosCep['localidade'], '/', cep.dadosCep['uf'],
      '\nDDD:', cep.dadosCep['ddd'])
