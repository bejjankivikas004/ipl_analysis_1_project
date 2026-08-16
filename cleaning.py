import pandas as pd
import numpy as np
import os

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")
players = pd.read_csv("players.csv")



# =========================
# MATCHES CLEANING
# =========================

matches = matches.drop_duplicates(subset=["match_id"], keep="first")

matches["winner"] = matches["winner"].fillna("No Result")

matches["match_date"] = pd.to_datetime(matches["match_date"])

matches["season"] = matches["season"].astype(int)

matches["team1"] = matches["team1"].str.strip().str.upper()
matches["team2"] = matches["team2"].str.strip().str.upper()
matches["winner"] = matches["winner"].str.strip()

matches.to_csv("matches_clean.csv", index=False)


# =========================
# DELIVERIES CLEANING
# =========================

deliveries = deliveries.drop_duplicates()

deliveries["batsman_runs"] = deliveries["batsman_runs"].fillna(0)
deliveries["bowler_runs"] = deliveries["bowler_runs"].fillna(0)
deliveries["is_wicket"] = deliveries["is_wicket"].fillna(0)

deliveries["batsman_runs"] = deliveries["batsman_runs"].astype(int)
deliveries["bowler_runs"] = deliveries["bowler_runs"].astype(int)
deliveries["is_wicket"] = deliveries["is_wicket"].astype(int)

deliveries.to_csv("deliveries_clean.csv", index=False)


# =========================
# PLAYERS CLEANING
# =========================

players = players.drop_duplicates()

players["player_name"] = players["player_name"].str.strip()
players["team"] = players["team"].str.strip().str.upper()

players["role"] = players["role"].fillna("Unknown")

players.to_csv("players_clean.csv", index=False)


print("Data cleaning completed successfully.")