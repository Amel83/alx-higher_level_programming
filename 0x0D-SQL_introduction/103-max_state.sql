-- displays the max temperature of each state
SELECT city, AVG(temp) as avg_temp
FROM Temperatures
WHERE MONTH BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
