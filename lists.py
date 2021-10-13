class Solution:
    def lists(self):
        N = int(input())
        result = list()
        for _ in range(N):
            x = input()
            res = x.split(' ')
            if res[0] == 'insert':
                result.insert(int(res[1]), int(res[2]))
            elif res[0] == 'print':
                print(result)
            elif res[0] == 'remove':
                result.remove(int(res[1]))
            elif res[0] == 'append':
                result.append(int(res[1]))
            elif res[0] == 'sort':
                result = sorted(result)
            elif res[0] == 'pop':
                result.pop()
            elif res[0] == 'reverse':
                result = sorted(result, reverse=True)
