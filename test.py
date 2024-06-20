from pydantic import BaseModel

class MyModel(BaseModel):
    name: str

model = MyModel(name="test")
print(model)
