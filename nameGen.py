#!/usr/bin/env python
import argparse
import random
import time

def loadBaseModel(filePath):
	base = list()
	if filePath:
		with open(filePath) as f:
			for line in f:
				base.append(line.strip().lower())
	return base

def generateModel(baseModel=[], base=1):
	model = dict()
	if baseModel:
		for word in baseModel:
			word += "\n"
			string = ""
			for c in word:
				if len(string) == base:
					if word not in model:
						model[string] = list()
					model[string].append(c)
				string += c
				if len(string) > base:
					string = string[1:]
	return model

def generateName(model=None, length=random.randint(6, 10)):
	if model:
		name = random.choice(model.keys())
		base = name
		while True:
			nextChar = random.choice(model[base])
			if len(name) >= length or nextChar == '\n':
				break
			name += nextChar
			base += nextChar
			base = base[1:]
		return name

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('baseFilePath')
	parser.add_argument('base', type=int)

	args = parser.parse_args()
	random.seed(time.time())

	baseModel = loadBaseModel(args.baseFilePath)
	model = generateModel(baseModel, args.base)
	name = generateName(model)
	print name

if __name__ == '__main__':
	main()
