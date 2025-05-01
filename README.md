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

https://github.com/lucasrigobello/api-test/blob/86be48baa8a1ad4f51b8f01a1a59cdee42ed9f75/notebook/EDA%20Results/test.html

<iframe id="content" src=[https://github.com/lucasrigobello/api-test/blob/22c7ca8a5a0e1cd9244bb06866e87a81740c93d0/notebook/EDA%20Results/test.html](https://github.com/lucasrigobello/api-test/blob/06832d10266b33fddd98b51389d335a0c435d0e4/notebook/EDA%20Results/test.html) width="100%" height="300">

