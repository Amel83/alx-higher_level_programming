-- displays the top 3 of cities temperature during July and August
SELECT city, AVG(temp) as avg_temp
FROM temperatures
WHERE MONTH BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
