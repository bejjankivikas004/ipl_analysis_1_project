import pandas as pd
import numpy as np
import os


# =========================
# EXTRACT
# =========================

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")
players = pd.read_csv("players.csv")


print("Original Data:")
print("Matches:", matches.shape)
print("Deliveries:", deliveries.shape)
print("Players:", players.shape)


# =========================
# TRANSFORM - MATCHES
# =========================

matches = matches.drop_duplicates(subset=["match_id"], keep="first")

matches["winner"] = matches["winner"].fillna("No Result")

matches["match_date"] = pd.to_datetime(matches["match_date"])

matches["team1"] = matches["team1"].str.strip().str.upper()
matches["team2"] = matches["team2"].str.strip().str.upper()
matches["winner"] = matches["winner"].str.strip()


# =========================
# TRANSFORM - DELIVERIES
# =========================

deliveries = deliveries.drop_duplicates()

deliveries["batsman_runs"] = deliveries["batsman_runs"].fillna(0)
deliveries["bowler_runs"] = deliveries["bowler_runs"].fillna(0)
deliveries["is_wicket"] = deliveries["is_wicket"].fillna(0)

deliveries["batsman_runs"] = deliveries["batsman_runs"].astype(int)
deliveries["bowler_runs"] = deliveries["bowler_runs"].astype(int)
deliveries["is_wicket"] = deliveries["is_wicket"].astype(int)


# =========================
# TRANSFORM - PLAYERS
# =========================

players = players.drop_duplicates()

players["player_name"] = players["player_name"].str.strip()
players["team"] = players["team"].str.strip().str.upper()

players["role"] = players["role"].fillna("Unknown")


# =========================
# LOAD
# =========================


matches.to_csv("matches_clean.csv", index=False)
deliveries.to_csv("deliveries_clean.csv", index=False)
players.to_csv("players_clean.csv", index=False)


print("\nETL Pipeline Completed Successfully!")

print("\nCleaned Data:")
print("Matches:", matches.shape)
print("Deliveries:", deliveries.shape)
print("Players:", players.shape)


print("\n========== NULL CHECK ==========")

print("Matches NULL values:")
print(matches.isnull().sum())

print("\nDeliveries NULL values:")
print(deliveries.isnull().sum())

print("\nPlayers NULL values:")
print(players.isnull().sum())