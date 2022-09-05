#variables
WinnerScore = 0
WinnerRank = 0
NewWinnerRank = 0
LoserScore = 0
LoserRank = 0
NewLoserRank = 0
UpperBoundary = 249

#score inputs
WinnerScore = int(input("Winner score: "))
LoserScore = int(input("Loser score: "))

#calculating player's ranks
while WinnerScore > UpperBoundary:
    UpperBoundary += 250
    WinnerRank += 1
UpperBoundary = 249
while LoserScore > UpperBoundary:
    UpperBoundary += 250
    LoserRank += 1
UpperBoundary = 249

print(".........................................")

#calculating point changes based on rank difference - with limits for changes <5 or >25
print("Winner's rank is ", WinnerRank, ", and Loser's rank is ", LoserRank, ", therefore:")
x = LoserRank - WinnerRank
PointsGain = 15 + x * 2
if PointsGain > 25:
    PointsGain = 25
    print("Overscore Clause - points change capped at 25")
elif PointsGain < 5:
    PointsGain = 5
    print("Underscore clause - points change capped at 5")
    
#calculating point changes based on rank difference - with limits for changes <5 or >25
print("Winner's rank is ", WinnerRank, ", and Loser's rank is ", LoserRank, ", therefore:")
x = LoserRank - WinnerRank
PointsChange = 15 + x * 2
if PointsChange > 25:
    PointsChange = 25
    print("Overscore Clause - points change capped at 25")
elif PointsChange < 5:
    PointsChange = 5
    print("Underscore clause - points change capped at 5")
    
#applying changes
WinnerScore += PointsChange
print("Winner gains ", PointsChange, " points")
LoserScore -= PointsChange
print("Loser loses ", PointsChange, " points")

#clause to prevent negative points after applying changes
if LoserScore < 0:
    LoserScore = 0
    print(".........................................")
    print("Negative Cap Clause - Loser's points fell negative, score was set to 0.")

print(".........................................")

#calculating players ranks after changes
while WinnerScore > UpperBoundary:
    UpperBoundary += 250
    NewWinnerRank += 1
UpperBoundary = 249
while LoserScore > UpperBoundary:
    UpperBoundary += 250
    NewLoserRank += 1
UpperBoundary = 249

#stating rank changes
if NewWinnerRank > WinnerRank:
    print("Winner's rank has increased to ", NewWinnerRank)
    WinnerRank = NewWinnerRank
else:
    print("Winner's rank has not changed")
if NewLoserRank < LoserRank:
    print("Loser's rank has decreased to ", NewLoserRank)
    LoserRank = NewLoserRank
else:
    print("Loser's rank has not changed")
