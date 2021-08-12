SELECT D.name AS Department, E.name AS Employee, Salary
FROM Employee E INNER JOIN Department D on DepartmentId = D.Id
WHERE E.Salary = (SELECT max(Salary)
FROM Employee F
WHERE F.DepartmentId = E.DepartmentId);