# Quick SQL

## Conditional Query

```
SELECT 

```


## Operation

### Numerical
```
SELECT min_salary, min_salary+100, min_salary-100, min_salary*0.1
FROM jobs;
```

### Ordering
```sql
SELECT department_id, location_id
FROM departments
ORDER BY column_a ASC;
```

ORDER BY: resource-consuming

### Logical Operators
```sql
SELECT * FROM employees
WHERE employee_id < 150 AND salary >= 10000;
```

```sql
SELECT * FROM employees
WHERE employee_id < 150 AND salary >= 10000 OR manager_id = 100;
```
numeric > and > or
```sql
SELECT * FROM table
WHERE locaiton_id <> 1700;

SELECT * FROM table
WHERE location_id != 1700;

SELECT * FROM table
WHERE manager_id IS NOT NULL;
```

### Set Operators

* UNION: 합집합 & 중복제거
* UNION ALL: 합집합 & 중복보존
* MINUS: 차집합
* INTERSECT: 교집합

```sql
SELECT employee_id, first_name, email, manager_id FROM employees
WHERE manager_id = 114
UNION
SELECT employee_id, first_name, email, manager_id FROM employees
WHERE manager_id = 120;
```

* columns & datatype should be matched

```sql

```

## Functions
* built-in functions
* user defined functions

DATA_TYPE
* MySQL https://dev.mysql.com/doc/refman/8.0/en/data-types.html
	* 
* Oracle https://docs.oracle.com/database/121/SQLRF/sql_elements001.htm
	* CHAR, VARCHAR2, NUMBER, DATE, ...

* UPPER, LOWER, INITCAP
	* INITCAP ~~ capitalize
* SUBSTR
* REPLACE
* LPAD, RPAD, LTRIM, RTRIM, TRIM
	* LTRIM, RTRIM will remove spaces with no settings
	* TRIM only remove spaces at front & rear
* LENGTH
* CONCAT

```sql
SELECT job_title, upper(job_title), lower(job_title), initcap(job_title)
FROM jobs;
```

```sql
SELECT phone, substr(phone, 1, 3) AS phone_front
FROM jobs;
```

```sql
SELECT job_id, replace(job_id, 'CLERK', 'CL')
FROM jobs;
```

```sql
SELECT email, lpad(email, 10, '@')
FROM jobs;

SELECT email, rpad(email, 10, '@')
FROM jobs;
```

```sql
SELECT concat(first_name, concat(',', last_name))
FROM jobs;
```


