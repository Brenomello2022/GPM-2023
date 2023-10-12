#Criar um dicionario / tupla para as nossas atividades.

tarefas = {}

#Aqui a gente cria as tarefas.

# 1) Criar uma nova tarefa.
def criar_tarefas(nome):
  tarefas[nome] = {
      'descricao': None,
      'data_vencimento': None,
      'concluida': False,
      'lista': 'Geral' 
      #por padrão, todos nascem na lista geral.
  }
  print(f"Tarefa: <{nome}> foi criada com sucesso! ")

# 2) Adicionar uma descrição à tarefa.
def adicionar_descricao(nome, descricao):
  if nome in tarefas:
    tarefas[nome]['descricao'] = descricao
    print(f"Deu boa, a descrição da sua tarefa <{nome}> foi adicionada! : <{descricao}> !!!")
  else:
    print(f"Não deu boa, tarefa não encontrada!")

# 3) Definir uma data de vencimento para a tarefa.
def definir_data_vencimento(nome, data_vencimento):
  tarefas[nome]['data_vencimento'] = data_vencimento
  print(f"A data de vencimento definida para a tarefa <{nome}> foi : <{data_vencimento}> !!!")
else:
  print(f"Mais uma vez, a tarefa não foi encontrada, amigo! ")

# 4) Categorizar tarefas em listas.
def categorizar_lista(nome, lista):
  if nome in tarefas:
    print(f"Tarefa <{nome}> agora está na lista <{lista}> !!! ")
  else:
    print(f"Pela terceira vez, a tarefa não foi encontrada, parça! ")

# 5) Marcar uma tarefa como concluida.
def marcar_tarefa_concluida(nome):
  if nome in tarefas:
    tarefas[nome]['concluida'] = True
    print(f"Tarefa <{nome}> marcada como concluída! ")
  else:
    print(f"Pela quarta vez, a tarefa não foi encontrada, parça! ")

# 6) Adiar uma tarefa para uma data futura.
def adiar_tarefas(nome, nova_data):
  if nome in tarefas:
    data_velha = tarefas[nome]['data_vencimento']
    tarefas[nome]['data_vencimento'] = nova_data
    print(f"A tarefa <nome> foi atualizada para a nova data <{nova_data}> - a data original era <{data_velha} !!>")
  else:
    print(f"Pela quinta vez, a tarefa não foi encontrada, parça! ")