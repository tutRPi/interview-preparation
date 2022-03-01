class Solution:
    def invalidTransactions(self, transactions: list):
        invalids = []

        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            if int(amount) > 1000:
                invalids.append(transactions[i])
                continue

            for j in range(len(transactions)):
                if i == j:
                    continue
                name2, time2, amount2, city2 = transactions[j].split(",")

                if name == name2 and city != city2 and abs(int(time2) - int(time)) <= 60:
                    invalids.append(transactions[i])
                    break
        print(invalids)
        return invalids


if __name__ == "__main__":
    assert Solution().invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]) == ["alice,20,800,mtv","alice,50,100,beijing"]