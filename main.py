class NewList:
    def __init__(self, list):
        self.list = list

    def __reversed__(self):
        return reversed(self.list)

if __name__ == "__main__":
    list = NewList([0,1,4,7])
    print(reversed(list))