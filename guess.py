import random
from warnings import catch_warnings


with open("word5.txt") as f:
    data = f.read().splitlines()

def guess(wordlist=data,chars=[],not_chars=[],wrong_words=[],first="",second="",third="",fourth="",fifth=""):
    sub_wordlist,sub_subwordlist,final_subwordlist = [],[],[]
    for word in wordlist:
        contain_all =  all(item in word for item in chars)
        contain_any =  any(item in word for item in not_chars)
        if contain_all and not contain_any:
            sub_wordlist.append(word)
    print("There are {} options in sub_wordlist".format(len(sub_wordlist)))
    print("\n==================================\n")
    for word in sub_wordlist:
        if ((word[0] == first or first =="") and
        (word[1] == second or second =="") and
        (word[2] == third or third =="") and
        (word[3] == fourth or fourth =="") and
        (word[4] == fifth or fifth =="")):
            sub_subwordlist.append(word)
            # print(word)
    print("There are {} options in sub_subwordlist".format(len(sub_subwordlist)))
    print("\n==================================\n")
    

    final_subwordlist = sub_subwordlist.copy()
    for word in sub_subwordlist:
            for wrong in wrong_words:
                if ((word[0] == wrong[0]) or
                (word[1] == wrong[1]) or
                (word[2] == wrong[2]) or
                (word[3] == wrong[3]) or
                (word[4] == wrong[4])):
                    # print("Removing .... {}".format(word))
                    try:
                        final_subwordlist.remove(word)
                    except ValueError as err:
                        # print("Could not remove word({}) as it removed before.".format(word))
                        # print(err)
                        pass
                    # finally:
                    #     pass
    final_subwordlist = set(final_subwordlist)  
    for word in final_subwordlist:
        print(word) 
    print("There are {} options in final_subwordlist".format(len(final_subwordlist)))
    print("\n==================================\n")    


# Logic Scenario
rand1,rand2,rand3 = random.choice(data),random.choice(data),random.choice(data)
chars,not_chars,first,second,third,fourth,fifth = "","","","","","",""
wrong_words = []
print("Three Random Words to start with : " + rand1,rand2,rand3)
for i in range(6):
    chars += input("Enter new found Letters: ").lower()
    not_chars += input("Enter new not found Letters: ").lower()
    wrong_words.append(input("Enter new wrong word (must be 5): ").lower())
    first = input("Enter First Letter: ").lower()
    second = input("Enter second Letter: ").lower()
    third = input("Enter third Letter: ").lower()
    fourth = input("Enter fourth Letter: ").lower()
    fifth = input("Enter fifth Letter: ").lower()
    
    guess(data,chars,not_chars,wrong_words,first,second,third,fourth,fifth)