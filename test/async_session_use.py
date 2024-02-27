import asyncio


class SessionTransaction:
    def __init__(self):
        pass

    async def __aenter__(self):
        print("Entering transaction context")
        # This value will be used in the `as` clause of the `async with` statement
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Exiting transaction context")


class AsyncSession:
    def __init__(self):
        self._session = None
        self._transaction = None

    async def begin(self):
        self._transaction = SessionTransaction()
        return self._transaction

    async def __aenter__(self):
        print("Entering async context")

    async def __aexit__(self, exc_type, exc_value, traceback):
        print("Exiting async context")


async def get_session():
    session = AsyncSession()
    async with await session.begin():
        # 在这里进行操作，session 已经被创建和启动
        yield session

    print("session closed")

# 调用异步上下文管理器


async def run_example():
    async for session in get_session():
        print("Inside async context")

# 使用 asyncio.run() 运行新的异步函数
asyncio.run(run_example())
