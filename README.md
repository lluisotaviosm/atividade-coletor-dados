# 📊 Brasileirão Série A - Scraper

## 📝 5W1H

### 🔹 What (O quê?)
Um projeto em **Python** que acessa a tabela do **Campeonato Brasileiro Série A** no site do [UOL Esporte](https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/2024), coleta os dados da classificação (posição, time, pontos, jogos, vitórias, empates, derrotas, gols pró, gols contra, saldo de gols e aproveitamento) e exporta tudo em um arquivo **`.csv`** para consulta posterior.

---

### 🔹 Why (Por quê?)
Para **automatizar a coleta de informações esportivas**, evitando a necessidade de copiar manualmente os dados do site.  
O CSV gerado pode ser usado em:
- 📈 Dashboards de análise  
- 🎓 Estudos acadêmicos  
- 📰 Jornalismo esportivo  
- 🤖 Projetos de ciência de dados e aprendizado de máquina  

---

### 🔹 Who (Quem?)
Desenvolvido para fins **didáticos e de prática em web scraping**.  
Pode ser utilizado por:
- Estudantes de programação  
- Entusiastas de dados e esportes  
- Jornalistas esportivos  
- Pesquisadores e analistas de dados  

---

### 🔹 Where (Onde?)
- Funciona em **qualquer máquina com Python 3.10+** (Windows, Linux ou macOS).  
- Os dados são coletados diretamente do site **UOL Esporte**.  

---

### 🔹 When (Quando?)
- Pode ser executado **sob demanda**, sempre que o usuário quiser atualizar a tabela.  
- O arquivo `tabela_brasileirao_2024.csv` será **recriado a cada execução**.  

---

### 🔹 How (Como?)

#### 🛠️ Tecnologias usadas
- [Python](https://www.python.org/)  
- [Selenium](https://www.selenium.dev/) → acesso e coleta dos dados do site  
- [Pandas](https://pandas.pydata.org/) → organização e exportação para CSV  

#### 📂 Estrutura do projeto
atividade-coletor-dados/
├─ src/
│ ├─ main.py # Script principal - coleta e gera CSV
│ └─ top10_brasileirao.py # Exemplo de leitura e exibição do CSV
├─ data/
│ └─ tabela_brasileirao_2024.csv # Arquivo gerado automaticamente
├─ requirements.txt
└─ README.md

---

## 🚀 Como rodar o projeto

### 1️⃣ Clone o repositório:
```bash
git clone https://github.com/lluisotaviosm/atividade-coletor-dados.git
cd atividade-coletor-dados

2️⃣ Instale as dependências:
pip install -r requirements.txt

3️⃣ Execute o coletor:
python src/main.py
➡️ Isso vai criar o arquivo data/tabela_brasileirao_2024.csv.

4️⃣ Visualize os 10 primeiros colocados:
python src/top10_brasileirao.py

📌 Observações
Certifique-se de ter o Google Chrome e o ChromeDriver compatíveis instalados para que o Selenium funcione corretamente.
Caso use outro navegador, ajuste a configuração no main.py.

📜 Licença
Este projeto é de uso didático e está disponível sob a licença MIT.