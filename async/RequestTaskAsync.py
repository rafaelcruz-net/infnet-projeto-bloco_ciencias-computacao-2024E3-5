import asyncio
import aiohttp


async def fetch_user_data(session, user_id):
    print(f"buscando dados do usuário {user_id}..")
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    async with session.get(url) as response:
        user_data = await response.json()
        print(f"Dados do usuário {user_id} recebidos")
        return user_data


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for user_id in range(1, 10):
            tasks.append(fetch_user_data(session, user_id))
        user_data = await asyncio.gather(*tasks)
        print('Todos os usuários foram processados')
        print(user_data)

asyncio.run(main())