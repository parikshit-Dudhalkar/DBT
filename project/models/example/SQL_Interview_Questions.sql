-- Input
-- Date_time              Calls
-- 20-01-2022 12:05:01     100
-- 20-01-2022 12:10:02     121
-- 21-01-2022 09:22:11     311
-- 21-01-2022 09:22:12     21
-- 21-01-2022 09:22:13     45
-- 21-01-2022 09:22:14     67



select extract(day from date_time) , sum(calls) over(partition by extract(day from date_time) order by extract(day from date_time)

from table group by extract(day from date_time)


SELECT     EXTRACT(day FROM Date_time) AS day,    SUM(Calls) OVER (PARTITION BY EXTRACT(day FROM Date_time) ORDER BY Date_time) AS cumulative_calls
FROM    your_table_name GROUP BY     EXTRACT(day FROM Date_time), Date_time ORDER BY     day, Date_time;


 



-- ======================================/

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    manager_id INT,
    position VARCHAR(50)
);
 
INSERT INTO employees (employee_id, employee_name, manager_id, position) VALUES
(1, 'Alice', 2, 'Engineer'),
(2, 'Bob', 3, 'Manager'),
(3, 'Charlie', 4, 'Director'),
(4, 'David', 5, 'VP'),
(5, 'Eve', NULL, 'CEO');
 
 
 
 
 
 
 
 
 select * from employees;
 
-- manager find
   select e.employee_id, e.employee_name, ee.employee_name as manager, e.manager_id , e.position
   from employees e left  join employees ee
    on e.manager_id=ee.employee_id   
;    
    
    
    -- find the ceo
 select  employee_id, employee_name, manager_id, position from employees where manager_id is null ;
 
 
-- hierrarchy
 with cte as 
     (
    select  employee_id, employee_name, manager_id, position from employees where manager_id is null 
     union all 
    
    select e.employee_id, e.employee_name, e.manager_id , e.position from employees e join cte ee
    on e.manager_id=ee.employee_id
    )
select * from cte;


*********************************************************************************

Write a query to find the department with the highest average salary for 
employees who have been with the company for more than 2 years.
 
 
 with cte (
 select emp_id, department, datediff(joining_time,CURRENT_DATE) as timespent from employee e join department d 
 on e.empid=d.empid )
 ,
 cte2 as (
 
 
 select  emp,dept, avg(sal)    as high_sal from cte
 group by emp 
 
 where timespent > 2)
 
 select d.department from cte2 join department d on cte2.empid=d.empid  order by high_sal desc limit 1 