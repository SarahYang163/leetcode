class exception:
    def demo(self):
        try:
            a = 0 / 1
            print("0")
        except Exception as e:
            print(e)
            print("exception")
        else:
            print(1)
        finally:
            print("yes")


test = exception()
test.demo()
