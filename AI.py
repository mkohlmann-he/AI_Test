# Michael Kohlmann
# devCodeCamp.com
# 6/3/2015


# Stage 1
# 1. Initialize the knowledge base (KB) with anything it's already learned. "knowledge_base.txt"

# 2. Parse the KB entries into
#		- Object is adverb phrases and
#		- Object is a <member of group> phrases

# Stage 2
# 3. Commands to eventually program
#		- Add new is/isa relationship to the KB in local memory
#		- Display the relationships for an entry
#		- Backup existing KB back to the .txt file
#		- Scrape a "seed" website for more is/isa phrases.
#		- Auto crawl websites to continually build new relationship

# Data Structure:
# each entry is a dictionary item that follows a basic structure like this:
#
# dict{"keyword":[[is list],
#				[isa list],
#				[examples list]}
#
# So after processing these two statements, 
#	- apple is red
#	- apple is a fruit
#
# the dictionary would look like.
# KB{"apple"	:  [[red],
#				 	[fruit],
#				 	[]]
#	   "red"  	:  [[],
#					[],
#					[apple]]
#	   "fruit" 	:  [[],
#					[],
#					[apple]]}
#
#
#
def init(): #First Run, Open the knowledge base (KB) file and build the dictionary.
	#Add Try-Except here
    kbFile_name = "knowledge_base.txt"
    kbFile = open(kbFile_name, "r")
    kbFileEntries = [line.strip("\n") for line in kbFile.readlines()]
    print("Entire File contains:/n")
    print(kbFileEntries)
	
	#Initialize the Dictionary Structure
    KB = {}
	
	#process Entries
    print("Parsed Entries goes to:")
    for kbEntry in kbFileEntries:
        kbEntry = kbEntry.strip("/n")
        print(kbEntry)
        addKeywordToDictionary(KB, kbEntry)
	
    print("Post Process Check:")
    print(kbFileEntries)
    kbFile.close()
    return KB
	
def main():

	return

def addKeywordToDictionary(KB, entry):
	return KB
	
	
	
KB = init()
main()
raw_input("press Enter to Exit")
