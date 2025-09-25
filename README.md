# atividade-coletor-dados

# 5W1H

# **What (O quê?)**

Um projeto em **Python** que acessa a tabela do **Campeonato Brasileiro Série A** no site do UOL, coleta os dados da classificação (posição, time, pontos, jogos, vitórias, empates, derrotas, gols pró, gols contra, saldo de gols e aproveitamento) e exporta tudo em um arquivo ".csv" para consulta posterior.



# **Why (Por quê?)**

Para **automatizar** a coleta de informações esportivas, evitando a necessidade de copiar manualmente os dados do site. O CSV gerado pode ser usado em análises, dashboards, estudos acadêmicos ou projetos de ciência de dados.



# **Who (Quem?)**

* Desenvolvido para fins **didáticos** e de prática em **web scraping**.
* Pode ser usado por estudantes, entusiastas de programação, jornalistas esportivos ou qualquer pessoa que queira trabalhar com dados do Brasileirão.



# **Where (Onde?)**

* O código roda em qualquer máquina com **Python 3.10+** (Windows ou Linux).
* Os dados são coletados do site público do **UOL Esporte**:
 https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/2024



# **When (Quando?)**

* Pode ser executado **sob demanda**, sempre que o usuário quiser atualizar a tabela do campeonato.
* O arquivo "tabela_brasileirao_2024.csv" será recriado a cada execução.



# **How (Como?)**

* Tecnologias usadas:

  * Python
  * Selenium (para acessar o site e coletar os dados)
  * Pandas (para organizar e exportar os dados)

* Estrutura do projeto:

  brasileirao-scraper/
  ├─ src/
  │  ├─ main.py              # Script principal - coleta e gera CSV
  │  └─ top10_brasileirao.py # Exemplo de leitura e exibição do CSV
  ├─ data/
  │  └─ tabela_brasileirao_2024.csv  # Arquivo gerado automaticamente
  ├─ requirements.txt
  └─ README.md

* Passos para rodar:

  1. Clone o repositório:

     git clone https://github.com/<seu-usuario>/brasileirao-scraper.git  
     cd brasileirao-scraper

  2. Instale as dependências:

     pip install -r requirements.txt

  3. Execute o coletor:

     python src/main.py

  4. O arquivo "data/tabela_brasileirao_2024.csv" será criado.

  5. Para visualizar os 10 primeiros colocados:

     python src/top10_brasileirao.py