-- Задача 1.
-- створити таблицю для працівників, з стовбцями: id, first_name, last_name, department, salary
--
-- змінити таблицю, додавши ще один стовпець - date
-- перейменувати даний стовпець на hire_date
-- перейменувати таблицю на new_employee
-- додати в таблицю запис про працівника
-- очистити таблицю
-- видалити таблицю

-- CREATE TABLE WORKERS
-- (
--     ID         INTEGER PRIMARY KEY,
--     first_name VARCHAR(20) NOT NULL,
--     last_name  VARCHAR(20) NOT NULL,
--     department TEXT        NOT NULL,
--     salary     INTEGER     NOT NULL
-- );

-- ALTER TABLE WORKERS
--     ADD COLUMN date DATE;

-- ALTER TABLE WORKERS
--     RENAME COLUMN date to hire_date;

-- ALTER TABLE WORKERS
--     RENAME TO new_employee;

-- INSERT INTO new_employee
-- VALUES (1, 'Andrii', 'Zadorozhnii', 'IT', '99999999', '2025-02-17');

-- DELETE FROM new_employee WHERE 1 = 1;

-- DROP TABLE new_employee

-- Задача 2.
-- створити таблицю, згідно пункту 1.1
-- додати кілька працівників
-- додати кілька працівників, що працюють в одному департаменті (ІТ)
-- підняти зарплату ІТ-шникам на 20% (update)
-- звільнити всіх, крім ІТ-шників (DELETE)
-- звільнити всіх (TRUNCATE)
-- стартап закрито (видалити таблицю) - обережно з стартапами, тримайтесь подалі від них, 97 з 100 закриваються )

-- CREATE TABLE workers
-- (
--     ID         INTEGER PRIMARY KEY,
--     first_name VARCHAR(20) NOT NULL,
--     last_name  VARCHAR(20) NOT NULL,
--     department TEXT        NOT NULL,
--     salary     INTEGER     NOT NULL
-- );

-- INSERT INTO workers
-- VALUES (1, 'Ivan', 'Ivanov', 'IT', 120000),
--        (2, 'Maria', 'Petrova', 'SECURITY', 50000),
--        (3, 'Oleg', 'Sidorov', 'COUNTER', 35000),
--        (4, 'Dmytro', 'Tkachenko', 'IT', 100000),
--        (5, 'Yulia', 'Kovalenko', 'SERVICE', 30000),
--        (6, 'Roman', 'Marchenko', 'IT', 150000),
--        (7, 'Viktor', 'Bondarenko', 'SECURITY', 70000),
--        (8, 'Tetyana', 'Melnyk', 'COUNTER', 45000),
--        (9, 'Anastasia', 'Andrieieva', 'IT', 130000),
--        (10, 'Vitalii', 'Zakharchenko', 'SERVICE', 25000),
--        (11, 'Petr', 'Shulha', 'SECURITY', 60000),
--        (12, 'Yevhen', 'Kovalenko', 'COUNTER', 42000),
--        (13, 'Oksana', 'Chornyi', 'SERVICE', 27000),
--        (14, 'Serhiy', 'Morozov', 'IT', 220000),
--        (15, 'Tetiana', 'Khomenko', 'SECURITY', 80000),
--        (16, 'Vadym', 'Pavlenko', 'COUNTER', 50000),
--        (17, 'Kateryna', 'Danylenko', 'SERVICE', 22000),
--        (18, 'Iryna', 'Klimenko', 'IT', 110000),
--        (19, 'Mykola', 'Lytvyn', 'SECURITY', 65000),
--        (20, 'Sergiy', 'Bodnar', 'COUNTER', 40000),
--        (21, 'Alina', 'Vasylenko', 'IT', 125000),
--        (22, 'Artem', 'Chumak', 'SERVICE', 30000),
--        (23, 'Olha', 'Khmelyna', 'SECURITY', 70000),
--        (24, 'Yurii', 'Kucherenko', 'COUNTER', 55000),
--        (25, 'Valentyn', 'Dubovik', 'IT', 180000);

-- UPDATE workers
-- SET salary = salary * 1.2
-- WHERE department == 'IT'

-- DELETE
-- FROM workers
-- WHERE department != 'IT';

-- DELETE
-- FROM workers
-- WHERE 1 = 1;

-- DROP TABLE workers;

-- Задача 3.
-- Створити повну копію таблиці employee, використовуючи SELECT
-- зробіть вибірку з таблиці employee з допомогою SELECT використовуючи LIKE, EXISTS, BETWEEN оператори (не одночасно)
-- зробіть вибірку з employee first_name, last_name, department, salary , сортування по department ASC, по salary - DESC

-- CREATE TABLE employees_copy AS
-- SELECT *
-- FROM employees

-- SELECT *
-- FROM employees
-- WHERE first_name LIKE 'S%';

-- SELECT first_name, last_name
-- FROM employees
-- WHERE EXISTS(SELECT first_name, last_name
--              FROM employees
--              WHERE first_name = 'Steven');

-- SELECT *
-- FROM employees
-- WHERE salary BETWEEN 1 AND 10000;

-- SELECT first_name, last_name, department_id, salary
-- FROM employees
-- ORDER BY department_id ASC, salary DESC;




