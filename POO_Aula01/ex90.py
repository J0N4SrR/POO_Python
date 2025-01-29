
infoAlunos = {'nome': input('Digite um nome:'), 'média': ''}
infoAlunos['media'] = float(input(f'Digite a média de {infoAlunos['nome']}:'))
print(f'O nome é igual a {infoAlunos['nome']}')
print(f'A média é igual a {infoAlunos['media']}')
if infoAlunos['media'] > 5:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')