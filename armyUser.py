from pydantic import BaseModel

class armyUser(BaseModel):
    Age: int
    Gender: int
    OL: int
    AL: int
