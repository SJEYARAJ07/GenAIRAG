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
BGE_TOKEN = os.getenv("BGE_TOKEN","eyJraWQiOiJyc2FLZVVOSUUxIiwiYWxnIjoiUlM1MTIifQ.eyJzY3AiOlsiXC9nZW5haVwvZ29vZ2xlXC92MVwvbGF1bmNocGFkXC9tb2RlbHNcL2JnZS1sYXJnZS1lblwvZW1iZWRkaW5nc1wvKio6OnBvc3QiLCJcL2dlbmFpXC9nb29nbGVcL3YxXC9sYXVuY2hwYWRcL21vZGVsc1wvbGxhbWEzXC8qKjo6cG9zdCJdLCJzdWIiOiJhOTViZDgzYi1hOTk4LTM1Y2UtYjI4ZC02ZTdkMzUzMGViYzIiLCJ2ZXIiOiIxLjAiLCJpc3MiOiJBbWV4SURhYVNJRCIsInR5cCI6ImFwcCIsImV4cCI6MTc3ODI5OTk4OCwianRpIjoiZjRjNGE2YTItMmI2Ny00MzAwLWJiNDgtYjgxZjk3NTVhMTY4In0.SXWRWcx4rBSnKFrstw09L5TrSHBRuOmJHH+7Ei3qLB5DH/aaDcPVPXAoSn+LllbL/4Q7yfSSnu7jDFIGIigCposAAMcBmK9Vs3JRsEIggS/jlJbSq/o9XVmI0LN9UPTee1blMZtrwOjsGVus8/9Zyykh95oDWQeBG054DkZiTL0dGN7DnBu/akg0b4juTDVKYA2w2FHIObvZ9iwAB1GpLYWlyHfXPbDa5C0SRq4xoKWyiuJ3rdmE736gM0E6thZAGBLjTBao2kfniM0/KTvEiOFOUAmadDUUS12x7Tt0fy944irn2Df9KPNQHt8jbos5e5KnaOdwyZPbrTiTwXAnsA==")
LLM_URL = os.getenv("LLM_URL", "https://eag-dev.aexp.com/genai/google/v1/launchpad/models/llama3/llama3-90b/chat/completions")
LLM_TOKEN = os.getenv("LLM_TOKEN", "eyJraWQiOiJyc2FLZVVOSUUxIiwiYWxnIjoiUlM1MTIifQ.eyJzY3AiOlsiXC9nZW5haVwvZ29vZ2xlXC92MVwvbGF1bmNocGFkXC9tb2RlbHNcL2JnZS1sYXJnZS1lblwvZW1iZWRkaW5nc1wvKio6OnBvc3QiLCJcL2dlbmFpXC9nb29nbGVcL3YxXC9sYXVuY2hwYWRcL21vZGVsc1wvbGxhbWEzXC8qKjo6cG9zdCJdLCJzdWIiOiJhOTViZDgzYi1hOTk4LTM1Y2UtYjI4ZC02ZTdkMzUzMGViYzIiLCJ2ZXIiOiIxLjAiLCJpc3MiOiJBbWV4SURhYVNJRCIsInR5cCI6ImFwcCIsImV4cCI6MTc3ODI5OTk4OCwianRpIjoiZjRjNGE2YTItMmI2Ny00MzAwLWJiNDgtYjgxZjk3NTVhMTY4In0.SXWRWcx4rBSnKFrstw09L5TrSHBRuOmJHH+7Ei3qLB5DH/aaDcPVPXAoSn+LllbL/4Q7yfSSnu7jDFIGIigCposAAMcBmK9Vs3JRsEIggS/jlJbSq/o9XVmI0LN9UPTee1blMZtrwOjsGVus8/9Zyykh95oDWQeBG054DkZiTL0dGN7DnBu/akg0b4juTDVKYA2w2FHIObvZ9iwAB1GpLYWlyHfXPbDa5C0SRq4xoKWyiuJ3rdmE736gM0E6thZAGBLjTBao2kfniM0/KTvEiOFOUAmadDUUS12x7Tt0fy944irn2Df9KPNQHt8jbos5e5KnaOdwyZPbrTiTwXAnsA==")
SSL_VERIFY = os.getenv("SSL_VERIFY", "false").lower() in ("1", "true", "yes")
LLM_MODEL = os.getenv("LLM_MODEL", "llama32-90b-instruct")
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "6000"))
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.0"))
LLM_TOP_P = float(os.getenv("LLM_TOP_P", "0.5"))
