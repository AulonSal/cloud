import uvicorn

import asyncio
from tortoise import run_async, Tortoise

from main import app

# Uvicorn does not expose a run_from_config to go along with uvicorn.config
CONFIG = dict(
        app='main:app',  # app must be passed using import string to enable reload or workers
        uds="{{ steward_socket_path }}",
        # workers=3, # Uvicorn does not suppont unix sockets with multiple workers + only 1 vCpu
        log_level='info',
    )

if __name__ == '__main__':
    uvicorn.run(**CONFIG)
    run_async(Tortoise.close_connections())

