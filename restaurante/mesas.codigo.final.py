#Uma lista de mesas disponiveis.

mesas_disponiveis = ["Mesa 01", "Mesa 02", "Mesa 03", "Mesa 04", "Mesa 05"]

#Iniciar um dicionário para armazenar as reservas

reservas = {}

#Uma lista de mesas disponiveis.

#User Story 1
def visualizar_mesas_disponiveis():
  print("Mesas disponiveis: ")
  for mesa in mesas_disponiveis:
    print(mesa)

#User Story 2
def selecionar_numero_pessoas():
  return int(input("Quantas pessoas vão farrear contigo? (APENAS NÚMEROS)" ))

#User Story 3
def selecionar_data_e_hora():
  data_hora = input("Informe a data e hora da sua reserva... querido: (formato: AAAA-MM-DD HH:MM)")
  return data_hora

#User Story 4
def confirmar_reserva(mesa, num_pessoas, data_hora):
  if mesa in mesas_disponiveis:
    mesas_disponiveis.remove(mesa)
    reservas [mesa] = {
        "num_pessoas": num_pessoas,
        "data_hora": data_hora
    }
    print(f"Reserva confirmada para a {mesa} às {data_hora} para {num_pessoas} seres humanos...")
  else:
    print("Foi mal, hoje não vai dar... favor volte mais tarde...")

#User Story 5
def visualizar_reservas_do_dia(data):
  print(f"Reservas do dia {data}:")
  for mesa, reserva in reservas.items():
    if reserva["data_hora"].startswith(data):
      print(f"{mesa}, hora: {reserva['data_hora']}, pessoas: {reserva['num_pessoas']}")

#User Story 6
def editar_reserva(mesa, novo_numero_pessoas, novo_data_hora):
  if mesa in reservas:
    reservas[mesa] = {'num_pessoas':novo_numero_pessoas, 'data_hora': novo_data_hora}
    print(f"A reserva para {mesa} foi atualizada para {novo_data_hora}, e o novo numero será: {novo_numero_pessoas}")
  else:
    print("Mesa não encontrada nas reservas... tem certeza de que reservou??")

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