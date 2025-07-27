import time
import threading
from typing import Callable


class RateLimiter:
    def __init__(self, seconds: int = 60, **limits: int):
        self.timeframe = seconds
        self.limits = {key: value if isinstance(value, (int, float)) else 0 for key, value in (limits or {}).items()}
        self.values = {key: [] for key in self.limits.keys()}
        self._lock = threading.Lock()

    def add(self, **kwargs: int):
        now = time.time()
        for key, value in kwargs.items():
            if not key in self.values:
                self.values[key] = []
            self.values[key].append((now, value))

    def cleanup(self):
        with self._lock:
            now = time.time()
            cutoff = now - self.timeframe
            for key in self.values:
                self.values[key] = [(t, v) for t, v in self.values[key] if t > cutoff]

    def get_total(self, key: str) -> int:
        with self._lock:
            if not key in self.values:
                return 0
            return sum(value for _, value in self.values[key])

    def wait(
        self,
        callback: Callable[[str, str, int, int], None] | None = None,
    ):
        while True:
            self.cleanup()
            should_wait = False

            for key, limit in self.limits.items():
                if limit <= 0:  # Skip if no limit set
                    continue

                total = self.get_total(key)
                if total > limit:
                    if callback:
                        msg = f"Rate limit exceeded for {key} ({total}/{limit}), waiting..."
                        callback(msg, key, total, limit)
                    should_wait = True
                    break

            if not should_wait:
                break

            time.sleep(1)
