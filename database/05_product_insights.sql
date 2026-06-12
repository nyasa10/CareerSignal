SELECT
    CASE
        WHEN readiness_score < 40 THEN 'Low'
        WHEN readiness_score < 70 THEN 'Medium'
        ELSE 'High'
    END AS readiness_bucket,

    ROUND(
        100.0 * AVG(p.placed),
        2
    ) AS placement_rate

FROM students s
JOIN placements p
ON s.student_id = p.student_id

GROUP BY readiness_bucket;

SELECT
    COUNT(*) FILTER (WHERE dsa_score < 5) AS weak_dsa,
    COUNT(*) FILTER (WHERE sql_score < 5) AS weak_sql,
    COUNT(*) FILTER (WHERE python_score < 5) AS weak_python,
    COUNT(*) FILTER (WHERE communication_score < 5) AS weak_communication
FROM skills;


SELECT
    COUNT(*)
FROM students
WHERE readiness_score < 50;

SELECT
    s.student_id,
    s.readiness_score,
    p.placed
FROM students s
JOIN placements p
ON s.student_id = p.student_id
WHERE
    readiness_score >= 70
    AND p.placed = 0
ORDER BY readiness_score DESC;



