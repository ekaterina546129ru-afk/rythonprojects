# Два бандита 
cans_killed = input()
cans_killed_list = cans_killed.split()

Larry = int(cans_killed_list[0])
Garry = int(cans_killed_list[1])

dont_killed_Larry = Garry - 1
dont_killed_Garry = Larry - 1

print(f"{dont_killed_Larry} {dont_killed_Garry}")