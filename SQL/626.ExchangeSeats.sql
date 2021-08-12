SELECT 
    CASE 
        WHEN (select count(*) FROM seat) % 2 = 1 and id = (select count(*) FROM seat) THEN id 
        WHEN id % 2 = 1 THEN id + 1 
        ELSE id - 1 
    END as id, 
    student
FROM seat
ORDER BY id;