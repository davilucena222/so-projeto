    ################################# ALGORITMO FCFS ########################################
# arquivo de texto com os processos
nome_do_arquivo = "processos.txt"

# lendo o arquivo de texto
with open(nome_do_arquivo, "r") as f:
  linhas = f.readlines()
numero_de_processos = len(linhas)

# função para extrair os dados dos processos e armazená-los em uma lista
def dadosProcessos(linhas):
  dados_processos = [] 

  # loop para extrair os dados do arquivo de texto
  for i, linha in enumerate(linhas):  
    temporario = [] 
    tempo_de_chegada, tempo_de_execucao = linha.split() 
    temporario.extend([i + 1, int(tempo_de_chegada), int(tempo_de_execucao)]) 
    dados_processos.append(temporario) 

  # chamando função para realizar os cálculos
  calculoProcesso(dados_processos)

# função para realizar os calculos de tempos iniciais e finais
def calculoProcesso(dados_processos):
  # ordenando processos com base no tempo de chegada
  dados_processos.sort(key=lambda x: x[1]) 
  tempo_inicio = []
  tempo_de_saida = []
  tempo_atual = 0

  # loop for para calcular o tempo de início e o tempo de saída
  for i in range(len(dados_processos)):
    if tempo_atual < dados_processos[i][1]: 
      tempo_atual = dados_processos[i][1] 

    # armazenando os tempos de início e saída
    tempo_inicio.append(tempo_atual) 
    tempo_atual = tempo_atual + dados_processos[i][2] 
    tempo_final = tempo_atual 
    tempo_de_saida.append(tempo_final)
    dados_processos[i].append(tempo_final) 

  # chamando função para calcular os tempos médios
  tempo_de_retorno = calculandoTempoDeRetorno(dados_processos)
  tempo_de_resposta = calculandoTempoDeResposta(dados_processos, tempo_inicio)
  tempo_de_espera = calculandoTempoDeEspera(dados_processos) 

  # chamando função para eixibir os resultados finais
  resultadosFinais(tempo_de_retorno, tempo_de_resposta, tempo_de_espera) 

# função para calcular o tempo de retorno
def calculandoTempoDeRetorno(dados_processos):
  tempo_total_de_retorno = 0

  # loop para realizar o cálculo do tempo de retorno
  for i in range(len(dados_processos)):  
    tempo_de_retorno = dados_processos[i][3] - dados_processos[i][1]  
    tempo_total_de_retorno = tempo_total_de_retorno + tempo_de_retorno  
    dados_processos[i].append(tempo_de_retorno)  

  tempo_de_retorno_medio = tempo_total_de_retorno / len(dados_processos)   

  return tempo_de_retorno_medio 

# função para calcular o tempo de espera
def calculandoTempoDeEspera(dados_processos):
  tempo_total_de_espera = 0

  # loop para realizar o cálculo do tempo de espera
  for i in range(len(dados_processos)):  
    tempo_de_espera = dados_processos[i][4] - dados_processos[i][2] 
    tempo_total_de_espera = tempo_total_de_espera + tempo_de_espera 
    dados_processos[i].append(tempo_de_espera) 

  tempo_de_espera_medio = tempo_total_de_espera / len(dados_processos)  

  return tempo_de_espera_medio  

# função para calcular o tempo de resposta
def calculandoTempoDeResposta(dados_processos, tempo_inicial):
  tempo_total_de_resposta = 0  

  # loop para realizar o cálculo do tempo de resposta
  for i in range(len(dados_processos)):  
    tempo_de_resposta = tempo_inicial[i] - dados_processos[i][1] 
    tempo_total_de_resposta = tempo_total_de_resposta + tempo_de_resposta 
    dados_processos[i].append(tempo_de_resposta)  

  tempo_de_resposta_medio = tempo_total_de_resposta / len(dados_processos)  

  return tempo_de_resposta_medio  

# função para imprimir os resultados finais
def resultadosFinais(tempo_de_retorno_medio, tempo_de_resposta_medio, tempo_de_espera_medio):
  print(f"FCFS {tempo_de_retorno_medio:.1f} {tempo_de_resposta_medio:.1f} {tempo_de_espera_medio:.1f}")

# chamando a função para extrair os dados dos processos e iniciar o programa
dadosProcessos(linhas)


      ################################# ALGORITMO SJF ########################################

processos = []

# capturando os processos do arquivo de entrada
for i, linha in enumerate(linhas):
  tempo_de_chegada, tempo_de_execucao = map(int, linha.strip().split())
  processos.append((tempo_de_chegada, tempo_de_execucao, i))

# ordenando os processos
processos.sort()

# arrays para armazenar os dados dos processos
qtd_processos = len(processos)
tempo_de_conclusao = [0] * qtd_processos
tempo_de_retorno = [0] * qtd_processos
tempo_de_espera = [0] * qtd_processos
tempo_de_resposta = [0] * qtd_processos

tempo = 0

# bloco principal que executa os processos
while processos:
  processos_disponiveis = [p for p in processos if p[0] <= tempo]

  if not processos_disponiveis:
    tempo = tempo + 1
    continue
  
  # pega o processo com o menor tempo de execução no tempo atual
  proximo_processo = min(processos_disponiveis, key=lambda p: p[1])
  
  # remove o processo da lista de processos que foi para a execução 
  processos.remove(proximo_processo)


  # cálculos de todos os tempos médios
  tempo_de_chegada, tempo_de_execucao, i = proximo_processo 
  tempo_de_conclusao[i] = tempo + tempo_de_execucao 
  tempo_de_retorno[i] = tempo_de_conclusao[i] - tempo_de_chegada 
  tempo_de_espera[i] = tempo_de_retorno[i] - tempo_de_execucao 
  tempo_de_resposta[i] = tempo - tempo_de_chegada 
  tempo = tempo_de_conclusao[i]

# demonstrando o resultado final
print(f"SJF {sum(tempo_de_retorno)/numero_de_processos:.1f} {sum(tempo_de_resposta)/numero_de_processos:.1f} {sum(tempo_de_espera)/numero_de_processos:.1f}")


  ################################# ALGORITMO ROUND ROBIN ########################################   
        
processos = []
j = 0

# inicializando os processos com os valores
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

# função que realiza o desconto do tempo de execução de cada processo e avança o tempo
# a cada tempo de execução avançado os processos que chegam tem seus tempos alterados com base nos cálculos
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

# ordenando os procesos com base no tempo de chegada
processos.sort(key = lambda x: x["tempo_de_chegada"])

# arrays e variáveis para armazenar os dados dos processos
fila_de_espera = []
processos_encerrados = []
primeiros_processos = []
tempo_atual = 0
tempo_de_espera = 0
tempo_de_resposta = 0
num_processos = len(processos)
tempo_de_chegada_primeiro_processo = processos[0]["tempo_de_chegada"]

# loop while que executa os processos enquanto houver processos na fila de espera
while len(processos_encerrados) < num_processos:

  # loop for para adicionar os primeiros processos na fila de espera
  if len(processos) > 0:
    for processo_executa in processos:
      if processo_executa["tempo_de_chegada"] <= tempo_atual and processo_executa not in fila_de_espera and not processo_executa["tempo_restante"] == 0:
        fila_de_espera.append(processo_executa)
      
      # capturando o primeiro processo a ser executado para evitar que o tempo de espera seja contabilizado errado
      if tempo_atual == tempo_de_chegada_primeiro_processo and processo_executa["tempo_de_chegada"] == tempo_de_chegada_primeiro_processo:
        primeiros_processos.append(processo_executa)

  # se não houver processos na fila de espera, avança o tempo e volta para o inicio do loop
  if len(fila_de_espera) == 0:
    tempo_atual = tempo_atual + 1
    continue
  
  # retirando o processo da fila de espera e executando
  processo = fila_de_espera.pop(0)
  tempo_final = executa_processo(processo, tempo_atual)

  # adicionando novos processos na fila de espera que chegaram durante a execução do último processo
  if len(processos) > 0:
    for novo_processo in processos:
      if novo_processo["tempo_de_chegada"] <= tempo_final and novo_processo not in fila_de_espera and not novo_processo["tempo_restante"] == 0 and not novo_processo["pid"] == processo["pid"]:
        fila_de_espera.append(novo_processo)

  if len(fila_de_espera) > 0:
    # somando o tempo de espera dos processos que estão na fila de espera
    for proc in fila_de_espera:
      # verifica se o processo é o primeiro a ser executado e calcula o tempo de espera, senão calcula o tempo de espera normalmente
      if proc["tempo_de_espera"] == None and proc["tempo_de_chegada"] == tempo_de_chegada_primeiro_processo and proc in primeiros_processos and proc["tempo_de_resposta"] != None:
        proc["tempo_de_espera"] = tempo_final - tempo_atual
      elif proc["tempo_de_espera"] == None:
        proc["tempo_de_espera"] = tempo_final - proc["tempo_de_chegada"]
      else:
        proc["tempo_de_espera"] = proc["tempo_de_espera"] + (tempo_final - tempo_atual)

  # verifica se o processo foi concluído, caso contrário, adiciona-o novamente na fila de espera
  if processo["tempo_restante"] == 0:
    if processo["tempo_de_espera"] == None:
      processo["tempo_de_espera"] = 0
    processos_encerrados.append(processo)
  else:
    fila_de_espera.append(processo)
    
  tempo_atual = tempo_final

# calculando os tempos de retorno, resposta e espera
tempo_medio_de_retorno = [pp1["tempo_de_finalizacao"] - pp1["tempo_de_chegada"] for pp1 in processos_encerrados]
tempo_medio_de_resposta = [pp2["tempo_de_inicio"] - pp2["tempo_de_chegada"] for pp2 in processos_encerrados]
tempo_medio_espera = [pp3["tempo_de_espera"] for pp3 in processos_encerrados]

# imprimindo os resultados
print(f"RR {sum(tempo_medio_de_retorno) / len(tempo_medio_de_retorno):.1f} {sum(tempo_medio_de_resposta) / len(tempo_medio_de_resposta):.1f} {sum(tempo_medio_espera) / len(tempo_medio_espera):.1f}")