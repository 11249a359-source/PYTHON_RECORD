large_num = float(input("Enter a number over 100: "))
small_num = float(input("Enter a number under 10: "))
times = large_num // small_num
exact = large_num / small_num
print(f"\nThe number {small_num} goes into {large_num} about {times} whole times.")
print(f"(Exact value: {exact})")
