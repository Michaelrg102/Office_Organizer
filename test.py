import os

names = ['test1', 'test2', 'test3', 'test4', 'test5']

system = os.environ
user = system['USERNAME']
os.chdir(fr'C:\Users\{user}\Downloads')
caminho = os.getcwd()

print(system['USERNAME'])
print(caminho)


for name in names:
    with open(f'{name}.xlsx', 'w') as f:
        f.write(f'Conteúdo do {name}.xlsx')

for name in names:
    with open(f'{name}.ppt', 'w') as f:
        f.write(f'Conteúdo do {name}.ppt')

for name in names:
    with open(f'{name}.docx', 'w') as f:
        f.write(f'Conteúdo do {name}.docx')

print('Todos os Arquivos Criados')

with open(f'tomate.docx', 'w') as f:
    f.write(f'tomate')