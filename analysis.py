import mysql.connector
import pandas as pd


# ==========================================
# 1. CONNECT TO MYSQL
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="ipl_analysis"
)

print("Connected to MySQL successfully.")



# 2. HIGHEST WINS
# ==========================================

query_wins = """
SELECT
    winner AS team,
    COUNT(*) AS total_wins
FROM matches
WHERE winner <> 'No Result'
GROUP BY winner
ORDER BY total_wins DESC;
"""

wins = pd.read_sql(query_wins, connection)

print("\n========== TEAM WINS ==========")
print(wins)


# ==========================================
# 3. WINS BY SEASON
# ==========================================

query_season_wins = """
SELECT
    season,
    winner AS team,
    COUNT(*) AS total_wins
FROM matches
WHERE winner <> 'No Result'
GROUP BY season, winner
ORDER BY season, total_wins DESC;
"""

season_wins = pd.read_sql(query_season_wins, connection)

print("\n========== WINS BY SEASON ==========")
print(season_wins)


# ==========================================
# 4. AVERAGE RUNS PER MATCH
# ==========================================

query_average_runs = """
SELECT
    ROUND(AVG(total_runs), 2) AS average_runs_per_match
FROM (
    SELECT
        match_id,
        SUM(batsman_runs) AS total_runs
    FROM deliveries
    GROUP BY match_id
) AS match_runs;
"""

average_runs = pd.read_sql(query_average_runs, connection)

print("\n========== AVERAGE RUNS PER MATCH ==========")
print(average_runs)


# ==========================================
# 5. NO RESULT MATCHES
# ==========================================

query_no_result = """
SELECT
    match_id,
    season,
    team1,
    team2,
    venue,
    match_date
FROM matches
WHERE winner = 'No Result'
ORDER BY season;
"""

no_result = pd.read_sql(query_no_result, connection)

print("\n========== NO RESULT MATCHES ==========")
print(no_result)


# ==========================================
# 6. RUNS DISTRIBUTION
# ==========================================

query_runs_distribution = """
SELECT
    match_id,
    SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY match_id
ORDER BY total_runs;
"""

runs_distribution = pd.read_sql(
    query_runs_distribution,
    connection
)

print("\n========== RUNS DISTRIBUTION ==========")
print(runs_distribution)


# ==========================================
# 7. WICKETS PER MATCH
# ==========================================

query_wickets = """
SELECT
    match_id,
    SUM(is_wicket) AS total_wickets
FROM deliveries
GROUP BY match_id
ORDER BY total_wickets DESC;
"""

wickets = pd.read_sql(
    query_wickets,
    connection
)

print("\n========== WICKETS PER MATCH ==========")
print(wickets)


# ==========================================
# 8. HIGH-SCORING MATCHES
# ==========================================

query_high_scoring = """
SELECT
    m.match_id,
    m.season,
    m.team1,
    m.team2,
    m.venue,
    SUM(d.batsman_runs) AS total_runs
FROM matches m
JOIN deliveries d
    ON m.match_id = d.match_id
GROUP BY
    m.match_id,
    m.season,
    m.team1,
    m.team2,
    m.venue
ORDER BY total_runs DESC
LIMIT 10;
"""

high_scoring = pd.read_sql(
    query_high_scoring,
    connection
)

print("\n========== HIGH-SCORING MATCHES ==========")
print(high_scoring)


# ==========================================
# 9. CLOSE CONNECTION
# ==========================================

connection.close()

print("\nMySQL connection closed.")
print("SQL analytics completed successfully.")