class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # set indegree of a recipe to be number of required ingredients
        indegree = defaultdict(int)
        # use a graph to connect ingredient and recipe
        graph = defaultdict(list)
        
        for recipe, ingre in zip(recipes, ingredients):
            indegree[recipe] = len(ingre)
            for ing in ingre:
                graph[ing].append(recipe)
        
        # iterate over the supply to decrement the indegree of recipe
        queue = deque(supplies)
        ans = []
        
        while queue:
            supply = queue.popleft()
            # a recipe is added to the queue only when it has indegree of 0
            if supply in recipes:
                ans.append(supply)
                
            for reci in graph[supply]:
                indegree[reci] -= 1
                if indegree[reci]==0:
                    queue.append(reci)
        
        return ans