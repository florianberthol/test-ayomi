from pydantic import BaseModel, constr

class Calcul(BaseModel):
    operation: constr(pattern=r"^[0-9 +-/*]+$")