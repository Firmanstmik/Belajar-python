# CASTING (Merubah dari satu tipe data ke tipe yang lain)

data_int = 9;
print("data = ", data_int, "type =", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #Akan bernilai false jika value int = 0
print("data = ", data_float, "type =", type(data_float))
print("data = ", data_str, "type =", type(data_str))
print("data = ", data_bool, "type =", type(data_bool))