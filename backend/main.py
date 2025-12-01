# #from fastapi import FastAPI

# #app = FastAPI()


# #@app.get("/")
# #async def root():
#    # return {"message": "Hello World"}

#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/items/{item_id}")
#async def read_item(item_id):
 #   return {"item_id": item_id}

#app = FastAPI()


#@app.get("/users/me")
#async def read_user_me():
 #   return {"user_id": "the current user"}


#@app.get("/users/{user_id}")
#async def read_user(user_id: str):
 #   return {"user_id": user_id}

#@app.get("/users")
#async def read_users():
 #   return ["Rick", "Morty"]
#@app.get("/users")
#async def read_users2():
 #   return ["Bean", "Elfo"]

#from enum import Enum

from fastapi import FastAPI
#class ModelName(str, Enum):
 #   alexnet = "alexnet"
  # lenet = "lenet"
#app = FastAPI()
#@app.get("/models/{model_name}")
#async def get_model(model_name: ModelName):
 #   if model_name is ModelName.alexnet:
  #      return {"model_name": model_name, "message": "Deep Learning FTW!"}
# if model_name.value == "lenet":
 #       return {"model_name": model_name, "message": "LeCNN all the images"}
#  return {"model_name": model_name, "message": "Have some residuals"}

#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/files/{file_path:path}")
#async def read_file(file_path: str):
 #   return {"file_path": file_path}

#from fastapi import FastAPI

#app = FastAPI()

#fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#@app.get("/items/")
#async def read_item(skip: int = 0, limit: int = 10):
 #   return fake_items_db[skip : skip + limit]

#from fastapi import FastAPI

#app = FastAPI()
#@app.get("/items/{item_id}")
#async def read_item(item_id: str, q: str | None = None):
  #  if q:
   #     return {"item_id": item_id, "q": q}
 #   return {"item_id": item_id}

#from fastapi import FastAPI

#app = FastAPI()


#@app.get("/items/{item_id}")
#sync def read_item(item_id: str, q: str | None = None, short: bool = False):
 #   item = {"item_id": item_id}
  #  if q:
   #     item.update({"q": q})
    #if not short:
     #   item.update(
      #      {"description": "This is an amazing item that has a long description"}
       # )
    #return item

# from fastapi import FastAPI
# from pydantic import BaseModel


# class Course_Registration(BaseModel):
#     first_name: str
#     last_name: str 
#     dob: int
#     city: str
#     phone_no:int
#     email_id:str



# app = FastAPI()


# @app.post("/items/")
# async def create_item(item: Course_Registration):
#     return item

# @app.get("/items/")
# async def create_item(item: Course_Registration):
#     return item


# from fastapi import FastAPI
# from pydantic import BaseModel

# app=FastAPI()


# @app.get("/query/")
# def query_func(first_name: str,
#     last_name: str ,
#     dob: int,
#     city: str,
#     phone_no:int,
#     email_id:str,
# ):
#   var_name={"first_name":first_name,
#             "last_name": lastname ,
#     "dob": dob,
#     "city":city,
#     "phone_no":phone_no,
#     "email_id":email_id,}
#   return(var_name)

#main.py

from fastapi import FastAPI
# from core.config import settings

# app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
#app = FastAPI()


#@app.get("/")
#def hello_api():
    #return {"msg":"Hello FastAPI🚀"}


