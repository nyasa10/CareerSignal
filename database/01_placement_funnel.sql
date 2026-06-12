SELECT
    ROUND(
        100.0 * SUM(placed) / COUNT(*),
        2
    ) AS placement_rate
FROM placements;

SELECT
    offers_received,
    COUNT(*) AS students
FROM applications
GROUP BY offers_received
ORDER BY offers_received;

SELECT
    ROUND(
        100.0 * SUM(oa_cleared) /
        NULLIF(SUM(oa_attempted),0),
        2
    ) AS oa_conversion_rate
FROM applications;

SELECT
    ROUND(
        100.0 * SUM(interviews_received) /
        NULLIF(SUM(oa_cleared),0),
        2
    ) AS interview_conversion_rate
FROM applications;

SELECT
    ROUND(
        100.0 * SUM(offers_received) /
        NULLIF(SUM(interviews_received),0),
        2
    ) AS offer_conversion_rate
FROM applications;

