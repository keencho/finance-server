from contextvars import ContextVar

from starlette.types import ASGIApp, Receive, Scope, Send

REQUEST_STATE_CTX_KEY = "request_state"

_request_state_ctx_var: ContextVar[dict] = ContextVar(REQUEST_STATE_CTX_KEY, default=None)


def get_request_state() -> dict:
    return _request_state_ctx_var.get()


class RequestMiddleware:
    def __init__(
            self,
            app: ASGIApp,
    ) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] not in ["http", "websocket"]:
            await self.app(scope, receive, send)
            return

        request_state = _request_state_ctx_var.set(scope['state'])

        await self.app(scope, receive, send)

        _request_state_ctx_var.reset(request_state)