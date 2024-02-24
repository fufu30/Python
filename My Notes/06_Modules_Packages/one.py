#one.py

def func():
	print("func() in one.py")

print("Top LEVEL in one.py")

def func2():
	pass

def func3():
	pass

if __name__ == "__main__":
	#Run the script
	#for organisational purpose - here code gets executed:
	func2()
	func3()
