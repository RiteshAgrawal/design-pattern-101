class MyList(list):
    def get(self, index, default_param=None):
        try:
            return self[index]
        except:
            return default_param


if __name__ == '__main__':
    l = MyList([1,2,3,4])
    print(l.get(0))
    print(l.get(5, -1))


