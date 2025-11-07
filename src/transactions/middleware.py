import os
import redis
from django.utils.deprecation import MiddlewareMixin

def get_redis_client():
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=int(os.getenv("REDIS_DB", 0)),
        decode_responses=True
    )

class RequestCounterMiddleware(MiddlewareMixin):
    KEY = "api_request_count"

    def __init__(self, get_response=None):
        super().__init__(get_response)
        self._r = get_redis_client()

    def process_request(self, request):
        # Only count API paths (optional: restrict to /api/)
        try:
            # increment returns new value
            new_count = self._r.incr(self.KEY)
            print(f"[RequestCounterMiddleware] Total API requests so far: {new_count}")
        except Exception as e:
            # fail-safe: don't break app if Redis is down
            print(f"[RequestCounterMiddleware] Redis error: {e}")
        return None
