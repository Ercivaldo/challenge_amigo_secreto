import requests
import datetime
import pandas as pd

# Sua chave de API obtida no site
api_key = '4b8d1d79fd0e4439bbf10f73fea3f9c1'

# URL base da API do Football-Data.org
base_url = 'https://api.football-data.org/v4/'

# Cabeçalhos necessários para autenticação
headers = {'X-Auth-Token': api_key}

# Função para obter partidas de amanhã
def obter_partidas_amanha():
    # Definir data de amanhã
    hoje = datetime.date.today()
    amanha = hoje + datetime.timedelta(days=1)
    amanha_str = amanha.strftime('%Y-%m-%d')  # formato AAAA-MM-DD
    print(f"Buscando jogos para: {amanha_str}")  # Verificar a data de amanhã

    # Buscar todos os jogos
    url = f'{base_url}matches'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Filtrar os jogos de amanhã
        jogos_amanha = [jogo for jogo in data['matches'] if jogo['utcDate'].startswith(amanha_str)]
        
        if jogos_amanha:
            print(f"Jogos encontrados: {len(jogos_amanha)}")
            return jogos_amanha
        else:
            print("Nenhum jogo encontrado para amanhã.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Função para obter estatísticas do time
def obter_estatisticas_time(team_id):
    url = f'{base_url}teams/{team_id}'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        time = response.json()
        
        # Inspecionar a estrutura da resposta
        print(f"Resposta de dados do time: {time.keys()}")  # Mostrar as chaves principais
        # Verificar se a chave 'season' está presente e se contém as informações desejadas
        if 'seasons' in time and time['seasons']:
            # Assumindo que estamos pegando a primeira temporada na lista (isso pode ser ajustado)
            temporada = time['seasons'][0]
            vitorias = temporada.get('wins', 0)
            empates = temporada.get('draws', 0)
            derrotas = temporada.get('losses', 0)
            return {'vitórias': vitorias, 'empates': empates, 'derrotas': derrotas}
        else:
            print(f"Dados de temporada não encontrados para o time {team_id}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Função para calcular a probabilidade de vitória
def calcular_probabilidade(time_casa, time_visitante):
    # Estatísticas hipotéticas (essas podem ser obtidas por meio da API)
    vitorias_casa = time_casa['vitórias']
    vitorias_visitante = time_visitante['vitórias']
    
    # Vamos usar uma fórmula simples: probabilidade de vitória = vitórias no último ano / total de jogos
    probabilidade_casa = vitorias_casa / (vitorias_casa + time_casa['derrotas'])
    probabilidade_visitante = vitorias_visitante / (vitorias_visitante + time_visitante['derrotas'])
    
    # Ajustando para o fator "casa" (normalmente, jogar em casa aumenta a chance de vitória)
    probabilidade_final_casa = probabilidade_casa + 0.1  # bônus para jogar em casa
    probabilidade_final_visitante = probabilidade_visitante - 0.1  # penalização para jogar fora
    
    # Garantir que a probabilidade esteja entre 0 e 1
    probabilidade_final_casa = min(1, max(0, probabilidade_final_casa))
    probabilidade_final_visitante = min(1, max(0, probabilidade_final_visitante))
    
    return probabilidade_final_casa, probabilidade_final_visitante

# Função para calcular probabilidade de vitória para jogos de amanhã
def prever_vitoria_amanha(partidas):
    if partidas:
        for partida in partidas:
            time_casa_id = partida['homeTeam']['id']
            time_visitante_id = partida['awayTeam']['id']
            
            # Obter estatísticas dos times
            time_casa = obter_estatisticas_time(time_casa_id)
            time_visitante = obter_estatisticas_time(time_visitante_id)
            
            if time_casa and time_visitante:
                prob_casa, prob_visitante = calcular_probabilidade(time_casa, time_visitante)
                print(f"Jogo: {partida['homeTeam']['name']} vs {partida['awayTeam']['name']}")
                print(f"Probabilidade de vitória do {partida['homeTeam']['name']}: {prob_casa * 100:.2f}%")
                print(f"Probabilidade de vitória do {partida['awayTeam']['name']}: {prob_visitante * 100:.2f}%")
                print("-----")
            else:
                print(f"Não foi possível obter as estatísticas para o jogo {partida['homeTeam']['name']} vs {partida['awayTeam']['name']}.")
    else:
        print("Nenhum jogo encontrado para amanhã.")

# Obter as partidas de amanhã
partidas_amanha = obter_partidas_amanha()

# Aplicar a previsão nos jogos de amanhã
prever_vitoria_amanha(partidas_amanha)








