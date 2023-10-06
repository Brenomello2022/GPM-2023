#Uma lista de mesas disponiveis.

mesas_disponiveis = {"Mesa 01", "Mesa 02", "Mesa 03", "Mesa 04", "Mesa 05"}

#Iniciar um dicionário para armazenar as reservas

reservas = {}

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
def confirmar_reserva(mesa, numero_pessoas, data_hora):
  if mesa in mesas_disponiveis:
    mesas_disponiveis.remove(mesa)
    reservas [mesa] = {
        "num_pessoas": numero_pessoas, 
        "data_hora": data_hora
    }
    print({"Reserva confirmada para a {mesa} às {data_hora} para {numero_pessoas} seres humanos..."})
  else:
    print("Foi mal, hoje não vai dar... favor volte mais tarde...")

#User Story 5
def visualizar_reservas_do_dia(data):
  print(f"Reservas do dia {data}:")
  for mesa, reserva in reserva.itens():
    if reserva["data_hora"].startswith(data):
      print(f"{mesa}, hora: {reserva['data_hora']}, pessoas: {reservas['numero_pessoas']}")

#User Story 6
def editar_reserva(mesa, novo_numero_pessoas, data_hora):
  if mesa in reservas:
    reservas[mesa] = {'numero_pessoas':novo_numero_pessoas, 'data_hora': novo_data_hora}
    print(f"A reserva para {mesa} foi atualizada para {novo_data_hora}, e o novo numero será: {novo_numero_pessoas}")
  else:
    print("Mesa não encontrada nas reservas... tem certeza de que reservou??")