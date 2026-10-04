from __future__ import annotations
import json
import urllib.error
import urllib.request
from dataclasses import dataclass


@dataclass(frozen=True)
class NebiusResponse:
    status: int
    body: dict


class TokenFactoryClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.tokenfactory.nebius.com",
        timeout: float = 60.0,
    ) -> None:
        if not api_key:
            raise ValueError("NEBIUS_API_KEY is required")
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def chat(self, *, model: str, prompt: str, temperature: float = 0.0) -> NebiusResponse:
        payload = json.dumps(
            {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": temperature,
            }
        ).encode("utf-8")
        req = urllib.request.Request(
            f"{self.base_url}/v1/chat/completions",
            data=payload,
            method="POST",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "User-Agent": "frequency-nebius-assurance/0.1",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return NebiusResponse(
                    response.status,
                    json.loads(response.read().decode("utf-8")),
                )
        except urllib.error.HTTPError as error:
            raw = error.read().decode("utf-8", errors="replace")
            try:
                body = json.loads(raw)
            except json.JSONDecodeError:
                body = {"error": raw}
            return NebiusResponse(error.code, body)
