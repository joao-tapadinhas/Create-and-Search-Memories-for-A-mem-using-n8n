from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from memory_system import AgenticMemorySystem

# Initialize FastAPI app
app = FastAPI()

# Initialize A-MEM memory system
memory_system = AgenticMemorySystem(
    model_name="all-MiniLM-L6-v2",  
    llm_backend="openai",  
    llm_model="gpt-4"
)

# Request models
class MemoryCreateRequest(BaseModel):
    content: str
    tags: Optional[List[str]] = None
    category: Optional[str] = None
    timestamp: Optional[str] = None

class MemoryUpdateRequest(BaseModel):
    content: str

class SearchRequest(BaseModel):
    query: str
    k: int = 5


# Routes

@app.post("/memories")
def add_memory(request: MemoryCreateRequest):
    """Create a new memory and return its ID."""
    memory_id = memory_system.create(
        content=request.content,
        tags=request.tags,
        category=request.category,
        timestamp=request.timestamp
    )
    return {"id": memory_id}

@app.get("/memories/{memory_id}")
def get_memory(memory_id: str):
    """Retrieve a memory by ID."""
    memory = memory_system.read(memory_id)
    if not memory:
        return {"error": "Memory not found"}
    return {
        "id": memory_id,
        "content": memory.content,
        "tags": memory.tags,
        "context": memory.context,
        "keywords": memory.keywords
    }

@app.post("/memories/search")
def search_memories(request: SearchRequest):
    """Search stored memories and return top-k results."""
    results = memory_system.search(request.query, k=request.k)
    return {"results": results}

@app.put("/memories/{memory_id}")
def update_memory(memory_id: str, request: MemoryUpdateRequest):
    """Update a memory's content."""
    memory_system.update(memory_id, request.content)
    return {"message": "Memory updated successfully"}

@app.delete("/memories/{memory_id}")
def delete_memory(memory_id: str):
    """Delete a memory."""
    memory_system.delete(memory_id)
    return {"message": "Memory deleted successfully"}
