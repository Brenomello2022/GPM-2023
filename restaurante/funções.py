#Exemplos das funções em uso...

print("--------VISÃO DE RESERVAS DO CLIENTE--------")
visualizar_mesas_disponiveis()

numero_de_convidados = selecionar_numero_pessoas()
numero_de_convidados

data_hora = selecionar_data_e_hora()
data_hora

mesa_escolhida = "Mesa 03"

confirmar_reserva(mesa_escolhida, numero_de_convidados, data_hora)

print("--------VISÃO DO GERENTE--------")
visualizar_reservas_do_dia(data_hora.split()[0])
editar_reserva(mesa_escolhida, numero_de_convidados + 10, "2023-07-22 12:00")
visualizar_reservas_do_dia("2023-07-22 12:00")