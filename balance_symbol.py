class BalanceSymbol:

    def __init__(self):
        self.items = []

    def split_string(self, string: str):
        self.items = list(string)
        return self.items

    def loop(self):
        arr = []
        symbol_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for k, v in enumerate(self.items):
            if v in symbol_dict.keys():
                last_one = arr[-1] if len(arr) > 0 else None
                print("checking now:", v, last_one)
                print("item no:", k, "total item:", len(self.items))
                if last_one != symbol_dict[v]:
                    return False
                else:
                    print("new array", arr)
                    arr.pop()
            else:
                arr.append(v)
                print("new array", arr)
        return True
