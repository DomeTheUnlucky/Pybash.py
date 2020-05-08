import sys
import os
from os import listdir
from os.path import isfile, join
import shutil
from colorama import Fore
from colorama import Style


#File manipulating functions

def rmtree():
	shutil.rmtree(sys.argv[2])


def rmdir():
	try:
		os.rmdir(sys.argv[2])
	except:
		print("The dir is not empty!")
		print("You can use rmtree to delete the dir and it's contents!")

def cp():
	src = sys.argv[2]
	dst = sys.argv[3]
	shutil.copy(src, dst)


def mkdir():
	os.mkdir(sys.argv[2])

def ls():
	for f in listdir(os.getcwd()):
		if isfile(join(os.getcwd(), f)):
			print(f)

def ld(val):
	return next(os.walk(val))[1] # Thank you @eryksun


def ls_dir():
	print("----------------------------")
	for fold in ld(os.getcwd()):
		print(f'{Fore.GREEN}{fold}{Style.RESET_ALL}')
 
def cat():
	f = open(file, 'r')
	file_contents = f.read()
	print (file_contents)
	f.close()


def ls_dir():
	print("----------------------------")
	for fold in ld(os.getcwd()):
		print(f'{Fore.GREEN}{fold}{Style.RESET_ALL}')

def ls_all_files():
	print("----------------------------")
	for f in listdir(os.getcwd()):
		if isfile(join(os.getcwd(), f)):
			print(f)

def mv():
	file_to_move = sys.argv[2]
	where_to_move = sys.argv[3]
	shutil.move(file_to_move, where_to_move)


command = sys.argv[1]

if command == "cat":
	file = sys.argv[2]
	cat()

if command == "ls":
	ls_dir()
	ls_all_files()	
	print("----------------------------")

if command == "mv":
	mv()

if command == "cp":
	cp()

if command == "mkdir":
	mkdir()

if command == "rmdir":
	rmdir()

if command == "rmtree":
	rmtree()
