# Classificação de Cards de Gods Unchained - API com FastAPI

<img src="https://github.com/lucasrigobello/api-test/blob/134c76946e3cc86d5662467093dc2302b91c3f3c/images/gods-unchained-coverjpg.jpg?raw=true" width="450">

## 📌 Sobre o projeto
Esta API foi desenvolvida para classificar os cards do jogo **Gods Unchained** como **"early game"** ou **"late game"** com base em atributos como mana, **attack, health, type e god**. O modelo treinado utiliza técnicas de machine learning para realizar essa predição e é exposto publicamente através de uma API criada com **FastAPI**.

<p align="center">
<img src="https://github.com/lucasrigobello/api-test/blob/134c76946e3cc86d5662467093dc2302b91c3f3c/images/gods-unchained-cover.jpg?raw=true" width="450">
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
