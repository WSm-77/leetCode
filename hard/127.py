from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        INF = float("inf")
        wordList.append(beginWord)
        graph = self.createGraph(wordList)
        V = len(wordList)
        distances = {wordList[i] : INF for i in range(V)}
        visited = {wordList[i] : False for i in range(V)}
        toCheck = deque()
        toCheck.append(beginWord)
        distances[beginWord] = 1
        visited[beginWord] = True

        while toCheck:
            currentWord = toCheck.popleft()

            for neighbour in graph[currentWord]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    distances[neighbour] = distances[currentWord] + 1
                    if neighbour == endWord:
                        return distances[endWord]
                    toCheck.append(neighbour)
        
        return 0

    def createGraph(self, words):
        G: dict[list] = dict()
        for word in words:
            G[word] = []
            for key in G:
                if word == key:
                    continue
                if self.existsEdge(word, key):
                    G[key].append(word)
                    G[word].append(key)

        return G

    def existsEdge(self, word1, word2):
        if len(word1) != len(word2):
            return False
        
        differsCnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                differsCnt += 1
                if differsCnt > 1:
                    return False
        
        return True
    
if __name__ == "__main__":
    test = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(test.ladderLength(beginWord, endWord, wordList))