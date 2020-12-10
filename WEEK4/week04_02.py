class Value:
    def __init__(self):
        self.amount = 0

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = value - value * obj.commission

