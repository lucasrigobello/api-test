import uvicorn
from fastapi import FastAPI, File, UploadFile
"""
import pandas as pd
import joblib

# from sklearn.preprocessing import OneHotEncoder
from utils.functions import preparar_dado_predict, preparar_dado_trainamento
from sklearn.svm import SVC

"""
description = """
Para se preparar para o jogo Gods Unchained, utilize desta ferramenta de classificar
de estratégia do card, entre “early” ou “late” game.
O ID do cardo deve ser utilizado para as requisições da classificação, atraves da rota **/predict**.


O dataset contendo informações relacionadas aos cards de Gods Unchained, utilizado no treinmaento do modelo 
de classificação toma como base as features “mana”, “attack”, “health”, “type” e “god”.
"""
"""
tags_metadata = [
    {
        "name": "predict",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "fit",
        "description": "Manage items. So _fancy_ they have their own docs.",
    },
    {
        "name": "Hello World",
        "description": "Teste inicial de Hello World"
    }
]
"""
app = FastAPI()
"""
        title="Gods Unchained - Chanlange",
        summary="Classificador de *strategy**",
        description=description,
        version="0.0.1",
        contact={
            "name": "Lucas Rigobello",
            # "url": "http://x-force.example.com/contact/",
            "email": "dp@x-force.example.com",
        },
        license_info={
            "name": "GitHub repositorio",
            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
        openapi_tags=tags_metadata
    )

#===========================================
# Rota da Prediçao da Classificação do Card
@app.get("/predict/{id}", tags=["predict"])
async def predict(id):

    # carregar o dado para o predict    
    X = preparar_dado_predict(id)
    
    # carregar o modelo e fazer predição
    clf = joblib.load("./models/Classification_model.pkl") 
    pred = clf.predict(X)

    return {'prediction': pred[0]}

#===========================================
# Rota para upload de dataset de treinmaento
@app.post("/upload_train_data", tags=["fit"])
async def uploupload_train_data(file: UploadFile):
    df_train = pd.read_csv(file.file)

    df_train.to_csv('./dataset/challenge_train.csv', sep = ';', index=False)

    return {"filename": file.filename}

#===========================================
# Rota para realizar o Treinamneto do Modelo
@app.get("/fit", tags=["fit"])
async def fit():

    # carregar o dado para o treinamento
    X_train, X_test, y_train, y_test = preparar_dado_trainamento()

    # treinamento
    clf = SVC(gamma='auto')
    clf.fit(X_train, y_train)
    # save Classification Model
    joblib.dump(clf, "./models/Classification_model.pkl") 

    return {"Treinamento": "Executado com Sucesso",
            "Score treinamento": clf.score(X_train, y_train),
            "Score test": clf.score(X_test, y_test)}
"""
#===========================================
# Rota da Prediçao da Classificação do Card
@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=81)