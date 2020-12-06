class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        print(f"{self.name} - {self.email}")

    @classmethod
    def get_info_class(cls, data):
        name, email= data
        return cls(name, email)

    @staticmethod
    def get_info_static(self):
        print(f"{self.name} - {self.email}")


user_list = ['Admin2', 'test@test.com']

user = User.get_info_class(user_list)
user.get_info()
user.get_info_static(user)

    