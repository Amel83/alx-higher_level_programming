-- get not null name from the tabek.
SELECT `score`, `name`
FROM `second_table` WHERE `name` != ""
ORDER BY `score` DESC
