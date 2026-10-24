# AI Model Benchmark — Architecture

## Overview
The platform benchmarks the performance and task-specific accuracy of locally executed Large Language Models.

## Main components

**1. Streamlit Dashboard**

Provides the user interface for selecting models, configuring benchmark runs and visualizing results.

**2. FastAPI Backend**

Receives and validates HTTP requests, invokes the benchmark engine and exposes stored results.

**3. Benchmark Engine**

Coordinates model executions, measures latency and token throughput, and evaluates answers against reference data.

**4. Ollama Client**

Handles communication with the local Ollama server to execute prompts and retrieve model output and timing metrics.

**5. SQLite Database**

Stores benchmark configurations, individual model executions and historical results.

## Benchmark execution flow

1. The user configures a benchmark through Streamlit.
2. FastAPI validates the request with Pydantic.
3. The benchmark engine executes prompts through Ollama.
4. The engine calculates and records metrics.
5. Results are persisted in SQLite.
6. Streamlit requests the results and displays comparative charts.

## Design decisions

- Python is the primary programming language.
- FastAPI separates HTTP concerns from benchmarking logic.
- Pydantic validates the structure of benchmark requests and results.
- SQLite keeps the initial deployment lightweight.
- Streamlit makes it possible to develop a dashboard without a separate JavaScript frontend.
- Benchmarks will execute models sequentially to reduce resource contention.
- Benchmark settings and hardware information should be recorded to support reproducible comparisons.

## Planned extensions

Cloud LLM providers, advanced evaluation metrics, resource monitoring and distributed execution may be considered after the first release.
