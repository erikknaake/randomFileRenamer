import os
import argparse
import random

parser = argparse.ArgumentParser(description='A random file renamer')
parser.add_argument('-f', '--folder', default='./', help='The folder to rename all files for', type=str)
parser.add_argument('-a', '--alphabet', default='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_', help='Characters that can be used in the rename', type=str)
parser.add_argument('-l', '--length', default=13, help='Number of characters to use', type=int)
args = parser.parse_args()

def generateName(alphabet, length):
	result = ''
	for i in range(0, length):
		result += random.choice(alphabet)
	return result

def getName(alphabet, length, root, extension):
	return root + generateName(alphabet, length) + extension

for root, dirs, files in os.walk(args.folder):
	for file in files:
		extension = os.path.splitext(file)[1]
		os.rename(root + file, getName(args.alphabet, args.length, root, extension))