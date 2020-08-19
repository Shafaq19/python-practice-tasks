class SingletonFactory:
    '''
    turns every class in to singleton
    '''
    minstances = {}

    def __init__(self, class_type):
        self.class_type = class_type


    def __call__(self, *args, **kwargs):
        if (self.class_type not in SingletonFactory.minstances):
            SingletonFactory.minstances[self.class_type] = self.class_type(*args, **kwargs)
        return SingletonFactory.minstances[self.class_type]


@SingletonFactory
class TestClass:
    def test_func(self):
        print("testfunc called")


if __name__ == '__main__':
    m = TestClass()
    j=TestClass()
    j.test_func()

