def solution(begin, target, words):
    if not target in words:
        return 0

    words = [begin] + words
    visited = [0] * len(words)

    def dfs(words, v, visited):
        for i in range(len(words)):
            cnt = 0
            for j in range(len(begin)):
                if words[v][j] == words[i][j]:
                    cnt += 1
            if cnt == len(target) - 1:
                if visited[i] != 0:
                    if visited[i] > visited[v] + 1:
                        visited[i] = visited[v] + 1
                        dfs(words, i, visited)
                else:
                    visited[i] = visited[v] + 1
                    dfs(words, i, visited)

    dfs(words, 0, visited)
    return visited[words.index(target)]
