class Solution:
    def findAllRecipes(self, recipes: list, ingredients: list, supplies: list) -> list:
        producible_recipes = []
        producible = set(supplies)
        for recipe in recipes:
            is_producible = self.can_produce(recipe, recipes, ingredients, producible)
            if is_producible:
                producible_recipes.append(recipe)
        return producible_recipes

    def can_produce(self, recipe, recipes, ingredients, producible) -> bool:
        if recipe in producible:
            return True
        recipe_index = recipes.index(recipe)
        for ingredient in ingredients[recipe_index]:
            if ingredient in producible:
                continue
            if ingredient in recipes:
                if self.can_produce(ingredient, recipes, ingredients, producible):
                    producible.add(ingredient)
            else:
                return False
        return True


if __name__ == "__main__":
    assert Solution().findAllRecipes(["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]],
                                     ["yeast", "flour", "meat"]) == ["bread", "sandwich"]
    assert Solution().findAllRecipes(["bread", "sandwich", "burger"],
                                     [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]],
                                     ["yeast", "flour", "meat"]) == ["bread", "sandwich", "burger"]
    Solution().findAllRecipes(["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"],
                              [["d"], ["hveml", "f", "cpivl"], ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"],
                               ["cpivl", "hveml", "zpmcz", "ju", "h"], ["h", "fzjnm", "e", "q", "x"],
                               ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"], ["f", "hveml", "cpivl"]],
                              ["f", "hveml", "cpivl", "d"])
