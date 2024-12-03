import re

Done = False
while not Done:
    with open ("day-3/input.txt", "r+") as f:  
        content = f.read()
        match = re.search(r"don\'t\(\)(.*?)do\(\)", content)
        if match != None:
            print(match.span()[0], match.span()[1])
            newcontent = content[:match.span()[0]] + content[match.span()[1]:]
            # print(newcontent)
            f.seek(0)
            f.write(re.sub(r"<string>ABC</string>(\s+)<string>(.*)</string>", r"<xyz>ABC</xyz>\1<xyz>\2</xyz>", newcontent))
            f.truncate()
        else:
            Done = True
    
