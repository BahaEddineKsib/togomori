from executor import execute
import readline
import sys
import GlobalVars as TopG




print('╺┳╸┏━┓┏━╸┏━┓┏┳┓┏━┓┏━┓╻\n'
     +' ┃ ┃ ┃┃╺┓┃ ┃┃┃┃┃ ┃┣┳┛┃\n'
     +' ╹ ┗━┛┗━┛┗━┛╹ ╹┗━┛╹┗╸╹ version 0.0\n')


run = True
while run:
	CW = "["+ TopG.CURRENT_WORKSHOP+"]" if TopG.CURRENT_WORKSHOP else ""
	CD = "["+ TopG.CURRENT_DOMAIN  +"]" if TopG.CURRENT_DOMAIN   else ""
	IN =  input("\n┌─"+CW+""+CD+"🕵"
	           +"\n└─>>> ")
	run = execute(IN)
