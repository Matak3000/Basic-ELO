# Basic-ELO
Basic ELO-style ranking system based on a win/lose result between two parties.

Parties have a numberical score, which translates into a rank in 250-brackets (i.e. 0-249 = rank 0, 250-499 = rank 1, 500-749 = rank 2, etc)

A win result between parties of the same rank cause a 15-point change to both parties (winner gains 15 points, loser loses 15 points), for each rank difference, point changes are then altered by 2 points, with limits to prevent gaining or losing more than 25 points per interaction.

Examples:
(Winner) rank 1 vs rank 1 (Loser)
Gain 15 points : Lose 15 points

(Winner) rank 1 vs rank 2 (Loser)
Gain 17 points : Lose 17 points

(Winner) rank 2 vs rank 1 (Loser)
Gain 13 points : Lose 13 points

Clauses:
Overscore - when point changes >25, limits to 25
Underscore - when points changes <5, limits to 5
Negative cap - when losers points after changes <0, sets to 0
