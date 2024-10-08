import asyncio
import time

def funcao_bloqueante():
    print("Função bloqueante começou")
    time.sleep(2)
    print("função bloqueante terminou")

async def main():
    #Executa a função bloqueante em um executor separado para não bloquear a thread principal
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, funcao_bloqueante)

asyncio.run(main())
