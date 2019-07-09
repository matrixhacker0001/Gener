import sys

arr = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

fin = []

def help():
	print " A Hex Character List Generation tool"
	print " ==========================================="
	print " Usage: ./gener.py [options]"
	print ""
	print " all - print complete list with all hex values"
	print " {badchar} - badchar to remove. Format [\\x00][00][x00]"
	print " help - show this banner"
	return

def badchar(data):
	core = ""
	if ',' in data:
		data = data.split(',')
	else:
		d = data
		data = []
		data.append(d)

	char = []
	if len(data[0]) < 2:
		print "[-] Bad Char not passed correctly..!! Check it..!!"
		print "[-] Aborting..!!"
		exit()
	elif data[0].startswith('\\'):
		for i in data:
			i = i[2:]
			char.append(i)

		return char
	elif data[0].startswith('x'):
		for i in data:
			i = i[1:]
			char.append(i)
		return char
	else:
		return data

def gen(bad):
	for i in arr:
		code = ''
		for j in arr:
			c = i + j
			if c in bad:
				continue
			code += '\\x' + c
		fin.append(code)

	for i in fin:
		print i

title = '''                     ,;L.                     ,;           
         .Gt       f#i EW:        ,ft       f#i j.         
        j#W:     .E#t  E##;       t#E     .E#t  EW,        
      ;K#f      i#W,   E###t      t#E    i#W,   E##j       
    .G#D.      L#D.    E#fE#f     t#E   L#D.    E###D.     
   j#K;      :K#Wfff;  E#t D#G    t#E :K#Wfff;  E#jG#W;    
 ,K#f   ,GD; i##WLLLLt E#t  f#E.  t#E i##WLLLLt E#t t##f   
  j#Wi   E#t  .E#L     E#t   t#K: t#E  .E#L     E#t  :K#E: 
   .G#D: E#t    f#E:   E#t    ;#W,t#E    f#E:   E#KDDDD###i
     ,K#fK#t     ,WW;  E#t     :K#D#E     ,WW;  E#f,t#Wi,,,
       j###t      .D#; E#t      .E##E      .D#; E#t  ;#W:  
        .G#t        tt ..         G#E        tt DWi   ,KK: 
          ;;                       fE                      
                                    ,                      
'''
print title
print "------------------------------------------------------------\n"

if len(sys.argv) < 2:
	help()
elif sys.argv[1] == "help":
	help()
elif sys.argv[1] == "all":
	data = []
	gen(data)
elif len(sys.argv) > 1:
	data = badchar(sys.argv[1])
	gen(data)
else:
	help()
