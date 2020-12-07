# class Singelton:
#     isinstance = None

#     def __new__(cls):
#         if cls.isinstance is None:
#             cls.isinstance = super().__new__(cls)

#         return cls.isinstance

# a = Singelton()
# b = Singelton()
# print(a is b)