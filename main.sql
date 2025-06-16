-- 1. Total stories count
SELECT COUNT(*) AS total_stories
FROM `bigquery-public-data.hacker_news.full`
WHERE type = 'story';

-- 2. Top 5 stories by score
SELECT title, score
FROM `bigquery-public-data.hacker_news.full`
WHERE type = 'story'
ORDER BY score DESC
LIMIT 5;

-- 3. Top 5 users by total score
SELECT by AS author, SUM(score) AS total_score
FROM `bigquery-public-data.hacker_news.full`
WHERE type = 'story'
GROUP BY author
ORDER BY total_score DESC
LIMIT 5;

-- 4. Average score per hour of day
SELECT
  EXTRACT(HOUR FROM timestamp) AS hour,
  ROUND(AVG(score), 2) AS avg_score,
  COUNT(*) AS cnt
FROM `bigquery-public-data.hacker_news.full`
WHERE type = 'story'
GROUP BY hour
ORDER BY avg_score DESC;

-- 5. Most-commented story each month
WITH ranked AS (
  SELECT
    title,
    EXTRACT(YEAR FROM timestamp) AS yr,
    EXTRACT(MONTH FROM timestamp) AS mth,
    descendants AS comments,
    ROW_NUMBER() OVER (
      PARTITION BY EXTRACT(YEAR FROM timestamp),
                   EXTRACT(MONTH FROM timestamp)
      ORDER BY descendants DESC
    ) AS rn
  FROM `bigquery-public-data.hacker_news.full`
  WHERE type = 'story'
)
SELECT yr, mth, title, comments
FROM ranked
WHERE rn = 1
ORDER BY yr, mth;
