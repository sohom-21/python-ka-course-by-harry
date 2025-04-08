# Can you change the values inside a list which is contained in set S?
S = {8, 7, 12, "Harry", [1,2]}
# print(s)

# Nahi! Tum list ko set ke andar nahi rakh sakte.
# ⚠️ Kyun?
# Python me set ke andar sirf hashable (immutable) cheezein hi ja sakti hain — jaise integers, strings, tuples (agar unke andar bhi mutable cheezein na ho).
# List mutable hoti hai, isliye uska hash nahi banta, aur wo set me store nahi ho sakti.