import sys
sys.path.append(".")
import cnki_spyder_tool as cnki
from pprint import pprint as fprint

if __name__ == "__main__":

    input_file = open("../data/doc_url.txt","r",encoding="utf-8")
    
    while True:        
        line = input_file.readline()
        if not line:
            break
        cnki.get_doc_bibilo(line.strip())