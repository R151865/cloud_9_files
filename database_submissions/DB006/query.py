Q1="""
    select avg(age) 
    from
    Player as player;
"""


Q2="""
select match_no,
        play_date
from 
    Match 
where audience>50000
order by match_no asc;
"""

Q3="""
select team.team_id,
        count(mtd.win_lose)
from  
Team as team
inner join MatchTeamDetails as mtd
    on team.team_id=mtd.team_id 
        AND mtd.win_lose= 'W'
group by team.team_id
order by count(mtd.win_lose) desc,
        team.team_id asc;
"""        

Q4="""
select match.match_no,
        match.play_date
from Match as match
where match.stop1_sec >(
        select avg(stop1_sec)
        from Match
                        )
order by match.match_no desc;
"""

Q5="""
select mcaptain.match_no,
        team.name,
        player.name
from 
(Team as team
    inner join  Player as player
        on team.team_id=player.team_id)
    inner join MatchCaptain as mcaptain
        on mcaptain.captain=player.player_id
order by mcaptain.match_no asc,team.name asc;
"""

Q6="""
select match.match_no,
        player.name,
        player.jersey_no
from
Match as match
    inner join Player as player
        on player.player_id=match.player_of_match
order by match.match_no asc;
"""


Q7="""
SELECT Team.name,
            (SELECT AVG(age)
            FROM Player
            WHERE Team.team_id=Player.team_id
            ) as average
FROM 
Team
WHERE average>26
ORDER BY Team.name ASC;
"""


Q8="""
SELECT player.name,
        player.jersey_no,
        player.age,
        (
        SELECT  COUNT(sq_gd.goal_id) as goals
        FROM
            GoalDetails as sq_gd
        WHERE sq_gd.player_id=player.player_id
        ) AS goal_count
FROM
Player as player
WHERE player.age<=27 AND goal_count>0
ORDER BY goal_count DESC,
        player.name ASC;
"""

Q9="""
select dg.team_id,
        count(dg.goal_id)*100.0/
        (select count(goal_id) from GoalDetails)
from 
GoalDetails as dg
group by dg.team_id;
"""


Q10="""
select avg(count)
from
(select COUNT(goal_id) as count,
        gd.team_id
from GoalDetails as gd
group by gd.team_id);
"""




Q11="""
select player_id,
        name,
        date_of_birth
from
Player 
where player_id not in(
                select gd.player_id 
                from GoalDetails as gd
                )

order by player_id asc ;
"""


Q12="""
select 
    team.name,
    match.match_no,
    match.audience,
    match.audience -(select
                        avg(match.audience)as average
                            from
                    (Team as team1
                            inner join MatchTeamDetails as mtd
                                on team1.team_id=mtd.team_id)
                            inner join Match as match
                                on  match.match_no=mtd.match_no
                    where team1.team_id=team.team_id
                    ) as average

    
from 
    ((Team as team
        inner join MatchTeamDetails as mtd
            on team.team_id=mtd.team_id)
        inner join Match as match
            on  match.match_no=mtd.match_no)
order by match.match_no asc;
"""