import hashlib
import sys
import colorama
import os
from colorama import Fore, Style, Back

# TODO: Make This Program controlled by command line (DONE!)
# TODO: Hash must be in a txt file (DONE!)

# TODO: next feature for hash.txt (DONE!)
# TODO: Figure Out A Way To Get To The Other Hash! (DONE!)

# TODO: Make This Thing Prettier (Colorama) (DONE!)
# TODO: getopt intergation (command line arguments advanced) (KINDA)
# TODO: Save Function to save all your data (DONE!)
# TODO: Save Function for non_work_files
# TODO: Fix THe ERROR!
colorama.init()

hashes = []
working_hashes = []
non_working_hashes = []


def main():
    if (sys.argv == None):
        print(Fore.YELLOW+"[-]"+"Please Provide Runtime Variables (MD5 Hash, Wordlist Path")
        exit()

    try:
        md5_hash_parameter = sys.argv[1]
        wordlist_input = sys.argv[2]
        output_file = sys.argv[3]
        
    except:
        print(Fore.RED+"[-]"+"please Provide Runtime Variables (MD5 Hash File / MD5 Hash, Wordlist Path, output_file.txt")
        exit()
    try:
        with open(md5_hash_parameter, 'r') as mF:
            for hash_ in mF:
                hashes.append(hash_)
            
    
    except:
        hashes.append(md5_hash_parameter)
            #crack(hash_, wordlist_input)
    readHash(wordlist_input) 


def banner():
    pass
def readHash(wordlist_input_):
    for _hash in hashes:
        crack(_hash , wordlist_input_)       

def crack(_hash, wordlist_input):
    with open(wordlist_input, 'r') as f:

        for line in f:
            line_ = hashlib.md5(line.encode("utf-8").strip()).hexdigest()
            
            if (line_.strip() == _hash.strip()):
                
                working_hash = str(line.strip() + ":" + line_.strip())
                working_hashes.append(working_hash)
                

                if (len(hashes) != 0): 
                    hashes.pop(0)
                    
                if (len(hashes) == 0): 
                    print (Fore.BLUE+"[*] All Hashes Cracked!")
                    createOutputFile(working_hashes, non_working_hashes)
                    exit()
                readHash(wordlist_input)

            elif line_.strip() != _hash.strip():
                print (Fore.LIGHTMAGENTA_EX+ "[*] Attempting Password: {}".format(line), end='')
                
                if ("" == line):
                    print (Fore.LIGHTRED_EX + "[-] No Words Found In Provided Wordlist! Try Another One!")
                    non_working_hashes.append(line__)
                
                    readHash(wordlist_input)
            #createOutputFile(working_hashes, non_working_hashes)
            #readHash(wordlist_input)      
    
        
def createOutputFile(on_hash, non_hash):
    outputFile = open("output.txt","w+")
    for hash_ in working_hashes:
        outputFile.write(hash_+'\n')
        print (Fore.LIGHTGREEN_EX+"[+]"+"Password Compromoised - Password: {}".format(hash_))
    outputFile.close()
    print(Fore.RESET+"[+] Cracked Hashes Sent To output.txt File!")
    
    
    
                
if __name__ == "__main__":
    main()
