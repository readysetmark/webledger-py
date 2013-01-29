#fragment start *
import ledgertree
import os
import time

#-------------------------------------------------
# support for writing output to a file
#-------------------------------------------------
def writeln(*args):
	for arg in args:
		f.write(str(arg))
	f.write("\n")

if __name__ == "__main__":
	output_filename = "output\\ledgertree_driver.txt"
	#source_filename = "input\\test.dat"
	#source_filename = "input\\ledger.dat"
	source_filename = os.getenv("LEDGER_FILE", "input\\ledger.dat")
	
	t1 = time.time()
	tree = ledgertree.parse_into_ledgertree(source_filename)
	t2 = time.time()

	print "~"*80
	print "Here is the ledger tree:"
	print "~"*80
	f = open(output_filename,"w")
	f.write(tree.to_string())
	f.close()
	print(open(output_filename).read())

	print "Took %0.3f ms to parse" % ((t2-t1)*1000.0)
