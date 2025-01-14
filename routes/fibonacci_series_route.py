import os
import sys
from fastapi import APIRouter
from fastapi.responses import JSONResponse

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from application.usecase import FibonacciSeriesUsecase

app = APIRouter()

@app.get('/fib')
def read_root(n : str = None):
    try:
        fibonacci_series_usecase = FibonacciSeriesUsecase(n).execute()
        return {'result': fibonacci_series_usecase}
    
    except Exception as e:
        return JSONResponse(status_code=400, content={'status': 400, 'message': str(e)})