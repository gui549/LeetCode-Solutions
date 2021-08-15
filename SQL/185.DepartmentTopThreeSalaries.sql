SELECT Department, Employee, Salary
FROM(
    SELECT D.name AS Department, E.name AS Employee, Salary, DENSE_RANK() OVER (PARTITION BY E.DepartmentId ORDER BY Salary DESC) d_rank
    FROM Employee E INNER JOIN Department D on E.DepartmentId = D.Id) AS tab
WHERE d_rank <= 3