-- Задание 1
--
-- Присоединяется
--
-- Используйте образец базы данных SQLite hr.db (ту же базу данных, которую вы использовали на предыдущем уроке для домашних заданий)
--
-- В качестве решения HW создайте файл с именем: task1.sql со всеми SQL-запросами:

-- написать запрос на SQL для отображения имени, фамилии, номера отдела и названия отдела для каждого сотрудника
SELECT employees.first_name,
       employees.last_name,
       employees.department_id,
       departments.depart_name
FROM employees
         LEFT JOIN departments ON employees.department_id == departments.department_id

-- написать запрос на SQL для отображения имени и фамилии, отдела, города и провинции штата для каждого сотрудника

SELECT employees.first_name,
       employees.last_name,
       departments.depart_name,
       locations.city
FROM employees
LEFT JOIN departments ON employees.department_id == departments.department_id
LEFT JOIN locations ON departments.location_id == locations.location_id


-- написать запрос на SQL для отображения имени, фамилии, номера отдела и названия отдела для всех сотрудников отделов 80 или 40

SELECT employees.first_name,
       employees.last_name,
       employees.department_id,
       departments.depart_name,
       locations.city
FROM employees
LEFT JOIN departments ON employees.department_id == departments.department_id
LEFT JOIN locations ON departments.location_id == locations.location_id

WHERE employees.department_id = 80 OR employees.department_id = 40

-- написать запрос на SQL для отображения всех отделов, включая те, где нет ни одного сотрудника

SELECT depart_name
FROM departments

-- написать запрос на SQL для отображения имен всех сотрудников, включая имена их менеджеров

SELECT e1.first_name AS employee, e2.first_name AS manager
FROM employees e1
INNER JOIN employees e2 ON e1.manager_id = e2.employee_id;

-- написать запрос на SQL для отображения должности, полного имени (имени и фамилии) сотрудника и разницы между максимальной зарплатой по должности и зарплатой сотрудника

SELECT jobs.job_title,
       employees.first_name,
       employees.last_name,
       employees.salary,
       (jobs.max_salary - employees.salary) AS Try
FROM employees

JOIN jobs ON employees.job_id = jobs.job_id

-- написать запрос на SQL для отображения должности и средней зарплаты сотрудников


SELECT jobs.job_title,
       ROUND(AVG(employees.salary), 2) AS average_salar
FROM employees
JOIN jobs ON employees.job_id = jobs.job_id
GROUP BY jobs.job_title;

-- написать запрос на SQL для отображения полного имени (имени и фамилии) и зарплаты тех сотрудников, которые работают в любом отделе, расположенном в Лондоне

SELECT CONCAT(e.first_name, ' ', e.last_name) AS full_name,
       e.salary,
       l.city
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE l.city = 'London';

-- написать запрос на SQL для отображения названия отдела и количества сотрудников в каждом отделе

SELECT d.depart_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.depart_name;