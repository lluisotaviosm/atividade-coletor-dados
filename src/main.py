from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
import os
os.makedirs("data", exist_ok=True)
LOGGER.setLevel(logging.WARNING)

def coletar_brasileirao_2024():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    site = 'https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/2024'
    driver.get(site)
    time.sleep(15)

    tabelas = driver.find_elements(By.CSS_SELECTOR, "table")
    print(f"Quantidade de tabelas encontradas: {len(tabelas)}")

    # Tabela 2: nomes dos times
    tabela_times = tabelas[2]
    times = []
    linhas_times = tabela_times.find_elements(By.CSS_SELECTOR, "tbody tr")
    for linha in linhas_times:
        texto = linha.text.strip()
        if texto and texto[0].isdigit() and len(texto.split()) > 1:
            # Exemplo: "1° BOT"
            times.append(texto.split()[1])
        elif texto and not texto[0].isdigit():
            # Exemplo: "BOT"
            times.append(texto)

    # Tabela 3: dados dos times
    tabela_dados = tabelas[3]
    linhas_dados = tabela_dados.find_elements(By.CSS_SELECTOR, "tbody tr")
    dados = []
    for linha in linhas_dados:
        texto = linha.text.strip()
        if texto:
            dados.append(texto.split())

    driver.quit()

    # Juntar times e dados
    resultado = []
    for i in range(min(len(times), len(dados))):
        # Ajuste conforme a ordem das colunas do site
        estat = dados[i]
        resultado.append({
            "Posição": i+1,
            "Time": times[i],
            "Pontos": estat[0],
            "Jogos": estat[1],
            "Vitórias": estat[2],
            "Empates": estat[3],
            "Derrotas": estat[4],
            "Gols Pró": estat[5],
            "Gols Contra": estat[6],
            "Saldo de Gols": estat[7],
            "Aproveitamento (%)": estat[8]
        })

    df = pd.DataFrame(resultado)
    df.to_csv("data/tabela_brasileirao_2024.csv", index=False, encoding="utf-8-sig")
    return resultado

if __name__ == "__main__":
    resultado = coletar_brasileirao_2024()
    for time in resultado:
        print(
            f"Posição: {time['Posição']} | "
            f"Time: {time['Time']} | "
            f"Pontos: {time['Pontos']} | "
            f"Gols Pró: {time['Gols Pró']} | "
            f"Vitórias: {time['Vitórias']} | "
            f"Derrotas: {time['Derrotas']}"
        )