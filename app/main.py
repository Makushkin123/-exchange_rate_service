import logging

import uvicorn
from app.create_fastapi_app import create_app
from app.config import settings
from pythonjsonlogger import jsonlogger
from app.api.test import router

main_app = create_app()
main_app.include_router(
    router,
)

handler = logging.StreamHandler()
handler.setFormatter(
    fmt=jsonlogger.JsonFormatter(
        "%(asctime)s 	%(levelname)s %(module)s %(message)s", json_ensure_ascii=False
    )
)
logging.basicConfig(level=logging.DEBUG, handlers=(handler,))

if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )
