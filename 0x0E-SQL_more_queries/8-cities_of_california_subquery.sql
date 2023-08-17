-- All cities of California using a subquery
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id ASC;
