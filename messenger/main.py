from fastapi import FastAPI
import uvicorn

from endpoints.login import router as login_router
from endpoints.user import router as user_router
from endpoints.utils import router as utils_router

app = FastAPI()

app.include_router(user_router, tags=["user"])
app.include_router(login_router, tags=["login"])
app.include_router(utils_router, tags=["utils"])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8080,
        reload=True,
        debug=True,
    )
