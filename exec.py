with open("processos.txt", "r") as arquivo:
  linhas = arquivo.readlines()
  
processos = []
j = 0
for linha in linhas:
  tempo_de_chegada, tempo_de_execucao = map(int, linha.strip().split())
  
  j += 1

  processos.append({
    "pid": j,
    "tempo_de_chegada": tempo_de_chegada,
    "tempo_de_execucao": tempo_de_execucao,
    "tempo_restante": tempo_de_execucao,
    "tempo_de_inicio": None,
    "tempo_de_finalizacao": None,
    "tempo_de_resposta": None,
    "tempo_de_espera": None
  })

print("PROCESSOS ORIGINAIS: ", processos)

def executa_processo(processo, tempo_atual):
  tempo_corrido = tempo_atual

  if processo["tempo_de_inicio"] == None:
    processo["tempo_de_inicio"] = tempo_atual

  if processo["tempo_restante"] > 2:
    processo["tempo_restante"] = processo["tempo_restante"] - 2
    tempo_corrido = tempo_corrido + 2
    
    if processo["tempo_de_resposta"] == None:
      processo["tempo_de_resposta"] = tempo_corrido

  elif processo["tempo_restante"] == 1:
    processo["tempo_restante"] = processo["tempo_restante"] - 1
    processo["tempo_restante"] = 0
    tempo_corrido = tempo_corrido + 1
    processo["tempo_de_finalizacao"] = tempo_corrido
  elif processo["tempo_restante"] == 2:
    processo["tempo_restante"] = processo["tempo_restante"] - 2
    processo["tempo_restante"] = 0
    tempo_corrido = tempo_corrido + 2
    processo["tempo_de_finalizacao"] = tempo_corrido
  
  return tempo_corrido

processos.sort(key = lambda x: x["tempo_de_chegada"])

fila_de_espera = []
processos_encerrados = []
primeiros_processos = []
tempo_atual = 0
tempo_de_espera = 0
tempo_de_resposta = 0
num_processos = len(processos)
tempo_de_chegada_primeiro_processo = processos[0]["tempo_de_chegada"]
print("")
print("TEMPO DE CHEGADA DO PRIMEIRO PROCESSO: ", tempo_de_chegada_primeiro_processo)
print("")

while len(processos_encerrados) < num_processos:
  if len(processos) > 0:
    for processo_executa in processos:
      print("")
      print("Processos atuais (restantes): ", processos)
      print("")

      if processo_executa["tempo_de_chegada"] <= tempo_atual and processo_executa not in fila_de_espera and not processo_executa["tempo_restante"] == 0:
        fila_de_espera.append(processo_executa)
        print("")
        print("fila dentro do primeiro for: ", fila_de_espera)
        print("")
        # processos.pop(0)

      if tempo_atual == tempo_de_chegada_primeiro_processo and processo_executa["tempo_de_chegada"] == tempo_de_chegada_primeiro_processo:
        primeiros_processos.append(processo_executa)

  if len(fila_de_espera) == 0:
    tempo_atual = tempo_atual + 1
    print("")
    print("tempo atual (sem processos): ", tempo_atual)
    print("")
    continue


  print("")
  print("Fila antes de retirar um processo para execução: ", fila_de_espera)
  print("")

  processo = fila_de_espera.pop(0)
  tempo_final = executa_processo(processo, tempo_atual)

  print("")
  print("Tempo atual: ", tempo_final)
  print("")


  # i = 0

  if len(processos) > 0:
    for novo_processo in processos:
      print("")
      print("Processo do for 2: ", novo_processo)

      if novo_processo["tempo_de_chegada"] <= tempo_final and novo_processo not in fila_de_espera and not novo_processo["tempo_restante"] == 0 and not novo_processo["pid"] == processo["pid"]:
        # fila_de_espera.insert(i, novo_processo)
        fila_de_espera.append(novo_processo)
        # processos.pop(0)
        # i = i + 1

  if len(fila_de_espera) > 0:
    for proc in fila_de_espera:
      # result = tempo_final - tempo_atual

      if proc["tempo_de_espera"] == None and proc["tempo_de_chegada"] == tempo_de_chegada_primeiro_processo and proc in primeiros_processos and proc["tempo_de_resposta"] != None:
        proc["tempo_de_espera"] = tempo_final - tempo_atual
        # proc["tempo_de_espera"] = tempo_final - proc["tempo_de_chegada"] - proc["tempo_de_resposta"] + tempo_de_chegada_primeiro_processo
      elif proc["tempo_de_espera"] == None:
        proc["tempo_de_espera"] = tempo_final - proc["tempo_de_chegada"]
      else:
        proc["tempo_de_espera"] = proc["tempo_de_espera"] + (tempo_final - tempo_atual)

  print("")
  print("Fila após retirar um processo para execução: ", fila_de_espera)
  print("")

  if processo["tempo_restante"] == 0:
    if processo["tempo_de_espera"] == None:
      processo["tempo_de_espera"] = 0
    processos_encerrados.append(processo)
  else:
    fila_de_espera.append(processo)
    
  tempo_atual = tempo_final
  print("")
  print("Fila após o processo voltar da execução: ", fila_de_espera)
  print("")

tempo_medio_de_retorno = [pp1["tempo_de_finalizacao"] - pp1["tempo_de_chegada"] for pp1 in processos_encerrados]
tempo_medio_de_resposta = [pp2["tempo_de_inicio"] - pp2["tempo_de_chegada"] for pp2 in processos_encerrados]
tempo_medio_espera = [pp3["tempo_de_espera"] for pp3 in processos_encerrados]

print(f"Tempo médio de retorno: {sum(tempo_medio_de_retorno) / len(tempo_medio_de_retorno):.1f}")
print(f"Tempo médio de resposta: {sum(tempo_medio_de_resposta) / len(tempo_medio_de_resposta):.1f}")
print(f"Tempo médio de espera: {sum(tempo_medio_espera) / len(tempo_medio_espera):.1f}")