# Create and Search Memories for A-Mem using n8n

## Overview
This repository contains an n8n application consisting of two workflows: a main workflow and a sub-workflow. The main workflow extracts sections of text from a web URL or a PDF and stores them as memories in A-Mem, with AI-generated tags for better organization and retrieval.

## Setup Instructions

### 1. Build and Run Required Containers
Before starting, ensure all required containers are built and running. The following containers need to be set up:

- **n8n** (Built from `self-hosted-ai-starter-kit` directory)
- **Docling API** (Named `docling-api`)
- **A-Mem API** (Named `amem-container`)

#### Create a Docker Network
```sh
docker network create n8n-network
```

#### Build and Run Docling API
Navigate to the `docling-api` directory and build the container:
```sh
cd docling-api
docker build -t docling-api .
```
Run the container and connect it to the network:
```sh
docker run -d --name docling-api --network n8n-network -p 8081:8081 docling-api
```

#### Build and Run A-Mem API
Navigate to the `amem-api` directory and build the container:
```sh
cd amem-api
docker build -t amem-api .
```
Run the container and connect it to the network:
```sh
docker run -d --name amem-container --network n8n-network -p 9000:9000 amem-api
```

#### Build and Run n8n
Navigate to the `self-hosted-ai-starter-kit` directory and build the n8n container:
```sh
cd self-hosted-ai-starter-kit
docker build -t my-custom-n8n .
```
Run the n8n container and connect it to the network:
```sh
docker run -d --name n8n --network n8n-network -p 5678:5678 n8n-image
```

### 2. Verify HTTP Node URLs in n8n
After importing the workflow, ensure that:
- The **A-Mem API HTTP node** has the correct URL (`http://amem-container:9000/memories`).
- The **Convert File HTTP node** has the correct URL for Docling (`http://docling-api:8081/process`).

### 3. Configure Google Drive Credentials
If processing Google Drive links, set up Google Drive credentials in n8n and apply them to relevant nodes.

## Usage
- Upload a **web URL** or a **Google Drive link**—memories will be created automatically.
- To **search memories by ID or query**, run the respective HTTP nodes manually.

---


