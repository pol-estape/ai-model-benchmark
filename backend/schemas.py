
from datetime import datetime, timezone

from pydantic import BaseModel, Field


class BenchmarkRequest(BaseModel):
    models: list[str] = Field(min_length=1)
    prompts: list[str] = Field(min_length=1)
    repetitions: int = Field(default=3, ge=1, le=20)
    temperature: float = Field(default=0.0, ge=0.0, le=2.0)


class BenchmarkResult(BaseModel):
    model: str
    prompt: str
    response: str

    latency_seconds: float = Field(ge=0)
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)
    tokens_per_second: float = Field(ge=0)

    correct: bool | None = None
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
