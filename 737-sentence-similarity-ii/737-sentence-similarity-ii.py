class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        # edge case
        if len(sentence1) != len(sentence2):
            return False
        
        # step 1. build a graph/adjacency list of similarPairs
        graph = defaultdict(set)
        for w1, w2 in similarPairs:
            graph[w1].add(w2)
            graph[w2].add(w1)
        
        
        def dfs(graph, visited, src_word, tgt_word):            
            if tgt_word in graph[src_word]:
                return True
            
            visited.add(src_word)
            
            for neighbor in graph[src_word]:
                if neighbor not in visited:
                    if dfs(graph, visited, neighbor, tgt_word):
                        return True
                    
            return False
        
        for w1, w2 in zip(sentence1, sentence2):
            # print(f"w1:{w1}, w2:{w2}")
            if w1==w2:
                continue
            if w1 not in graph:
                return False
            if not dfs(graph, set(), w1, w2):
                return False
        
        return True