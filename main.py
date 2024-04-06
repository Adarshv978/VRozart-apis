from fastapi import FastAPI
from config.Database import get_db_connection
from routes.route import router
app = FastAPI()

app.include_router(router=router)



