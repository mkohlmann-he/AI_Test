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
    print("/n>>> Start of 'init' function <<<")
	#Add Try-Except here
    kbFile_name = "knowledge_base.txt"
    kbFile = open(kbFile_name, "r")
    kbFileEntries = [line.strip("\n") for line in kbFile.readlines()]
    #print("\nEntire File contains:/n") #Debug
    #print(kbFileEntries) #Debug
	
	#Initialize the Dictionary Structure
    KB = {}
	
	#process Entries
    #print("\nParsed Entries goes to:") #Debug
    for kbEntry in kbFileEntries:
        kbEntry = kbEntry.strip("/n")
        #print(kbEntry) #Debug
        addKeywordToDictionaryFromFile(KB, kbEntry)
	
    print("\nPost Process Check:")
    print(KB)
    kbFile.close()
    
    print("/n>>> END of 'init' function <<<")
    return KB
	
def main(KB):
    print("/n>>> START of 'main' function <<<")
    print("/n>>> END of 'main' function <<<")
    return

def addKeywordToDictionaryFromFile(KB, entry):
    parsedLine = entry.split()
    addKeywordToDictionary(KB, parsedLine[0],parsedLine[1],parsedLine[2])
    return
    
def addKeywordToDictionary(KB, Key1, Operator, Key2):
    # Pre-validate
    ValidOperators = ["is","isa"]
    if Operator in ValidOperators:
        createKeyIfNeeded(KB, Key1)
        createKeyIfNeeded(KB, Key2)
        # Run appropriate operation
        if Operator == "is": # is condition
            KB[Key1][0].append(Key2)
            KB[Key2][2].append(Key1)
        elif Operator == "isa": # isa condition
            KB[Key1][1].append(Key2)
            KB[Key2][2].append(Key1)
    else:
        print("Warning >> Invalid Operator: Expecting " + str(ValidOperators) +"."
        print("        >> Received '" + str(Operator) + "'. Ignoring entry and continuing.")

    return
	
def createKeyIfNeeded(KB, Key):
    #Add first keyword to dictionary, if it doesn't already exist
    if Key not in KB:
        KB[Key] = [[],[],[]]
    return


print("/n>>> START of Run <<<")        
KB = init()
main(KB)
raw_input("/n>>> END of Run <<</npress Enter to Exit")
