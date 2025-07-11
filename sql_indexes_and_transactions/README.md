# Техническое задание: Работа с индексами и транзакциями в SQL

---

## Этап 1: Массовое наполнение базы

**Цель:** Сымитировать работу интернет-магазина с большим количеством данных.

**Требование:**
- Заполнить таблицу `order_items` минимум 1 000 000 строк.
- Данные должны быть осмысленными (разные товары, случайные цены, количества, ссылки на реальные заказы).

**Реализация:**
Для наполнения базы данных использовался Python-скрипт.

- **Скрипт:** `populate_db.py`
- **Зависимости:** `requirements.txt`

Скрипт использует `asyncpg` для асинхронной работы с PostgreSQL и `Faker` для генерации случайных данных. Он наполняет таблицы `customers`, `orders` и `order_items`.

---

## Этап 2: Установка индексов

**Цель:** Ускорить выполнение часто используемых запросов.

**Требования и реализация:**
1.  **Индекс по `customer_id` в таблице `orders`:**
    ```sql
    CREATE INDEX "customers_customer_id_idx" ON orders(customer_id);
    ```

2.  **Композитный индекс по `(order_id, price)` в таблице `order_items`:**
    ```sql
    CREATE INDEX "order_items_order_id_and_price_id_idx" ON order_items(order_id, price);
    ```

3.  **Индекс для текстового поиска по `product_name` в `order_items`:**
    ```sql
    CREATE INDEX order_items_product_name_gin_idx ON order_items USING GIN (to_tsvector('english', product_name));
    ```

---

## Этап 3: Анализ использования индексов

**Цель:** Проверить, используется ли индекс при выполнении запроса.

**Запрос для анализа:**
Поиск всех товаров с `price < 5000` из заказа с `ID = 123`.

```sql
EXPLAIN ANALYZE SELECT * FROM order_items WHERE order_id=123 AND price < 5000;
```
*План выполнения должен показать использование композитного индекса по `(order_id, price)`.*
![unnamed (2)](https://github.com/user-attachments/assets/41eb4353-7657-423a-abca-b8ecef613aae)
![unnamed (3)](https://github.com/user-attachments/assets/0ff141e5-1eeb-481f-b580-847f83e87802)

---

## Этап 4: Удаление неэффективных индексов

**Цель:** Очищать ненужные или неиспользуемые ресурсы.

**Действие:**
Индекс `order_items_product_name_gin_idx` был удалён и заменён на стандартный B-Tree индекс, так как он показал лучшую производительность для конкретных запросов.

```sql
DROP INDEX "order_items_product_name_gin_idx";
```

**Обоснование:**
> Удален GIN индекс по product_name, ставил думая что лучше подойдет для текстового поиска. Потом создал обычный индекс туда же, и Execution Time 90.469 ms → 42.530 ms.
![unnamed (1)](https://github.com/user-attachments/assets/9dec551a-8446-45cb-be63-0aea17c41e0b)
> ![unnamed](https://github.com/user-attachments/assets/aa286473-2bcf-4b9d-893f-4c70d0880e57)


---

## Этап 5: Бизнес-логика с использованием транзакций

**Цель:** Обеспечить целостность данных при выполнении операций.

**Сценарий:**
Реализовать следующую логику в виде SQL-транзакции:
1.  Создание новой записи в таблице `orders` с текущей датой.
2.  Добавление 3–5 случайных товаров в таблицу `order_items` для созданного заказа.
3.  В случае любой ошибки (например, попытка вставить `NULL` в `product_name`), вся транзакция откатывается.

**Требования:**
- Использовать явное начало/конец транзакции (`BEGIN`, `COMMIT`, `ROLLBACK`).
- Обработать возможные ошибки.
- Продемонстрировать, что в случае сбоя никаких частичных данных не остаётся в базе.

![unnamed](https://github.com/user-attachments/assets/8f074969-fbc0-461a-b933-577a05cdfe12)
![unnamed (1)](https://github.com/user-attachments/assets/d856d082-5359-4361-a7d4-e56d452b681d)

