SELECT
    s.branch,
    ROUND(
        100.0 * AVG(p.placed),
        2
    ) AS placement_rate
FROM students s
JOIN placements p
ON s.student_id = p.student_id
GROUP BY s.branch
ORDER BY placement_rate DESC;

SELECT
    s.branch,
    ROUND(
        AVG(p.package_lpa),
        2
    ) AS avg_package
FROM students s
JOIN placements p
ON s.student_id = p.student_id
WHERE p.placed = 1
GROUP BY s.branch
ORDER BY avg_package DESC;

SELECT
    branch,
    COUNT(*) AS students
FROM students
GROUP BY branch
ORDER BY students DESC;

SELECT
    s.branch,
    SUM(a.applications_sent) AS applications,
    SUM(a.oa_cleared) AS oa_cleared,
    SUM(a.interviews_received) AS interviews,
    SUM(a.offers_received) AS offers
FROM students s
JOIN applications a
ON s.student_id = a.student_id
GROUP BY s.branch;

