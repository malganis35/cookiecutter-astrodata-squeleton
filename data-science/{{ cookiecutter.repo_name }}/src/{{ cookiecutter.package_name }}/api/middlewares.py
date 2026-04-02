import os
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from loguru import logger

class LimitUploadSizeMiddleware(BaseHTTPMiddleware):
    """
    Middleware to limit the size of incoming requests.
    Rejects requests with a Content-Length greater than the specified limit.
    """
    def __init__(self, app, max_upload_size: int = None):
        super().__init__(app)
        # Default to 50MB if not specified
        self.max_upload_size = max_upload_size or int(os.getenv("API_MAX_UPLOAD_SIZE", 52428800))

    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("content-length")
        
        if content_length:
            if int(content_length) > self.max_upload_size:
                logger.warning(f"Request too large: {content_length} bytes (limit: {self.max_upload_size})")
                return JSONResponse(
                    status_code=413,
                    content={
                        "detail": f"Request entity too large. Maximum allowed size is {self.max_upload_size} bytes."
                    }
                )
        
        return await call_next(request)
