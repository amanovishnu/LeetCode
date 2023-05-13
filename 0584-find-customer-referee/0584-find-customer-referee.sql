# Write your MySQL query statement below

# SELECT name
# FROM Customer
# WHERE referee_id IS NULL
# OR referee_id != 2
# ORDER BY name ASC;

SELECT name
FROM Customer
WHERE referee_id != 2
OR referee_id IS NULL
ORDER BY name ASC;

