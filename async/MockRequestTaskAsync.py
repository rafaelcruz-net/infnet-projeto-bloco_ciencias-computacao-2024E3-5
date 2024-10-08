import asyncio
import random

async def fetch_user_data(user_id):
    #Simula uma requisição com o tempo de resposta variavel
    delay = random.uniform(0.5, 2.0)
    print(f"buscando dados do usuário {user_id}.. tempo de espera {delay: 2f}s")
    await asyncio.sleep(delay) #Simula a latencia de um requisição
    user_data = {"id": user_id, "name": f"User {user_id}", "delay": delay}
    print(f"Dados do usuário {user_id} recebidos {user_data}")
    return user_data

async def main():
    tasks = []
    for user_id in range(1, 10):
        tasks.append(fetch_user_data(user_id))
    user_data = await asyncio.gather(*tasks)
    print('Todos os usuários foram processados')
    print(user_data)

asyncio.run(main())
