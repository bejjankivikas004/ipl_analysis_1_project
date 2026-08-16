import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import sys


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


# ==========================================
# 2. GET CHART OPTION
# ==========================================

if len(sys.argv) < 2:
    print("\nPlease select a chart.")
    print("\nAvailable options:")
    print("1. wins")
    print("2. average")
    print("3. noresult")
    print("4. runs")
    print("5. wickets")
    print("6. highscore")
    
    connection.close()
    sys.exit()


chart = sys.argv[1].lower()


# ==========================================
# 3. TEAM WINS
# ==========================================

if chart == "wins":

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

    plt.figure(figsize=(10, 6))

    plt.bar(
        wins["team"],
        wins["total_wins"]
    )

    plt.title("IPL Teams - Total Wins")
    plt.xlabel("Team")
    plt.ylabel("Number of Wins")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("team_wins.png")

    plt.show()

    print("Team wins chart created.")


# ==========================================
# 4. AVERAGE RUNS PER MATCH
# ==========================================

elif chart == "average":

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

    average_runs = pd.read_sql(
        query_average_runs,
        connection
    )

    average_value = average_runs[
        "average_runs_per_match"
    ].iloc[0]

    plt.figure(figsize=(7, 5))

    plt.bar(
        ["Average Runs"],
        [average_value]
    )

    plt.title("Average Runs Per Match")
    plt.ylabel("Runs")

    plt.tight_layout()

    plt.savefig("average_runs.png")

    plt.show()

    print("Average runs chart created.")


# ==========================================
# 5. NO RESULT MATCHES
# ==========================================

elif chart == "noresult":

    query_no_result = """
    SELECT
        COUNT(*) AS no_result_matches
    FROM matches
    WHERE winner = 'No Result';
    """

    no_result = pd.read_sql(
        query_no_result,
        connection
    )

    no_result_value = no_result[
        "no_result_matches"
    ].iloc[0]

    total_matches = pd.read_sql(
        "SELECT COUNT(*) AS total_matches FROM matches",
        connection
    )

    total_match_value = total_matches[
        "total_matches"
    ].iloc[0]

    completed_matches = (
        total_match_value - no_result_value
    )

    plt.figure(figsize=(7, 5))

    plt.bar(
        ["Completed", "No Result"],
        [completed_matches, no_result_value]
    )

    plt.title("IPL Matches - Result Status")
    plt.ylabel("Number of Matches")

    plt.tight_layout()

    plt.savefig("no_result_matches.png")

    plt.show()

    print("No Result chart created.")


# ==========================================
# 6. RUNS DISTRIBUTION
# ==========================================

elif chart == "runs":

    query_runs_distribution = """
    SELECT
        match_id,
        SUM(batsman_runs) AS total_runs
    FROM deliveries
    GROUP BY match_id;
    """

    runs_distribution = pd.read_sql(
        query_runs_distribution,
        connection
    )

    plt.figure(figsize=(10, 6))

    plt.hist(
        runs_distribution["total_runs"],
        bins=15
    )

    plt.title("Distribution of Runs Per Match")
    plt.xlabel("Total Runs")
    plt.ylabel("Number of Matches")

    plt.tight_layout()

    plt.savefig("runs_distribution.png")

    plt.show()

    print("Runs distribution chart created.")


# ==========================================
# 7. WICKETS PER MATCH
# ==========================================

elif chart == "wickets":

    query_wickets = """
    SELECT
        match_id,
        SUM(is_wicket) AS total_wickets
    FROM deliveries
    GROUP BY match_id;
    """

    wickets = pd.read_sql(
        query_wickets,
        connection
    )

    plt.figure(figsize=(10, 6))

    plt.hist(
        wickets["total_wickets"],
        bins=15
    )

    plt.title("Distribution of Wickets Per Match")
    plt.xlabel("Total Wickets")
    plt.ylabel("Number of Matches")

    plt.tight_layout()

    plt.savefig("wickets_distribution.png")

    plt.show()

    print("Wickets distribution chart created.")


# ==========================================
# 8. HIGH-SCORING MATCHES
# ==========================================

elif chart == "highscore":

    query_high_scoring = """
    SELECT
        m.match_id,
        m.season,
        m.team1,
        m.team2,
        SUM(d.batsman_runs) AS total_runs
    FROM matches m
    JOIN deliveries d
        ON m.match_id = d.match_id
    GROUP BY
        m.match_id,
        m.season,
        m.team1,
        m.team2
    ORDER BY total_runs DESC
    LIMIT 10;
    """

    high_scoring = pd.read_sql(
        query_high_scoring,
        connection
    )

    high_scoring["match"] = (
        high_scoring["team1"]
        + " vs "
        + high_scoring["team2"]
    )

    plt.figure(figsize=(10, 7))

    plt.barh(
        high_scoring["match"],
        high_scoring["total_runs"]
    )

    plt.title("Top 10 High-Scoring IPL Matches")
    plt.xlabel("Total Runs")
    plt.ylabel("Match")

    plt.gca().invert_yaxis()

    plt.tight_layout()

    plt.savefig("high_scoring_matches.png")

    plt.show()

    print("High-scoring matches chart created.")


# ==========================================
# 9. INVALID OPTION
# ==========================================

else:

    print("\nInvalid chart option.")

    print("\nUse one of these:")
    print("wins")
    print("average")
    print("noresult")
    print("runs")
    print("wickets")
    print("highscore")


# ==========================================
# 10. CLOSE CONNECTION
# ==========================================

connection.close()

print("\nMySQL connection closed.")