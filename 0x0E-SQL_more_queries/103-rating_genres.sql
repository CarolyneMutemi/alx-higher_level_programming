-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.

-- Listing...
SELECT tv_genres.name, SUM(SUM(tv_show_ratings.rate)) AS 'rating'
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings
ON tv_show_genres.show_id = tv_show_ratings.show_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_shows.title
GROUP BY tv_genres.name
ORDER BY rating DESC;
