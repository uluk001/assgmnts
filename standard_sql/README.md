# SQL-задание на проектирование, вставку и чтение данных

## Цель

Создать простую реляционную структуру из трёх связанных таблиц, наполнить её тестовыми данными и выполнить серию SQL-запросов на выборку с использованием фильтрации, сортировки и группировки.

---

## Этап 1: Создание структуры базы данных

### Таблица `customers`
Хранит информацию о клиентах:
- `id` — первичный ключ, целое число, автоинкремент;
- `name` — имя клиента, строка;
- `email` — уникальный email, строка.

```sql
CREATE TABLE customers(
  id INT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(320) UNIQUE
);
```

### Таблица `orders`
Хранит информацию о заказах:
- `id` — первичный ключ, целое число, автоинкремент;
- `customer_id` — внешний ключ на `customers(id)`;
- `order_date` — дата заказа.

```sql
CREATE TABLE orders(
  id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

### Таблица `order_items`
Хранит информацию о товарах в заказах:
- `id` — первичный ключ, целое число, автоинкремент;
- `order_id` — внешний ключ на `orders(id)`;
- `product_name` — название товара, строка;
- `quantity` — количество, целое число;
- `price` — цена за единицу, число с плавающей точкой.

```sql
CREATE TABLE order_items(
  id SERIAL PRIMARY KEY,
  order_id INT,
  product_name VARCHAR(255),
  quantity INT,
  price FLOAT,
  FOREIGN KEY (order_id) REFERENCES orders(id)
);
```

---

## Этап 2: Наполнение тестовыми данными

Заполнение таблиц тестовыми данными для демонстрации работы запросов.

```sql
INSERT INTO customers (id, name, email) VALUES
(1, 'Иван Иванов', 'ivan.ivanov@example.com'),
(2, 'John Doe', 'john.doe@example.com'),
(3, 'Jane Smith', 'jane.smith@example.com');

INSERT INTO orders (id, customer_id, order_date) VALUES
(1, 1, '2025-06-20'),
(2, 1, '2025-06-25'),
(3, 2, '2025-06-24');

INSERT INTO order_items (id, order_id, product_name, quantity, price) VALUES
(1, 1, 'Gaming Laptop', 1, 15000.00),
(2, 1, 'Wireless Mouse', 2, 25.50),
(3, 2, 'Office Chair', 1, 220.00),
(4, 3, 'Smartphone', 1, 799.99),
(5, 3, 'USB-C Cable', 3, 9.99);
```

---

## Этап 3: Запросы на чтение

### Задание 1: Простая фильтрация
**Цель:** Вывести список заказов клиента с именем "Иван Иванов".

**Запрос:**
```sql
SELECT
  o.id,
  o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE c.name = 'Иван Иванов';
```

**Результат:**
```
+----+------------+
| id | order_date |
+----+------------+
|  1 | 2025-06-20 |
|  2 | 2025-06-25 |
+----+------------+
```

### Задание 2: Фильтрация + сортировка
**Цель:** Получить список всех товаров из заказа с `ID = 3`, отсортированный по цене по убыванию.

**Запрос:**
```sql
SELECT
  product_name,
  quantity,
  price
FROM order_items
WHERE order_id = 3
ORDER BY price DESC;
```

**Результат:**
```
+--------------+----------+--------+
| product_name | quantity | price  |
+--------------+----------+--------+
| Smartphone   |        1 | 799.99 |
| USB-C Cable  |        3 |   9.99 |
+--------------+----------+--------+
```

### Задание 3: Группировка + фильтрация
**Цель:** Вывести список клиентов и общую сумму, которую они потратили. Показать только тех, у кого сумма покупок больше 5000.

**Запрос:**
```sql
SELECT
  c.name,
  SUM(oi.price * oi.quantity) AS total_spent
FROM customers c
JOIN orders o ON o.customer_id = c.id
JOIN order_items oi ON oi.order_id = o.id
GROUP BY c.name
HAVING SUM(oi.price * oi.quantity) > 5000
ORDER BY total_spent DESC;
```

**Результат:**
```
+-------------+-------------+
| name        | total_spent |
+-------------+-------------+
| Иван Иванов |     15051.0 |
+-------------+-------------+
``` 