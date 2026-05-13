import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
#CHROMA_DIR = str(BASE_DIR / "chroma_db")
CHROMA_DIR = str(BASE_DIR / "data" / "chroma")
PDF_DIR = "data/pdfs"
#CHROMA_DIR = "data/chroma"

BGE_URL = os.getenv("BGE_URL", "https://eag-dev.aexp.com/genai/google/v1/launchpad/models/bge-large-en/embeddings")
BGE_TOKEN = os.getenv("BGE_TOKEN","eyJraWQiOiJyc2FLZVVOSUUxIiwiYWxnIjoiUlM1MTIifQ.eyJzY3AiOlsiXC9nZW5haVwvZ29vZ2xlXC92MVwvbGF1bmNocGFkXC9tb2RlbHNcL2JnZS1sYXJnZS1lblwvZW1iZWRkaW5nc1wvKio6OnBvc3QiLCJcL2dlbmFpXC9nb29nbGVcL3YxXC9sYXVuY2hwYWRcL21vZGVsc1wvbGxhbWEzXC8qKjo6cG9zdCJdLCJzdWIiOiJhOTViZDgzYi1hOTk4LTM1Y2UtYjI4ZC02ZTdkMzUzMGViYzIiLCJ2ZXIiOiIxLjAiLCJpc3MiOiJBbWV4SURhYVNJRCIsInR5cCI6ImFwcCIsImV4cCI6MTc3ODY0MjAzNSwianRpIjoiNmRiMDgxZGEtZTM2OS00OTE2LWJhYjItZTZmNWJlNDIzOGJmIn0.RL7uXGjDkdRCMyc2ekvOVOuG2LeCIon2aeTrAZVdvdtI//vW23WaFkDPkf0eheJrS1bjmoA7X/IsS9fVFC3Z9Xb+pY0SMSoHqlCMMsfuSOQqqUzR5/Ec5u7eyVSGsjQUdcZRgLGRrffVy/z/f/sfO1uSRoCoVEBRlE4vG0awWhyPcGauIxqy/mZ2hJjmEOhT80CkRh1k4dz9pmwb4ZZqQGCLn7AHJZB1R3rSOJLoZAdreTOisI9qZRM5429GntkrI4JeEfmW7IFjWEGtH3P53SHbJJTs3cgFaSd0C3aG4Liqv1UlB/PEvb/TudkW/iseMyp/YCtYLeqwMQECQGNAiA==")
LLM_URL = os.getenv("LLM_URL", "https://eag-dev.aexp.com/genai/google/v1/launchpad/models/llama3/llama3-90b/chat/completions")
LLM_TOKEN = os.getenv("LLM_TOKEN", "eyJraWQiOiJyc2FLZVVOSUUxIiwiYWxnIjoiUlM1MTIifQ.eyJzY3AiOlsiXC9nZW5haVwvZ29vZ2xlXC92MVwvbGF1bmNocGFkXC9tb2RlbHNcL2JnZS1sYXJnZS1lblwvZW1iZWRkaW5nc1wvKio6OnBvc3QiLCJcL2dlbmFpXC9nb29nbGVcL3YxXC9sYXVuY2hwYWRcL21vZGVsc1wvbGxhbWEzXC8qKjo6cG9zdCJdLCJzdWIiOiJhOTViZDgzYi1hOTk4LTM1Y2UtYjI4ZC02ZTdkMzUzMGViYzIiLCJ2ZXIiOiIxLjAiLCJpc3MiOiJBbWV4SURhYVNJRCIsInR5cCI6ImFwcCIsImV4cCI6MTc3ODY0MjAzNSwianRpIjoiNmRiMDgxZGEtZTM2OS00OTE2LWJhYjItZTZmNWJlNDIzOGJmIn0.RL7uXGjDkdRCMyc2ekvOVOuG2LeCIon2aeTrAZVdvdtI//vW23WaFkDPkf0eheJrS1bjmoA7X/IsS9fVFC3Z9Xb+pY0SMSoHqlCMMsfuSOQqqUzR5/Ec5u7eyVSGsjQUdcZRgLGRrffVy/z/f/sfO1uSRoCoVEBRlE4vG0awWhyPcGauIxqy/mZ2hJjmEOhT80CkRh1k4dz9pmwb4ZZqQGCLn7AHJZB1R3rSOJLoZAdreTOisI9qZRM5429GntkrI4JeEfmW7IFjWEGtH3P53SHbJJTs3cgFaSd0C3aG4Liqv1UlB/PEvb/TudkW/iseMyp/YCtYLeqwMQECQGNAiA==")
SSL_VERIFY = os.getenv("SSL_VERIFY", "false").lower() in ("1", "true", "yes")
LLM_MODEL = os.getenv("LLM_MODEL", "llama32-90b-instruct")
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "6000"))
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.0"))
LLM_TOP_P = float(os.getenv("LLM_TOP_P", "0.5"))
