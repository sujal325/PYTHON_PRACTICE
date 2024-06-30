print("Welcome to average height calculater.")
s_h = input("Write student heights: ").split()
ph = 0
s_t = len(s_h)
for av in s_h:
    pv = int(av)
    ph += pv
average = ph / s_t
print(f"TOTAL HEIGHT: {ph}\nTOTAL STUDENT: {s_t}\nAVERAGE HEIGHT: {average}")
