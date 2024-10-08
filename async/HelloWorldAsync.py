import asyncio

async def say_hello():
    print("Olá")
    await asyncio.sleep(1)
    print("Olá de novo")


#Executa a tarefa de forma assincrona
asyncio.run(say_hello())