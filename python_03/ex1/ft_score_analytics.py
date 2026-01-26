import sys

print("=== Player Score Analytics ===\n")
if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 "
          "ft_score_analytics.py <score1> <score2> ...")
else:
    scores = []
    for arg in sys.argv[1:]:
        try:
            arg = int(arg)
            scores.append(arg)
        except ValueError:
            print("That input isn’t numeric — try again with digits only.")
            sys.exit()
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(sys.argv) - 1}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / (len(sys.argv) - 1)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
