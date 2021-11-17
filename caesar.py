alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print("vvedi otstup")
otstup = int(input())
print("vvedi tekst")
text = raw_input().strip()
result = ''
for char in text:
    result += alphabet[(alphabet.index(char) + otstup) % len(alphabet)]
print(result)    
