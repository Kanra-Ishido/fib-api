import os
import sys
from fastapi import FastAPI
from mangum import Mangum

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from routes import fibonacci_series_route as fibonacci_series_route

app = FastAPI()

app.include_router(fibonacci_series_route.app, prefix='/fibonacci_series')

handler = Mangum(app)