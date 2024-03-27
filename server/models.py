from enum import Enum

class LanguageChoice(str, Enum):
	python = 'python'
	cpp = 'c++'
	java = 'java'
	
class QuestionChoice(str, Enum):
	q1 = 'Pivot Index'
	q2 = 'Minimum Paranthesis'
	q3 = 'Integer Break'
	q4 = 'SubArray Sum Equals K'