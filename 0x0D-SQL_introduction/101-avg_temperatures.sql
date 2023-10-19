-- Do displays average temperature in (Fahrenheit) by city ordered by temperature (descending).
SELECT city,AVG(value) AS avg_temp
FROM temperatures
GROUP by CITY
ORDER BY avg_temp DESC;
-- @yego redo
