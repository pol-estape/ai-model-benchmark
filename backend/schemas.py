from datetime import datetime, timezone

from pydantic import BaseModel, Field


# Request payload sent by the dashboard or API client to start a benchmark run.
class BenchmarkRequest(BaseModel):
    # The model names to benchmark. At least one model is required.
    models: list[str] = Field(min_length=1)

    # The prompt texts to send to each selected model. At least one prompt is required.
    prompts: list[str] = Field(min_length=1)

    # Number of times to repeat each benchmark test. Must stay within a reasonable range.
    repetitions: int = Field(default=3, ge=1, le=20)

    # Sampling temperature for model generation. Lower values are more deterministic.
    temperature: float = Field(default=0.0, ge=0.0, le=2.0)


# Recorded output for one model response during a benchmark execution.
class BenchmarkResult(BaseModel):
    # Name of the model that produced this result.
    model: str

    # Prompt used for the test run.
    prompt: str

    # Raw model response text.
    response: str

    # Total time taken to complete the request, in seconds.
    latency_seconds: float = Field(ge=0)

    # Number of input tokens consumed by the model.
    input_tokens: int = Field(ge=0)

    # Number of tokens generated in the output.
    output_tokens: int = Field(ge=0)

    # Calculated model throughput, measured as generated tokens per second.
    tokens_per_second: float = Field(ge=0)

    # Whether the answer is considered correct, if that evaluation is available.
    correct: bool | None = None

    # UTC timestamp marking when this result was recorded.
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
