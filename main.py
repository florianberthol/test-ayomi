from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.services.RnpCalculator import rnpCalculator
from app.models.Calcul import Calcul
from app.services.Logs import Logs

app = FastAPI()

@app.post("/calcul")
def rnp(calcul: Calcul):
    calculator = rnpCalculator()
    logs = Logs()
    try :
        result = calculator.process(calcul.operation.split())
    except:
        return 'Invalid calculation : ' + calcul.operation

    logs.log({'result':result, 'operation':calcul.operation})

    return {"result": result}

@app.get("/dump")
def dump():
    logs = Logs()

    dump = logs.dump()

    response = StreamingResponse(dump, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=dump.csv"
    return response