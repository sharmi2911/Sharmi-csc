fname = open("30days30houroperations.txt","w+")
fname.write("I have completed 10 days Successfully.\n")
fname.close()
fname = open("30days30houroperations.txt","a")
fname.write("Tushar Jadhav")
fname.close()
fname = open("30days30houroperations.txt","r+")
print(fname.read())
fname.close()