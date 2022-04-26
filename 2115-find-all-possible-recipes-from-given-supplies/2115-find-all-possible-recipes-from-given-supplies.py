class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        #topological sort
        #indegree = {recipe: number of ingredients needed}
        indegree = defaultdict(int)
        for i, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
        #build a graph where key in the indegredient, and neighbors is a list of recipes that consume the ingredient
        graph = defaultdict(list)
        
        for i, ingredient in enumerate(ingredients):
            recipe = recipes[i]
            for ingre in ingredient:
                graph[ingre].append(recipe)
        
        #use a queue, where elements are supplies, so we bfs over supplies, and
        #when indegree of a recipe becomes 0, we add it to the queue and the result list
        queue = deque(supplies)
        res = []
        
        while queue:
            supply = queue.popleft()
            for recipe in graph[supply]:
                indegree[recipe] -= 1
                if indegree[recipe]==0:
                    queue.append(recipe)
                    res.append(recipe)
        
        return res