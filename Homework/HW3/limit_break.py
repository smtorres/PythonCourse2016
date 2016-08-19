
import time

#####This code will eventually break - max recursion tree depth
def func(item):
    try:
#        code
        return something
    except:
        time.sleep(1)
        func(item)
for item in items:
    func(item)

#-or-
#### Best code for iterations
for item in items:
    not_finished=True
    while not_finished:
        try:
#            code
            not_finished=False
        except:
            time.sleep(1)

## good for one chunk of code, not for multiple terations
while True:
    try:
#        code
        break
    except:
        time.sleep(1)
