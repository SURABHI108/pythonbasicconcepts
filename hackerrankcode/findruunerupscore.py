n = int(input().strip())
scores = list(map(int, input().strip().split()))

# Remove duplicates and sort in descending order
unique_scores = sorted(set(scores), reverse=True)

# The second element is the runner-up score
runner_up_score = unique_scores[1]

print(runner_up_score)