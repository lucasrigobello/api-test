import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

import pandas as pd
import joblib
import yaml

from utils.functions import preparar_dado_predict, preparar_dado_trainamento, validation, treinar_modelo, get_dataset

## =====================================================================
## Inicio do serviço Fast API
## =====================================================================

# Read Features Conf YAML file
with open("./app/conf/swagger_documentation.yaml", 'r', encoding='utf-8') as stream:
    conf_swagger = yaml.safe_load(stream)

# Iniciando FastAPI
app = FastAPI(**conf_swagger)

#===========================================
# Rota da Prediçao da Classificação do Card
@app.get("/classificar/{id}", tags=["Classificar"])
async def classificar(id):

    # carregar o dado para o predict    
    X = preparar_dado_predict(id)
    
    # carregar o modelo e fazer predição
    clf = joblib.load("./models/Classification_model.pkl") 
    pred = clf.predict(X)

    return {'strategy': pred[0]}

#===========================================
# Rota para upload de dataset de treinmaento
@app.post("/atualizar_base_treinamento", tags=["Base de Dados"])
async def upload_train_data(file: UploadFile):
    df_train = pd.read_csv(file.file)

    df_train.to_csv('./dataset/challenge_train.csv', sep = ';', index=False)

    return {"filename": file.filename}

#===========================================
# Rota para upload de dataset de Test
@app.post("/atualizar_base_test", tags=["Base de Dados"])
async def upload_test_data(file: UploadFile):
    df_test = pd.read_csv(file.file)

    df_test.to_csv('./dataset/challenge_test.csv', sep = ';', index=False)

    return {"filename": file.filename}

#===========================================
# Rota para realizar o Treinamneto do Modelo
@app.get("/avaliation", tags=["Avaliar Modelo"], response_class=HTMLResponse)
async def avaliation():

    # carregar o dado para o treinamento
    X, y = get_dataset()

    # carregar o modelo e fazer predição
    clf = joblib.load("./models/Classification_model.pkl") 

    return """
        <html>
            <h1>Avalição do Modelo Atual Executada com Sucesso</h1>
            <h3>Avaliação do Score</h3>
            {}
        </html>""".format(validation(y, clf.predict(X)))

#===========================================
# Rota para realizar o Treinamneto do Modelo
@app.get("/treinar", tags=["Treinar Novo Modelo"], response_class=HTMLResponse)
async def treinar():

    # carregar o dado para o treinamento
    X_train, X_test, y_train, y_test = preparar_dado_trainamento()

    # treinamento do modelo
    clf = treinar_modelo(X_train, y_train)

    return """
        <html>
            <h1>Treinamento Executado com Sucesso</h1>
            <h3>Score treinamento</h3>
            {}
            <h3>Score validação</h3>
            {}
        </html>""".format(validation(y_train, clf.predict(X_train)),
                          validation(y_test, clf.predict(X_test)))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=81)