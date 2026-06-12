SELECT
    ROUND(AVG(dsa_score),2) AS dsa,
    ROUND(AVG(sql_score),2) AS sql,
    ROUND(AVG(python_score),2) AS python,
    ROUND(AVG(communication_score),2) AS communication
FROM skills s
JOIN placements p
ON s.student_id = p.student_id
WHERE p.placed = 1;

SELECT
    ROUND(AVG(dsa_score),2) AS dsa,
    ROUND(AVG(sql_score),2) AS sql,
    ROUND(AVG(python_score),2) AS python,
    ROUND(AVG(communication_score),2) AS communication
FROM skills s
JOIN placements p
ON s.student_id = p.student_id
WHERE p.placed = 0;

SELECT
    ROUND(AVG(CASE WHEN p.placed=1 THEN dsa_score END),2) -
    ROUND(AVG(CASE WHEN p.placed=0 THEN dsa_score END),2)
    AS dsa_gap
FROM skills s
JOIN placements p
ON s.student_id = p.student_id;

SELECT
    CASE
        WHEN dsa_score <= 3 THEN 'Low'
        WHEN dsa_score <= 7 THEN 'Medium'
        ELSE 'High'
    END AS dsa_bucket,

    ROUND(
        100.0 * AVG(p.placed),
        2
    ) AS placement_rate

FROM skills s
JOIN placements p
ON s.student_id = p.student_id

GROUP BY dsa_bucket;

SELECT
    CASE
        WHEN communication_score <= 3 THEN 'Low'
        WHEN communication_score <= 7 THEN 'Medium'
        ELSE 'High'
    END AS communication_bucket,

    ROUND(
        100.0 * AVG(p.placed),
        2
    ) AS placement_rate

FROM skills s
JOIN placements p
ON s.student_id = p.student_id

GROUP BY communication_bucket;

