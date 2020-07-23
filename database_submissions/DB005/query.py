Q1="""SELECT COUNT(*) FROM Movie WHERE year<1980;"""

Q2="""SELECT AVG(rank) FROM Movie WHERE year=1991; """

Q3="""SELECT MIN(rank) FROM Movie WHERE year=1991; """


Q4="""SELECT fname,lname FROM Actor WHERE id IN 
        (SELECT pid FROM Cast WHERE mid=1002);
        """
        
Q5="""SELECT COUNT(*) FROM Movie WHERE id IN 
(SELECT mid FROM Cast WHERE pid IN
(SELECT id FROM Actor WHERE fname= 'Orlando'  AND lname ='Galindo' ) ) ;"""        
        
Q6="""SELECT name FROM Movie WHERE  name LIKE 'Harry Potter%' AND year BETWEEN 2006 AND 2008;  """

Q7="""SELECT DISTINCT fname,lname FROM Director WHERE id IN
    (SELECT did FROM MovieDirector WHERE mid IN
    (SELECT id FROM Movie WHERE name LIKE 'Harry Potter%')
    );
    """


# need modification
Q8="""
    
SELECT name FROM Movie WHERE id IN(
SELECT  a.mid FROM

(SELECT mid FROM Cast  WHERE pid IN
(SELECT id FROM Actor WHERE fname='Jackie (I)' AND lname='Chan' )) AS a
INNER JOIN 

(SELECT mid FROM MovieDirector WHERE did IN
(SELECT id FROM Director WHERE fname='Jackie (I)' AND lname='Chan' )) AS b

ON a.mid=b.mid ) ORDER BY name ASC ;
"""

#MODIFICATION NEEDED
Q9="""
    
SELECT d.fname,d.lname FROM 

((SELECT did FROM MovieDirector WHERE mid IN
(SELECT id FROM Movie WHERE year=2001)
GROUP BY did 
HAVING COUNT(*)>=4) AS md
INNER JOIN
Director AS d ON md.did =d.id)

ORDER BY d.fname ASC,d.lname DESC
;

"""


#doubts
Q10="""       
        SELECT  * FROM Actor WHERE id IN
        (SELECT  pid FROM Cast WHERE mid IN
            (SELECT id FROM Movie WHERE year NOT BETWEEN 1990 AND 2000)
         )
        ORDER BY id ASC
        LIMIT 100;

"""

Q11="""
    SELECT gender,100.0*COUNT(gender)/ (SELECT COUNT(*) FROM Actor) FROM Actor
    GROUP BY gender;

"""

Q12="""
SELECT a.name,b.name,a.rank,a.year
FROM Movie a
INNER JOIN Movie b 
ON a.year=b.year AND a.rank=b.rank AND a.name!=b.name AND a.id<b.id
ORDER BY a.name ASC
LIMIT 100;
"""



Q13="""
select fname,year,avg(rank)
from 
(Movie inner join Cast on mid=Movie.id )
inner join Actor  on Actor.id=pid
group by pid,year 
order by fname asc,year desc
limit 100;
"""






Q15="""
select director.id,director.fname
from
    (Movie as movie
    inner join MovieDirector as md
        on md.mid=movie.id)
    inner join Director as director
        on director.id=md.did
    group by director.id
    having min(movie.year)>2005

order by director.id asc ;
"""


Q16="""
SELECT actor.fname,
    director.fname,
    AVG(movie.rank) AS score
FROM
    Director AS director
    INNER JOIN MovieDirector AS md
    INNER JOIN Cast AS sq_cast
    INNER JOIN Actor AS actor
    INNER JOIN Movie AS movie
        ON movie.id=md.mid and
        movie.id=sq_cast.mid and
        director.id=md.did and 
        sq_cast.mid=md.mid and
        actor.id=sq_cast.pid
        
    GROUP BY director.id,actor.id
    HAVING COUNT(*)>=5
ORDER BY score DESC,
    director.fname ASC,
    actor.fname DESC
LIMIT 100;
"""








"""
i need clarification from vedvidh annaiah

doubts
SELECT 
Director.fname,Director.fname, Movie.name, Movie.rank,

Movie.rank-(SELECT AVG(a.rank) FROM a WHERE a.did=Director.id )

FROM  (( Movie INNER JOIN MovieDirector ON Movie.id=mid) AS a

INNER JOIN Director ON Director.id=did ) AS b
LIMIT 10;
"""