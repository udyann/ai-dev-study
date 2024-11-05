from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field

class ModelName(str, Enum):
	alexnet = "alexnet"
	resnet = "resnet"
	lenet = "lenet"

class DataInput(BaseModel):
	name: str

app = FastAPI()

@app.get("/")
async def root():
	return {"message" : "Hello World"}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
	if model_name is ModelName.alexnet:
		return {"model_name" : model_name, "message" : "Deep Learning FTW!"}
	
	if model_name.value == "lenet":
		return {"model_name" : model_name, "message" : "LeCNN all the images"}

	return {"model_name" : model_name, "message": "Have some residuals"}

@app.post("/")
def home_post(data_request: DataInput):
	return {"Hello": "POST", "msg": data_request.name}