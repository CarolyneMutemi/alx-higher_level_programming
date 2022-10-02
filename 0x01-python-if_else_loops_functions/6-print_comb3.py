#!/usr/bin/python3
for x in range(0, 9):
	for y in range (0, 10):
		if x != y and x < y:
			print(f"{x}{y}", end="")
			if x != 8:
				print(", ", end="")
print()
