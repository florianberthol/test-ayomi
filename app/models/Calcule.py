from pydantic import BaseModel, constr

class Calcule(BaseModel):
    operation: constr(pattern=r"^[0-9 +-/*]+$")