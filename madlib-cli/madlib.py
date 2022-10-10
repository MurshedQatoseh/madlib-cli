import re  

def read_template():
    """
    Returns the template.txt file 
    """
    file = open("assets/make_me_a_video_game_template.txt",'r')
    content = file.read()
    return content

def parse(constant): 
    """
    Returns a list of words inside {} in a given text
    Arguments:
        constant {string} -- text contains words inside {}
    Output:
        lst {list of string} -- the words inside {} 
    """
    lst=[]
    res = re.findall(r'\{.*?\}', constant) # to find all the curly braces which have value inside it too then put all of them and their values inside res
    for i in res:
        lst.append(i.strip("{ }"))    # to remove every value in curly braces ,and get empty curly braces 
    return lst

def merge(constant , words):  

 
    lst = parse(constant)  
    
    return (re.sub(r' {[^}]*}',' {}',constant)).format(*words) 
def copyFile(text):
    print(text)
    file = open('assets/make_me_a_video_game_output.txt','w')
    file.write(text)

# here the execting happen
if __name__ == "__main__":
    print("Welcome to Madlib Game")
    print("You will be asked to input some words to play the game !!!")
    content = read_template()
    lst = parse(content)
    words=[]
    for i in range(len(lst)):
        words.append(input("enter a {} ".format(lst[i])))
    toCopy = merge(content, words)
    copyFile(toCopy)

