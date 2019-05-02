from random import randint
import time
import asyncio

def odds(start, stop):
	for i in range(start, stop+1,2):
		yield i

def random_sync():
	time.sleep(3)
	return randint(1,19)

def main():
	odd_values = [odd for odd in odds(3,15)]
	odds = tuple(odds(19,29))
	print(odd_values)
	print(odds)

if __name__=="__main__":
	main()
