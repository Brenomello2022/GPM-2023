print("TESTANDO A NOSSA GESTÃO DE TAREFAS")

#Uso das funções - testando as funcionalidades

nome_tarefa = "Preparar material para aula de quinta-feira"
criar_tarefas(nome_tarefa)

adicionar_descricao(nome_tarefa, "Criar contexto de desenvolvimento de software em python... ")
print(tarefas)

definir_data_vencimento(nome_tarefa, "2023-10-15")
print(tarefas)

categorizar_lista(nome_tarefa, "Aula de quinta-feira")
print(tarefas)

marcar_tarefa_concluida(nome_tarefa)
print(tarefas)

adiar_tarefas(nome_tarefa, "2023-10-21")
print(tarefas)