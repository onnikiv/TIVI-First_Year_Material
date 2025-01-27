import numpy as np

# 1. tehtävä ---------------------
random_taulukko = np.random.randint(0, 100, 20) # 0-100, 20 numeroa
sort_taulukko = np.sort(random_taulukko)
reshaped_taulukko = sort_taulukko.reshape(4, 5) # 4x5= 20 yksikköä

print(f"1.Tehtävä:\n{reshaped_taulukko}\n")

# 2. tehtävä ---------------------
"""
 a) u  = 2i + 3j ,
    v =  4i - 7j 
 
 b) uu =  i +  j + k ,
    vv 3i -3j + 2k
"""

u = np.array([2, 3])
v = np.array([4, -7])

uu = np.array([1, 1, 1])
vv = np.array([3, -3, 2])

# 3. tehtävä ---------------------
# vektorin normi, sitten pyöristys 2-decimaalilla

normi_u = np.round(np.linalg.norm(u), 2)
normi_v = np.round(np.linalg.norm(v), 2)

normi_uu = np.round(np.linalg.norm(uu), 2)
normi_vv = np.round(np.linalg.norm(vv), 2)

print(f"3.Tehtävä:\n a) Vektorien normit:\n    {normi_u}\n    {normi_v} \n b) Vektorien normit:\n    {normi_uu}\n    {normi_vv}\n")
