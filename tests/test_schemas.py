
import pytest
from pydantic import ValidationError

from backend.schemas import BenchmarkRequest, BenchmarkResult


def test_valid_benchmark_request():
    request = BenchmarkRequest(
        models=["qwen3:4b"],
        prompts=["What is 2 + 2?"]
    )

    assert request.repetitions == 3
    assert request.temperature == 0.0


def test_empty_models_rejected():
    with pytest.raises(ValidationError):
        BenchmarkRequest(
            models=[],
            prompts=["What is 2 + 2?"]
        )


def test_invalid_repetitions_rejected():
    with pytest.raises(ValidationError):
        BenchmarkRequest(
            models=["qwen3:4b"],
            prompts=["What is 2 + 2?"],
            repetitions=0
        )


def test_negative_latency_rejected():
    with pytest.raises(ValidationError):
        BenchmarkResult(
            model="qwen3:4b",
            prompt="What is 2 + 2?",
            response="4",
            latency_seconds=-1,
            input_tokens=10,
            output_tokens=2,
            tokens_per_second=5.0
        )
