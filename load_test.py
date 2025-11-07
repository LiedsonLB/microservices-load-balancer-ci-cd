import asyncio
import aiohttp
import time
import matplotlib.pyplot as plt
from collections import Counter

URL = "http://localhost:8080/api/agendamentos"  # Gateway endpoint
TOTAL_REQUESTS = 100000   # total de requisições
CONCURRENCY = 100      # número de requisições simultâneas

# armazenar qual instância respondeu
responses = []

async def fetch(session, url):
    async with session.get(url) as response:
        text = await response.text()
        responses.append(text.strip())
        return text

async def run_load_test():
    tasks = []
    connector = aiohttp.TCPConnector(limit_per_host=CONCURRENCY)
    async with aiohttp.ClientSession(connector=connector) as session:
        for _ in range(TOTAL_REQUESTS):
            task = asyncio.create_task(fetch(session, URL))
            tasks.append(task)
        await asyncio.gather(*tasks)

async def main():
    start = time.time()
    await run_load_test()
    end = time.time()

    print(f"\n✅ Teste finalizado em {end - start:.2f} segundos")
    print(f"Total de requisições: {TOTAL_REQUESTS}")
    print(f"Concorrência: {CONCURRENCY}")

    # contar quantas respostas vieram de cada instância
    counter = Counter(responses)
    print("\n📊 Distribuição das requisições:")
    for instance, count in counter.items():
        print(f"{instance}: {count}")

    # gráfico opcional
    plt.bar(counter.keys(), counter.values())
    plt.title("Distribuição de Requisições por Instância")
    plt.xlabel("Instância")
    plt.ylabel("Quantidade de Requisições")
    plt.show()

if __name__ == "__main__":
    asyncio.run(main())
