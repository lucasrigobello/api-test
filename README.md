# Classificação de Cards de Gods Unchained - API com FastAPI
[![Test](https://github.com/lucasrigobello/api-test/actions/workflows/main.yml/badge.svg)](https://github.com/lucasrigobello/api-test/actions/workflows/main.yml)
[![Docker Image CI](https://github.com/lucasrigobello/api-test/actions/workflows/docker-image.yml/badge.svg)](https://github.com/lucasrigobello/api-test/actions/workflows/docker-image.yml)

## 📌 Sobre o projeto
Esta API foi desenvolvida para classificar os cards do jogo **Gods Unchained** como **"early game"** ou **"late game"** com base em atributos como **mana, attack, health, type e god**. O modelo treinado utiliza técnicas de machine learning para realizar essa predição e é exposto publicamente através de uma API criada com **FastAPI**.

<p align="center">
<img src="https://github.com/lucasrigobello/api-test/blob/2baa1a8ca8df33e58629a8102c4710c56a577a68/images/gods-unchained-cover.jpg?raw=true" width="450">
</p>

## 🚀 Tecnologias utilizadas
- **Python** (para implementação do modelo e da API)
- **FastAPI** (para exposição do modelo via API REST)
- **Scikit-learn** ( para framework para machine learning)
- **Docker** (para conteinerização da aplicação)
- **Kubernetes** (para orquestração e deploy)
- **Swagger** (para documentação da API)
- **Pytest** (para testes unitários)

## 📂 Estrutura do projeto
```bash
├── src
│   ├── models/          # Código relacionado ao treinamento do modelo
│   ├── api/             # Código da API em FastAPI
│   ├── config/          # Configurações gerais do projeto
│   ├── tests/           # Testes unitários
│   ├── train.py         # Script para treinar o modelo
│   ├── main.py          # Ponto de entrada da API
│   └── requirements.txt # Dependências do projeto
├── data/
│   ├── train.csv        # Dataset de treino
│   ├── test.csv         # Dataset de teste
├── Dockerfile           # Configuração do container Docker
├── kubernetes/          # Manifests para deploy no Kubernetes
├── README.md            # Documentação do projeto
└── .gitignore           # Arquivos ignorados no repositório Git
````

## 🛠 Como configurar o projeto
1.	Clone este repositório:

```bash
git clone <url_do_repositorio>
cd <nome_do_projeto>
````

2.	Crie um ambiente virtual e instale as dependências:
```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
pip install -r src/requirements.txt
```

3.	Para treinar o modelo:
```bash
python src/train.py
```

4.  Para iniciar a API:
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## 🖥️ Utilização da API
A API expõe um endpoint para prever a estratégia de um card:

- **GET** ```/predict/{id}``` 
    - **Parâmetros:** ```id``` (ID do card a ser classificado)
    - **Retorno:** ```{"strategy": "early"}``` ou ```{"strategy": "late"}```


Exemplo de requisição:
```bash
curl -X GET "http://localhost:8000/predict/123"
```

## 📦 Executando com Docker
Para construir e executar o container:
```bash
docker build -t gods-unchained-api .
docker run -p 8000:8000 gods-unchained-api
```

## ☁️ Deploy no Kubernetes
Para implantar no Kubernetes, use os manifests disponíveis na pasta ```kubernetes/```:
```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

## 🧪 Testes unitários
Os testes podem ser executados via ```pytest```:
```bash
pytest src/tests/
```

## 📖 Documentação
A documentação da API pode ser acessada via Swagger em:
```
http://localhost:8000/docs
```

## 📜 Licença
Este projeto está sob a licença MIT.
________________________________________

## 📊 Análise Exploratória de Dados - EDA
### Análise de features numéricas
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>mana</th>
      <td>788.0</td>
      <td>3.572335</td>
      <td>2.190100</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>16.0</td>
    </tr>
    <tr>
      <th>attack</th>
      <td>788.0</td>
      <td>2.140863</td>
      <td>2.215047</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>13.0</td>
    </tr>
    <tr>
      <th>health</th>
      <td>788.0</td>
      <td>2.583756</td>
      <td>2.455053</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>17.0</td>
    </tr>
  </tbody>
</table>
