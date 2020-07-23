Q1="""SELECT COUNT(1) FROM Movie WHERE year=1991 ;"""

Q2="""SELECT MIN(rank) FROM Movie ;"""

Q3="""SELECT MAX(rank) FROM Movie WHERE year=2000;"""

Q4="""SELECT AVG(rank) FROM Movie WHERE year=2000;"""

Q5="""SELECT year,COUNT(name) FROM Movie
    GROUP BY year
    ORDER BY year;
"""
Q6="""SELECT MIN(year),MAX(year) FROM Movie; """