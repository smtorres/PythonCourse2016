raise Exception
print "I raised an exception!"

try:
	print b
except NameError:
	print "oops name error"	
except:
	print "opps"
finally:
	print "Yes! I did it!"
	
	
for i in range(1,10):
	if i==5:
		print "I found five!"
		continue
		print "Here is five!"
	else:
		print i
else:
	print "I went through all iterations!"
	
def Rename(entry):
    try:
     	if entry%1==0:
    		entry = str(entry)
    		if entry[-2] == '1':
    			return "%sth" %(entry)
     		elif entry[-1] == '1':
    			return "%sst" %(entry)
    		elif entry[-1] == '2':
    			return "%snd" %(entry)
    		elif entry[-1] == '3':
    			return "%srd" %(entry)  
    		else:
    			return  "%sth" %(entry)	
    	else:
    		return "Please do not enter decimal places." 	
    except:
    	return "Please enter an integer."
    finally: 
    	print "This is a function."
