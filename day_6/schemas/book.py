from pydantic import BaseModel
class bookcreate(BaseModel):
    title : str
    author : str

class bookresponses(BaseModel):
    id : int
    title : str
    author : str