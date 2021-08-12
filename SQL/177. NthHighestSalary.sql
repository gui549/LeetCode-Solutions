SELECT S.salary 
FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) r
FROM employee) as S
WHERE S.r = N
GROUP BY 1