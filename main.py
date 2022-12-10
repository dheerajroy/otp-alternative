from fastapi import FastAPI, Response, status
import hashlib
from database_manager import DatabaseManager

app = FastAPI()
database_manager = DatabaseManager()

@app.post('/hash', status_code=status.HTTP_201_CREATED)
async def gethash(data):
    """Returns hash (SHA256) of the given data"""
    return hashlib.sha256(str(data).encode('utf-8')).hexdigest()

@app.post('/register', status_code=status.HTTP_201_CREATED)
async def register(email, hashcode, response: Response):
    """Registers the hash on the database"""
    if not database_manager.set_user_hash(email, hashcode):
        response.status_code = status.HTTP_226_IM_USED

@app.post('/verify', status_code=status.HTTP_200_OK)
async def verify(email, hashcode):
    """Verifies if the hash is present in the database"""
    return database_manager.verify_user_hash(email, hashcode)
