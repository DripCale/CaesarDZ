print("Vvedi text")
text = raw_input()
print("Vvedi key")
key = raw_input()
alpha_eng=[chr(ord('a')+i) for i in range(26)]
key_opti="".join(list(key)*((len(text)//len(key))+len(key)))
vizener="".join([alpha_eng[(alpha_eng.index(i)+alpha_eng.index(j))%26]
if (alpha_eng.index(i)+alpha_eng.index(j))//26!=0 
else alpha_eng[alpha_eng.index(i)+alpha_eng.index(j)] 
for i,j in zip(text,key_opti)])
print(vizener)
