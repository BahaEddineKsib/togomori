import os


def pp(msg,end='\n',print_it=True):

	end_with = end
	if print_it:
		print(msg,end=end_with)
	with open('output.txt','a') as f:
		f.write(str(msg)+end_with)
	


def clear():
	os.system('clear')
	with open("output.txt", "w") as f:
		f.write('')
