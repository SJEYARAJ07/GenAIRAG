from fastapi import APIRouter, HTTPException
from app.schemas import QueryRequest, QueryResponse
from app.rag.chain import get_answer

router = APIRouter()


@router.post("/ask", response_model=QueryResponse)
def ask(req: QueryRequest):
    query = req.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    try:
        answer = get_answer(query)
        return QueryResponse(answer=answer)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))