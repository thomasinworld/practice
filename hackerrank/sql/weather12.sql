SELECT DISTINCT City FROM STATION WHERE NOT (City LIKE "A%" OR City LIKE "E%" OR City LIKE "I%" OR City LIKE "O%" OR City LIKE "U%") AND NOT (City LIKE "%A" OR City LIKE "%E" OR City LIKE "%I" OR City LIKE "%O" OR City LIKE "%U");