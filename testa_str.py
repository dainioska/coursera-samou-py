str1 = "ekranuotas tekstas \"yra cia\" "
str2 = r"ekranuotas tekstas \"yra cia\" "
print(str1)
print(str2)
#####
str3 = "pirmas" \
       "antras"
print(str3)
#####
str4 = """
22222222222222222222222222222222222222222 

    3333333333333333333333333333333333333
    """
print(str4)
#####
print("davai " *6)
print(id(str4))
print(id(str4 + "plius"))
##### 
print(str3[3:] +", " + str3[2:8])
#####
str5 = "12345678910"
print(str5[::-2])
#####string methods
print("2021".capitalize())
print("2020".isdigit())
#####
"3.14" in "3.1455555"
#####
for letter in str5:
    print("dig: ", letter)
##### FORMAT#############################!!!!!!!!!!!!!!!!!
str6 = " {} plius, {} minus ({})".format("PLIUS", "MINUS"," ALIO ")
print(str6)
str7 = "{num} MHZ das ist {sign}".format(num=555, sign="fine")
print(str7)
##### from python3.6
sub = "optimalus"
auth = "dainius"
print(f"sprendimas {sub}----priimtas yra {auth}")
##### modification
num = 10
print(f"binarnikas: {num:#b}")
num = 2/3
print(f"{num:#10f} sekundes")
##### convert to ASCI
name = input("ivesk: ")
print(name)
#####
str8 = b"hello"
for asci in str8:
    print(asci)
#####
str9 = "zzzLT"
print(str9.encode(encoding="utf-8"))



