class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz"),
        }
        result = []
        for d in digits:
            if not result:
                result = letters[d]
            else:
                res = []
                for comb in result:
                    for letter in letters[d]:
                        res.append(comb + letter)
                result = res

        return result