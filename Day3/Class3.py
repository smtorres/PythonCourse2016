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

