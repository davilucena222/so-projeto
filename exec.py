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

processos.sort(key = lambda x: x["tempo_de_chegada"])

fila_de_espera = []
processos_encerrados = []
tempo_atual = 0
tempo_de_espera = 0
tempo_de_resposta = 0
num_processos = len(processos)

while len(processos_encerrados) < num_processos:
  for processo_executa in processos:
    if processo_executa["tempo_de_chegada"] <= tempo_atual and processo_executa not in fila_de_espera and not processo_executa["tempo_restante"] == 0:
      fila_de_espera.append(processo_executa)

    processo = fila_de_espera.pop(0)
    p, tempo_final = executa_processo(processo, tempo_atual)

    # adicionando para todos os processos o tempo em que ficaram na fila de espera
    for proc in fila_de_espera:
      result = tempo_final - tempo_atual

      if proc["tempo_de_espera"] == None:
        proc["tempo_de_espera"] = 0

      proc["tempo_de_espera"] = proc["tempo_de_espera"] + result

    if p["tempo_restante"] == 0:
      processos_encerrados.append(p)
    else:
      fila_de_espera.append(p)
    
    tempo_atual = tempo_final

def executa_processo(processo, tempo_atual):
  tempo_corrido = tempo_atual

  if processo["tempo_de_inicio"] == None:
    processo["tempo_de_inicio"] = tempo_atual

  if processo["tempo_restante"] > 2:
    processo["tempo_restante"] = processo["tempo_restante"] - 2
    tempo_corrido = tempo_corrido + 2
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
  
  return processo, tempo_corrido