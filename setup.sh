#!/bin/bash

if command -v docker >/dev/null 2>&1; then
    echo "docker is installed."
else
    echo "docker is not installed."
    exit 1
fi


if command -v featureform >/dev/null 2>&1; then
    echo "featureform is installed."
else
    echo "featureform is not installed."
    exit 1
fi

featureform deploy docker --quickstart --include_clickhouse
docker run -p 8000:5000 --name mlflow -d ghcr.io/mlflow/mlflow:latest mlflow server --host 0.0.0.0
