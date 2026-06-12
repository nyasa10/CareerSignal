SELECT
    s.college_tier,
    ROUND(
        AVG(p.package_lpa),
        2
    ) AS avg_package
FROM students s
JOIN placements p
ON s.student_id = p.student_id
WHERE p.placed = 1
GROUP BY s.college_tier
ORDER BY s.college_tier;

SELECT
    internships,
    ROUND(
        AVG(package_lpa),
        2
    ) AS avg_package
FROM students s
JOIN placements p
ON s.student_id = p.student_id
WHERE p.placed = 1
GROUP BY internships
ORDER BY internships;

SELECT
    s.student_id,
    s.branch,
    p.package_lpa
FROM students s
JOIN placements p
ON s.student_id = p.student_id
WHERE p.placed = 1
ORDER BY p.package_lpa DESC
LIMIT 10;

SELECT
    CASE
        WHEN readiness_score < 40 THEN 'Low'
        WHEN readiness_score < 70 THEN 'Medium'
        ELSE 'High'
    END AS readiness_bucket,

    ROUND(
        AVG(package_lpa),
        2
    ) AS avg_package

FROM students s
JOIN placements p
ON s.student_id = p.student_id

WHERE p.placed = 1

GROUP BY readiness_bucket;

