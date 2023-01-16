import re
from pdfreader import text
def palindrom(fname):
    cnt=0
    output=list()
    j=0
    with open(fname, 'r', encoding='utf8') as file:
        for line in file:         
            for i in range (len(line)):
                _index=line.find(" ")
                if _index!=-1:
                    output.append(line[:_index+1])
                    line=line[_index+1:]
                else:
                    
                    break
                        
    
    file.close() 
    for i in range (0,len(output[i])):
        rev=output[i]
        rev=rev[::-1] 
        if output[i].lower().strip()==rev.lower().strip():
            print(output[i])
               


#palindrom('C:/Users/vpesp/VC projects/PythonCourse/text2.txt') 
digits=(re.findall('\d{3}/\d{2}',text))
print(digits)
#for i in range(len(digits)):
 #   print(digits[i])