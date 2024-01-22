olahraga = ("voly","senam","badminton","lompat","basket","futsal")

olahraga_list = list(olahraga)
olahraga_list.append("tenis")
print("update list = ",olahraga_list)
del olahraga_list[3]
print("hapus list = ",olahraga_list)
olahraga_list[4] = "sepak bola"
print("update = ",olahraga_list)
olahraga_tuole = tuple(olahraga_list)
