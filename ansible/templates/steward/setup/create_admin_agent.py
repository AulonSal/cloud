from steward_fastapi.core.authentication import create_new_active_agent
from steward_fastapi.utils import TortoiseContext
import asyncio


async def main():
    async with TortoiseContext():
        await create_new_active_agent(
            username="{{ steward_api_admin_agent }}",
            password="{{ steward_api_admin_password }}",
        )
        await create_new_active_agent(
            username="{{ steward_api_discord_test_agent }}",
            password="{{ steward_api_discord_test_password }}",
        )
        await create_new_active_agent(
            username="{{ steward_api_discord_agent }}",
            password="{{ steward_api_discord_password }}",
        )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

