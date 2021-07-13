from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn
import pandas as pd
import json

app = FastAPI(title="Data for House Price Prediction")


@app.get(
    "/get_train_set",
    response_description="Return data frame with data",
    description="Get dataframe with train set for House Price Prediction.",
)
async def get():
    try:       
        df_train = pd.read_csv('data/train.csv')
        train_set_json = df_train.to_dict()
    except:
        print("file not found")
    return train_set_json

@app.get(
    "/get_test_set",
    response_description="Return data frame with data",
    description="Get dataframe with train set for House Price Prediction.",
)
async def get():
    try:       
        df_test = pd.read_csv('data/test.csv')
        test_set_json = df_test.to_dict()
    except:
        print("file not found")       
    return test_set_json
    
# @app.post(
#     "/add",
#     response_description="Added phrase with *id* parameter",
#     response_model=PhraseOutput,
# )
# async def add(phrase: PhraseInput):
#     phrase_out = db.add(phrase)
#     return phrase_out

# @app.delete("/delete", response_description="Result of deleting")
# async def delete(id: int):
#     try:
#         db.delete(id)
#     except ValueError as e:
#         raise HTTPException(404, str(e))
