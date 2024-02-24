#two.py
import one
print("Top lvl in two.py")

one.func()

if __name__ == '__main__':
	print("Two.py is being run directly")
else:
	print("two.py has been imported")