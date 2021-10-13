class Solution:
    def nested_list(self, marks: list):
        n = sorted(marks, key=lambda x: x[1])
        print(n)
        lowest = n[0][1]
        mid = None
        res = list()
        for i in range(len(n)):
            if mid is None and n[i][1] > lowest:
                mid = n[i][1]
            if mid is not None and n[i][1] == mid:
                print(n[i][0])
                res.append(n[i][0])
        return res


        # for i in range(len(n)):
        #     if lowest <= marks[i][1] < highest:
        #         print("before logic", marks[i], mid)
        #         if mid < marks[i][1]:
        #             res = list()
        #             mid = marks[i][1]
        #             print("after logic", mid)
        #         if mid == marks[i][1]:
        #             res.append(marks[i][0])
        #             print("mid match", res)
        # return res

