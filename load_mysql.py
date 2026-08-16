import pandas as pd
import mysql.connector


# ==========================================
# 1. READ CLEANED CSV FILES
# ==========================================

matches = pd.read_csv("matches_clean.csv")
deliveries = pd.read_csv("deliveries_clean.csv")
players = pd.read_csv("players_clean.csv")

print("Cleaned CSV files loaded successfully.")

print("Matches:", len(matches))
print("Deliveries:", len(deliveries))
print("Players:", len(players))


# ==========================================
# 2. CONNECT TO MYSQL
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="ipl_analysis"
)

cursor = connection.cursor()

print("Connected to MySQL successfully.")


# ==========================================
# 3. CLEAR OLD DATA
# ==========================================

cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

cursor.execute("DELETE FROM deliveries")
cursor.execute("DELETE FROM players")
cursor.execute("DELETE FROM matches")

cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

connection.commit()

print("Old data cleared successfully.")


# ==========================================
# 4. INSERT MATCHES
# ==========================================

matches_query = """
INSERT INTO matches
(match_id, season, team1, team2, venue, winner, match_date)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for _, row in matches.iterrows():

    cursor.execute(
        matches_query,
        (
            int(row["match_id"]),
            int(row["season"]),
            str(row["team1"]),
            str(row["team2"]),
            str(row["venue"]),
            str(row["winner"]),
            row["match_date"]
        )
    )

connection.commit()

print("Matches data inserted successfully.")


# ==========================================
# 5. INSERT DELIVERIES
# ==========================================

deliveries_query = """
INSERT INTO deliveries
(match_id, inning, over_no, ball,
 batsman_runs, bowler_runs, is_wicket)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for _, row in deliveries.iterrows():

    cursor.execute(
        deliveries_query,
        (
            int(row["match_id"]),
            int(row["inning"]),
            int(row["over"]),
            int(row["ball"]),
            int(row["batsman_runs"]),
            int(row["bowler_runs"]),
            int(row["is_wicket"])
        )
    )

connection.commit()

print("Deliveries data inserted successfully.")


# ==========================================
# 6. INSERT PLAYERS
# ==========================================

players_query = """
INSERT INTO players
(player_id, player_name, team, role)
VALUES (%s, %s, %s, %s)
"""

for _, row in players.iterrows():

    cursor.execute(
        players_query,
        (
            int(row["player_id"]),
            str(row["player_name"]),
            str(row["team"]),
            str(row["role"])
        )
    )

connection.commit()

print("Players data inserted successfully.")


# ==========================================
# 7. VERIFY DATA
# ==========================================

cursor.execute("SELECT COUNT(*) FROM matches")
match_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM deliveries")
delivery_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM players")
player_count = cursor.fetchone()[0]


print("\n========== MYSQL DATA VERIFICATION ==========")

print("Matches in MySQL:", match_count)
print("Deliveries in MySQL:", delivery_count)
print("Players in MySQL:", player_count)


# ==========================================
# 8. CLOSE CONNECTION
# ==========================================

cursor.close()
connection.close()

print("\nMySQL connection closed.")
print("Data loading completed successfully.")