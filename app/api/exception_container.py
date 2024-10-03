from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.service.exceptions import CharCodeNotFoundError


def exception_container(app: FastAPI) -> FastAPI:
    @app.exception_handler(CharCodeNotFoundError)
    async def auction_not_found_exception_handler(
        request: Request, exc: CharCodeNotFoundError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content={"message": str(exc)}
        )

    return app
