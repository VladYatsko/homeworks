def get_winners(results: list):
    maximal_result = 0
    winner_numbers = []
    for _ in range(3):
        for points in results:
            if points > maximal_result:
                maximal_result = points
        winner_numbers.append(results.index(maximal_result)+1)
        results[results.index(maximal_result)] = 0
        maximal_result = 0
    return winner_numbers


print(get_winners([100, 10, 20, 30, 40, 5, 80, 21]))
