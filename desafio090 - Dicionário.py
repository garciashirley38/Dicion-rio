aluno = dict()
aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = float(input(f'Digite a média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(f'Nome é é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'A situação é {aluno["situação"]}')
print(aluno)
