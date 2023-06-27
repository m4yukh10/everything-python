#dice simulator
import random
dice = random.randint(1,6)
if dice == 1:
  print("   ")
  print(" * ")
  print("   ")
elif dice == 2:
  print("*  ")
  print("   ")
  print("  *")
elif dice == 3:
  print("*  ")
  print(" * ")
  print("  *")
elif dice == 4:
  print("*   *")
  print("     ")
  print("*   *")
elif dice == 5:
  print("*   *")
  print("  *  ")
  print("*   *")
else:
  print("*   *")
  print("*   *")
  print("*   *")
