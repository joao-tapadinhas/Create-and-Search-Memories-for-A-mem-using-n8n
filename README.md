# Create and Search Memories for A-Mem using n8n

## Overview
This repository contains an n8n application consisting of two workflows: a main workflow (Section_loading_to_A_mem.json) and a sub-workflow(Tool_Remove_Irrelevant_Sections.json). The main workflow extracts sections of text from a web URL or a PDF and stores them as memories in A-Mem, with AI-generated tags for better organization and retrieval.

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
docker build -t n8n-image .
```
Run the n8n container and connect it to the network:
```sh
docker run -d --name n8n --network n8n-network -p 5678:5678 n8n-image
```

### 2. Import Workflows into n8n
Before verifying HTTP node URLs, import the following workflows into n8n:
- **Section_loading_to_A_mem.json**
- **Tool_Remove_Irrelevant_Sections.json**

### 3. Verify HTTP Node URLs in n8n
After importing the workflow, ensure that:
- The **A-Mem API HTTP node** has the correct URL (`http://amem-container:9000/memories`).
- The **Convert File HTTP node** has the correct URL for Docling (`http://docling-api:8081/process`).

### 4. Configure Google Drive Credentials
If processing Google Drive links, set up Google Drive credentials in n8n and apply them to relevant nodes.

## Usage
- Upload a **web URL** or a **Google Drive link**—memories will be created automatically.
- To **search memories by ID or query**, run the respective HTTP nodes manually.

---

## Keeping This Fork in Sync with the Original Repository

This is a fork of [Abdullah's repository](https://github.com/abdullah91111/Create-and-Search-Memories-for-A-mem-using-n8n). To keep it in sync with the original repository:

### Using GitHub's Web Interface

1. Navigate to this fork on GitHub
2. Click on "Sync fork" button (located above the file list)
3. Click "Update branch" to sync with the original repository

### Using Git Commands

If you've cloned this repository locally:

1. Add the original repository as an upstream remote:
   ```bash
   git remote add upstream https://github.com/abdullah91111/Create-and-Search-Memories-for-A-mem-using-n8n.git
   ```

2. Fetch and merge changes:
   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   git push origin main
   ```

For more detailed instructions on keeping your fork in sync, see [GitHub's documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).