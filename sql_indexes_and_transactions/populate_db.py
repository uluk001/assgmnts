import asyncio
import datetime
import random

import asyncpg
import faker


async def main():
    fake = faker.Faker()

    async with asyncpg.create_pool(
        host="127.0.0.1",
        port=5432,
        user="postgres",
        password="postgres",
        database="test",
        min_size=6,
        max_size=6,
    ) as pool:
        print("Generating data...")
        users = [
            (i, fake.name(), f"user{i}@example.com")
            for i in range(1, 301)
        ]
        orders = [
            (
                i,
                random.randint(1, 300),
                fake.date_between_dates(
                    datetime.date(2010, 1, 1),
                    datetime.date(2025, 12, 31)
                )
            ) for i in range(1, 501)
        ]
        order_items = [
            (
                i,
                random.randint(1, 500),
                fake.bs(),
                random.randint(1, 4),
                random.randint(400, 50000)
            ) for i in range(1, 1000001)
        ]
        print("Data generated. Starting insertion...")

        async with pool.acquire() as connection:
            async with connection.transaction():
                await connection.executemany(
                    "INSERT INTO customers (id, name, email) "
                    "VALUES ($1, $2, $3) ON CONFLICT (id) DO NOTHING",
                    users
                )
                await connection.executemany(
                    "INSERT INTO orders (id, customer_id, order_date) "
                    "VALUES ($1, $2, $3) ON CONFLICT (id) DO NOTHING",
                    orders
                )
                await connection.executemany(
                    "INSERT INTO order_items "
                    "(id, order_id, product_name, quantity, price) "
                    "VALUES ($1, $2, $3, $4, $5) ON CONFLICT (id) DO NOTHING",
                    order_items
                )
        print("Insertion complete.")


if __name__ == "__main__":
    asyncio.run(main())
