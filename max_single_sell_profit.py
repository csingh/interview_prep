def max_profit_n2(prices_array):
    # brute force solution
    print("Brute force O(N^2) solution:")
    print("prices_array:", prices_array)

    max_profit = 0
    buy_index = 0
    sell_index = 0

    for i,price1 in enumerate(prices_array):
        for j,price2 in enumerate(prices_array):
            profit = price2 - price1
            if profit > max_profit:
                max_profit = profit
                buy_index = i
                sell_index = j

    print("max_profit:", max_profit)
    print("buy_index:", buy_index)
    print("sell_index:", sell_index)

def max_profit_n(prices_array):
    # dynamic programming (?) solution
    if len(prices_array) < 2:
        return None

    print("DP O(N) solution:")
    print("prices_array:", prices_array)

    min_price = prices_array[0]
    min_price_index = 0

    max_price = prices_array[0]
    max_price_index = 0
    
    max_profit = 0
    buy_index = 0
    sell_index = 0

    for i,price in enumerate(prices_array[1:]):
        index = i + 1

        # if price is less than min_price, update min
        if price < min_price:
            min_price = price
            min_price_index = index

        # if price is more than max_price, update max and compare with max_profit
        if price > max_price:
            max_price = price
            max_price_index = index
            max_profit = max_price - min_price
            buy_index = min_price_index
            sell_index = max_price_index

    # print("min_price:", min_price)
    # print("min_price_index:", min_price_index)
    # print("max_price:", max_price)
    # print("max_price_index:", max_price_index)
    print("max_profit:", max_profit)
    print("buy_index:", buy_index)
    print("sell_index:", sell_index)

if __name__ == '__main__':
    stocks = [5, 2, 10, 3, 10, 5, 5, 1, 17, 4, 100]
    max_profit_n2(stocks)
    max_profit_n(stocks)
