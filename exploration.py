import pandas as pd

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")
players = pd.read_csv("players.csv")

print("\n========== MATCHES ==========")
print(matches.head())
print(matches.shape)
print(matches.columns)
print(matches.info())
print(matches.isnull().sum())

print("\n========== DELIVERIES ==========")
print(deliveries.head())
print(deliveries.shape)
print(deliveries.columns)
print(deliveries.info())
print(deliveries.isnull().sum())

print("\n========== PLAYERS ==========")
print(players.head())
print(players.shape)
print(players.columns)
print(players.info())
print(players.isnull().sum())