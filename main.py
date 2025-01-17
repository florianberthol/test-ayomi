from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.services.RnpCalculator import rnpCalculator
from app.models.Calcule import Calcule
from app.services.Logs import Logs

app = FastAPI()

@app.post("/calcule")
def rnp(calcule: Calcule):
    calculator = rnpCalculator()
    logs = Logs()
    try :
        result = calculator.process(calcule.operation.split())
    except:
        return 'Invalid calculation : ' + calcule.operation

    logs.log({'result':result, 'operation':calcule.operation});

    return {"result": result}

@app.get("/dump")
def dump():
    logs = Logs()

    dump = logs.dump()

    response = StreamingResponse(dump, media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=dump.csv"
    return response