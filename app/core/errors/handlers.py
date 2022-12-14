from fastapi import status
from fastapi.requests import Request
from fastapi.responses import ORJSONResponse
from fastapi.exceptions import ValidationError
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.exceptions import HTTPException
from app.core.schemas.errors import Error, ErrorList
from app.core.errors.errors import ManagedErrors


async def http_exception_hander(req: Request, exc: HTTPException) -> ORJSONResponse:
    if isinstance(exc.errors, Error):
        exc.errors = ErrorList().append(exc.errors)

    return ORJSONResponse(
        content=jsonable_encoder(exc.errors),
        status_code=exc.status_code,
    )


async def request_validation_exception_handler(
    req: Request, exc: ValidationError
) -> ORJSONResponse:
    bad_request_exc = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        errors=ManagedErrors.bad_request,
    )
    return await http_exception_hander(req, bad_request_exc)


async def starlette_http_exception_handler(
    req: Request, exc: StarletteHTTPException
) -> ORJSONResponse:
    try:
        error = ManagedErrors.basic_error_responses[str(exc.status_code)]
    except KeyError:
        not_managed_exc = HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            errors=ManagedErrors.internal_server_error,
        )
        return await http_exception_hander(req, not_managed_exc)
    else:
        managed_exc = HTTPException(
            status_code=exc.status_code,
            errors=error,
        )
        return await http_exception_hander(req, managed_exc)
