from executor import execute
import readline




print('╺┳╸┏━┓┏━╸┏━┓┏┳┓┏━┓┏━┓╻\n'
     +' ┃ ┃ ┃┃╺┓┃ ┃┃┃┃┃ ┃┣┳┛┃\n'
     +' ╹ ┗━┛┗━┛┗━┛╹ ╹┗━┛╹┗╸╹ version 0.0\n')


run = True
while run:
	IN =  input("\n┌─🕵️"
	           +"\n└─conan> ")
	run = execute(IN)
	
