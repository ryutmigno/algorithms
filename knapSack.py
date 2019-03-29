def knapSack(num_of_items, max_weight, max_fragile, values, weights, fragile):
        knapsack = np.zeros((num_of_items + 1, max_weight + 1, max_fragile + 1))
        items = []

        for i in range(1, num_of_items + 1):
                for j in range(1, max_weight + 1):
                        for k in range(max_fragile + 1):
                                if weights[i-1] > j:
                                        knapsack[i][j][k] = knapsack[i-1][j][k]
                                else:
                                        if fragile[i-1] > k:
                                                knapsack[i][j][k] = knapsack[i - 1][j][k]
                                        else:
                                                if knapsack[i - 1][j][k] > knapsack[i - 1][j - weights[i - 1]][k - fragile[i - 1]] + values[i - 1]:
                                                        knapsack[i][j][k] = knapsack[i - 1][j][k]
                                                else:
                                                        knapsack[i][j][k] = knapsack[i - 1][j - weights[i - 1]][k - fragile[i - 1]] + values[i - 1]

        final_weight = 0
        final_value = 0
        final_fragile = 0

        j = max_weight
        k = max_fragile

        for i in range(num_of_items, 0, -1):
                if knapsack[i][j][k] != knapsack[i-1][j][k]:
                        items.append(i)
                        final_weight += weights[i - 1];
                        final_value += values[i - 1];
                        final_fragile += fragile[i - 1];
                        j -= weights[i - 1];
                        k -= fragile[i - 1];

        items = list(dict.fromkeys(items))
        
        print('total weight: {}\ntotal value: {}\nnumber of fragile items: {}'.format(final_weight, final_value, final_fragile))
        print('items: {}\nnumber of items: {}'.format(items, len(items)))

        return final_value, items
