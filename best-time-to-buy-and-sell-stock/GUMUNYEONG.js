/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    let max = 0;

    for (let i = 0; i <= prices.length; i++) {
        for (let j = i + 1; j <= prices.length; j++) {
            const profit = prices[j] - prices[i];
            max = profit > max ? profit : max;
        }
    }

    return max;
};

// TC : O(n^2);
// SC : O(1);
