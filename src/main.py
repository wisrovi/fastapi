from operator import imod


import uvicorn
from config import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)