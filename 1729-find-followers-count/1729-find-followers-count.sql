# Write your MySQL query statement below
SELECT user_id, count(*) as followers_count
FROM Followers
GROUP BY user_id
order by user_id