import numpy as np

TeamA=np.random.randint(0,11,10)
TeamB=np.random.randint(0,11,10)

print("Team A", TeamA)
print("Team B", TeamB)

print("Team A Wons", len(TeamA[TeamA>TeamB]))
print("Team B losses:",TeamB[TeamB<TeamA])
print("Maximum of Team A:",np.max(TeamA))
avg=np.mean(np.concatenate((TeamA,TeamB)))
print("Avg of all scores:",avg)
print("Point difference:",np.abs(TeamA-TeamB))