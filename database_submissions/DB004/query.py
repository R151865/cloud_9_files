
Q1="""
        SELECT fname,lname FROM Actor WHERE id IN
        (SELECT pid FROM Cast 
        WHERE mid=1000);
 
 """
 
Q2="""
    SELECT COUNT(mid) FROM Cast WHERE pid IN 
    (SELECT id FROM Actor 
    WHERE fname='Harrison (I)' AND lname='Ford');
    
"""

Q3=""" 
    SELECT DISTINCT id FROM Actor WHERE id IN
    (SELECT  pid FROM Cast WHERE mid IN
    (SELECT id FROM Movie WHERE name='Harry Potter')
    );
"""


Q4=""" 
    SELECT DISTINCT * FROM Actor  WHERE id IN
    (SELECT pid  FROM Cast WHERE mid IN 
        (SELECT id  FROM Movie WHERE year>=1990 AND year<=2000)
    );
"""