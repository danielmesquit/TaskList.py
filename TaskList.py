# Funções

# Adicionar Tarefas
# -Listas Tarefas
# -Marcar Tarefas
# -Exibir tarefas por prioridade/categoria

# Criar menu de comandos

lists = []


def adicionarTarefas():
    # posso adicionar mais de 1 tarefa com o laço for
    nomeTask = input('Digite o nome da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    categoria = input('Digite a categoria da tarefa: ')
    prioridade = int(input('Digite a prioridade da tarefa (0 - baixa /*/ 9 - urgente: '))

    taskList = {'Nome': nomeTask,
                'Descrição': descricao,
                'Categoria': categoria,
                'Prioridade': prioridade,
                'Status': 'Pendente'}

    # nome = lists[0]['Nome']
    # descricao = lists[0]['Descrição']
    # categoria = lists[0]['Categoria']
    # prioridade = lists[0]['Prioridade']
    # status = lists[0]['Status']
    #
    # print(f'A tarefa {nome}')
    # print(f'{descricao}')
    # print(f'Categoria: {categoria}')
    # print(f'Prioridade: {prioridade}')
    # print(f'Status: {status} \n')
    # print(f'Foi adicionada com sucesso.\n')

    print(f'\nA tarefa: {taskList} foi adicionada com sucesso...\n')

    lists.append(taskList)
    # return taskList

def listarTarefas():
    print(f'Foram adicionadas {len(lists)} tarefas.')
    for i in range(len(lists)):
        nome = lists[i]['Nome']
        print(f'A {i + 1}ª tarefa é {nome}')

def mudarStatus():
    selecao = int(input(f'Selecione a tarefa desejada, existem {len(lists)} tarefas: '))

    antigoStatus = lists[selecao - 1]['Status']  # armazenando status antigo

    novoStatus = input('Digite o novo status da tarefa: ')

    lists[selecao - 1].update({'Status':novoStatus})  # Alterando status

    tarefaSelecionada = lists[selecao - 1]['Nome']

    print(f'A tarefa {tarefaSelecionada} teve seu status alterado de {antigoStatus} para {novoStatus}.')

def exibirTarefas():
    print(f'Foram adicionadas {len(lists)} tarefas.')

    for i in range(len(lists)):
        nome = lists[i]['Nome']
        descricao = lists[i]['Descrição']
        categoria = lists[i]['Categoria']
        prioridade = lists[i]['Prioridade']
        status = lists[i]['Status']

        print(f'A {i + 1}ª tarefa é {nome}')
        print(f'Consiste em: {descricao}')
        print(f'Sua categoria: {categoria}')
        print(f'Prioridade: {prioridade}')
        print(f'Status: {status}')

exemploTaskList = {'Nome Tarefa': 'Correr',
                        'Descrição':'Percorrer 5km',
                        'Categoria': 'Esportes',
                        'Prioridade': 0,
                        'Status': 'Em andamento'}

print('---------------- Task List   ----------------\n')

condicao = 0

while True:
    print('--------------- Escolha uma das opções: ----------------')
    print('--------------- 1 - Adicionar Tarefas   -------------')
    print('--------------- 2 - Listar Tarefas      ----------')
    print('--------------- 3 - Mudar Status        ----------')
    print('--------------- 4 - Exibir Tarefas      ----------')
    print('--------------- 5 - Sair                ----------\n')

    seletor = input('Digite um número de 1 a 5: ')

    if seletor == '1':
        adicionarTarefas()

    elif seletor == '2':
        listarTarefas()

    elif seletor == '3':
        mudarStatus()

    elif seletor == '4':
        exibirTarefas()

    elif seletor == '5':
        print('Obrigado...')
        break

    # else:
    #     print('Digite um número de 1 a 5.')
    #     continue