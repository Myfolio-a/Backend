# API messages

from enum import Enum


class ErrorTypes(Enum):
    api_error = "api_error"
    invalid_request_error = "invalid_request_error"


WRONG_CREDENTIALS_ERROR = "이메일 또는 비밀번호를 잘못 입력했습니다. 입력하신 내용을 다시 확인해주세요."

UNAUTHORIZED_ERROR = "해당 요청을 위한 인증이 필요합니다."
FORBIDDEN_ERROR = "해당 요청에 대한 권한이 없거나 인증 정보가 유효하지 않습니다."