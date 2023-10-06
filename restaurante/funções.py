#Exemplos das funções em uso...

visualizar_mesas_disponiveis()

numero_de_convidados = selecionar_numero_pessoas() #15
numero_de_convidados

data_hora = selecionar_data_e_hora() #2023-10-06 10:00
data_hora

mesa_escolhida = "Mesa 03"

confirmar_reserva(mesa_escolhida, numero_de_convidados, data_hora)

print("--------VISÃO DO GERENTE--------")
visualizar_reservas_do_dia(data_hora.split()[0])
editar_reserva(mesa_escolhida, numero_de_convidados + 10, "2023-07-22 12:00")
visualizar_reservas_do_dia("2023-07-22 12:00")