CREATE TABLE test_region
(
    region_id   INT PRIMARY KEY NOT NULL,
    region_name VARCHAR(25)     NOT NULL
);

CREATE TABLE test_countries
(
    country_id   VARCHAR(2) PRIMARY KEY NOT NULL,
    country_name VARCHAR(40)            NOT NULL,
    region_id    INT,

    FOREIGN KEY (region_id) REFERENCES test_region (region_id) ON DELETE CASCADE
);

CREATE TABLE test_location
(
    location_id    INT PRIMARY KEY NOT NULL,
    stree_address  VARCHAR(25)     NOT NULL,
    postal_code    VARCHAR(25)     NOT NULL,
    city           VARCHAR(25)     NOT NULL,
    state_province VARCHAR(25)     NOT NULL,
    country_id     VARCHAR(2),

    FOREIGN KEY (country_id) REFERENCES test_countries (country_id) ON DELETE CASCADE
);

CREATE TABLE test_department
(
    department_id INT PRIMARY KEY NOT NULL,
    depart_name   VARCHAR(30)     NOT NULL,
    manager_id    INT             NOT NULL,
    location_id   INT             NOT NULL,

    FOREIGN KEY (location_id) REFERENCES test_location (location_id) ON DELETE CASCADE
);

CREATE TABLE test_jobs
(
    job_id     VARCHAR(10) PRIMARY KEY NOT NULL,
    job_title  VARCHAR(35)             NOT NULL,
    min_salary INT                     NOT NULL,
    max_salary INT                     NOT NULL
);

CREATE TABLE test_employees
(
    employee_id    INT PRIMARY KEY NOT NULL,
    first_name     VARCHAR(20)     NOT NULL,
    last_name      VARCHAR(20)     NOT NULL,
    email          VARCHAR(20)     NOT NULL,
    phone_number   VARCHAR(20)     NOT NULL,
    hire_date      DATE            NOT NULL,
    job_id         VARCHAR(20)     NOT NULL,
    salary         INT             NOT NULL,
    commission_pct INT             NOT NULL,
    manager_id     INT             NOT NULL,
    department_id  INT             NOT NULL,

    FOREIGN KEY (employee_id) REFERENCES test_job_history (employee_id) ON DELETE CASCADE,
    FOREIGN KEY (department_id) REFERENCES test_department (depart_name) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES test_jobs (job_id) ON DELETE CASCADE

);

CREATE TABLE test_job_history
(
    employee_id   INT PRIMARY KEY NOT NULL,
    start_date    DATE            NOT NULL,
    end_date      DATE            NOT NULL,
    job_id        VARCHAR(10),
    department_id INT             NOT NULL,

    FOREIGN KEY (department_id) REFERENCES test_department (department_id) ON DELETE CASCADE,
    FOREIGN KEY (job_id) REFERENCES test_jobs (job_id)
)

-- INSERT


-- Заполнение таблицы test_region
INSERT INTO test_region (region_id, region_name) VALUES
    (1, 'Europe'),
    (2, 'Asia'),
    (3, 'North America');

-- Заполнение таблицы test_countries
INSERT INTO test_countries (country_id, country_name, region_id) VALUES
    ('FR', 'France', 1),
    ('JP', 'Japan', 2),
    ('US', 'United States', 3);

-- Заполнение таблицы test_location
INSERT INTO test_location (location_id, stree_address, postal_code, city, state_province, country_id) VALUES
    (1, '10 Rue de Paris', '75001', 'Paris', 'Ile-de-France', 'FR'),
    (2, '1-1 Chiyoda', '100-0001', 'Tokyo', 'Tokyo', 'JP'),
    (3, '1600 Amphitheatre Pkwy', '94043', 'Mountain View', 'California', 'US');

-- Заполнение таблицы test_department
INSERT INTO test_department (department_id, depart_name, manager_id, location_id) VALUES
    (10, 'HR', 101, 1),
    (20, 'IT', 102, 2),
    (30, 'Finance', 103, 3);

-- Заполнение таблицы test_jobs
INSERT INTO test_jobs (job_id, job_title, min_salary, max_salary) VALUES
    ('DEV', 'Developer', 4000, 9000),
    ('MGR', 'Manager', 6000, 12000),
    ('ACC', 'Accountant', 3500, 8000);

-- Заполнение таблицы test_employees
INSERT INTO test_employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id) VALUES
    (101, 'Alice', 'Brown', 'alice@example.com', '1234567890', '2020-06-15', 'MGR', 8000, 10, 0, 10),
    (102, 'Bob', 'Smith', 'bob@example.com', '0987654321', '2019-04-20', 'DEV', 7000, 5, 101, 20),
    (103, 'Charlie', 'Johnson', 'charlie@example.com', '1122334455', '2018-08-30', 'ACC', 5000, 8, 101, 30);

-- Заполнение таблицы test_job_history
INSERT INTO test_job_history (employee_id, start_date, end_date, job_id, department_id) VALUES
    (101, '2018-01-01', '2020-06-14', 'DEV', 20),
    (102, '2017-05-10', '2019-04-19', 'ACC', 30),
    (103, '2016-07-01', '2018-08-29', 'DEV', 20);


-- Вывод
SELECT test_job_history.employee_id,
       test_employees.first_name,
       test_employees.last_name,
       test_employees.email,
       test_employees.phone_number,
       test_employees.hire_date,
       test_jobs.job_id,
       test_employees.salary,
       test_employees.commission_pct,
       test_employees.manager_id,
       test_employees.department_id
FROM test_employees
JOIN test_job_history ON test_employees.employee_id = test_job_history.employee_id
JOIN test_jobs ON test_employees.job_id = test_jobs.job_id


-- Connection

SELECT
    test_employees.employee_id,
    test_employees.first_name,
    test_employees.last_name,
    test_location.city
FROM test_employees
JOIN test_department ON test_employees.department_id = test_department.department_id
JOIN test_location ON test_department.location_id = test_location.location_id;















