from executor import execute
import readline
import GlobalVars as TopG




print('╺┳╸┏━┓┏━╸┏━┓┏┳┓┏━┓┏━┓╻\n'
     +' ┃ ┃ ┃┃╺┓┃ ┃┃┃┃┃ ┃┣┳┛┃\n'
     +' ╹ ┗━┛┗━┛┗━┛╹ ╹┗━┛╹┗╸╹ version 0.0\n')


run = True
while run:
	IN =  input("\n┌─🕵️ ["+ TopG.CURRENT_WORKSHOP+"]"
	           +"\n└─>>> ")
	run = execute(IN)
