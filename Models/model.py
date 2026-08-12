from pydantic import BaseModel


class audioModel(BaseModel):
    audio: list[float]
    
class textModel(BaseModel):
    text: str
    
class imageModel(BaseModel):
    image: list[list[int]]
    
class videoModel(BaseModel):
    video: list[list[list[int]]]
    
class thoughtModel(BaseModel):
    thought: str
    
class feelingModel(BaseModel):
    feeling: list[float]

class queryModel(BaseModel):
    Query: audioModel | textModel | imageModel | videoModel | thoughtModel | feelingModel
    