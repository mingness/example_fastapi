import os

import uvicorn
from api import routes
from fastapi import FastAPI

app = FastAPI(
    title="Example Application",
    description="This application is a template.",
    version="0.1.0",
)

app.include_router(routes)


@app.get("/health", status_code=200)
async def get_health():
    return


LOGLEVEL = os.environ.get("LOGLEVEL", "info").lower()


if __name__ == "__main__":
    log_config = uvicorn.config.LOGGING_CONFIG
    uvicorn.run("main:app", log_config=log_config, log_level=LOGLEVEL, port=8080)
