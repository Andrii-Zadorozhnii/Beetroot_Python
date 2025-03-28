-- Задание 1


-- Создайте таблицу по вашему выбору внутри образца базы данных SQLite, переименуйте ее и добавьте новый столбец.
-- Вставьте пару строк в вашу таблицу.
-- Также выполните операторы UPDATE и DELETE для вставленных строк.
-- Для решения этой задачи создайте файл с именем: task1.sql, содержащий все операторы SQL, которые вы использовали для выполнения этой задачи.


-- CREATE TABLE students (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL,
--     course TEXT NOT NULL
-- );

-- ALTER TABLE students RENAME TO learners;

-- ALTER TABLE learners ADD COLUMN age INTEGER;
-- SELECT * FROM learners;


-- INSERT INTO learners (name, course, age) VALUES
-- ('Андрей', 'Python', 30),
-- ('Екатерина', 'Data Science', 25);
-- SELECT * FROM learners;

-- UPDATE learners
-- SET course = 'Advanced Python'
-- WHERE name = 'Андрей';
-- SELECT * FROM learners;

-- DELETE FROM learners WHERE name = 'Екатерина';
-- SELECT * FROM learners;

-- SELECT * FROM learners;
