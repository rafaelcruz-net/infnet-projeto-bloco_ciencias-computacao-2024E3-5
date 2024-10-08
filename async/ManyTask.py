import asyncio

async def tarefa(nome, delay):
    print(f"Tarefa {nome} começou")
    await asyncio.sleep(delay)
    print(f"Tarefa {nome} terminou")


# EXEMPLO PARA EXECUÇÃO DE TAREFAS SIMULTANEAS
# async def main():
#     tarefa1 = asyncio.create_task(tarefa('A', 2))
#     tarefa2 = asyncio.create_task(tarefa('B', 1))
#     tarefa3 = asyncio.create_task(tarefa('C', 3))

#     #Espera todas as tarefas terminaram
#     await tarefa1
#     await tarefa2
#     await tarefa3


async def main():
    #  EXECUTAR VARIAS TAREFAS EM PARALELO E ESPERAR TODAS TERMINAREM
    # O GATHER permite executar várias tarefas em paralelo e espera que todas sejam concluidas antes de continuar
    await asyncio.gather(
        tarefa('A', 2),
        tarefa('B', 1),
        tarefa('C', 3)
    )

asyncio.run(main())
    