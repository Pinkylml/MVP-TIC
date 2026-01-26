#!/bin/bash

# Build the docker image
echo "🔨 Building Docker image..."
docker build -t employability-predictor-mvp .

# Run the container
echo "🚀 Running container on port 8000..."
docker run -p 8000:8000 employability-predictor-mvp
