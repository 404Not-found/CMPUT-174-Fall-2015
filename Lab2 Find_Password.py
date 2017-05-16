# Yunshu Zhao and Etienne Asselin
# 2015 Fall Term
# University of Alberta

import random;

def instructions():
    instructions = ["A group of possible passwords will be displayed.",
                   "You must guess the password. You have at most 4 guesses.",
                   "If you are incorrect, you will be told how many letters in",
                   "your guess were in exactly the correct location of the password."];
    for line in instructions :
        print(line);

def wordlist():
    words = ["PROVIDE","SETTING","CANTINA","CUTTING","HUNTERS","SURVIVE","HEARING",
         "HUNTING","REALIZE","NOTHING","REALIZE","NOTHING","OVERLAP","FINDING",
         "PUTTING"];
    tempans="HUNTING";
    
    
    for position in words:
        print(position);
    
    return tempans;

def passentry(passarg1):
    return input("Enter password ("+str(passarg1)+" guesses remaining) >")+"       ";

def check(one,two):
    count=0;
    for i in range(7):
        if one[i] == two[i]:
            count += 1;
    return count; 

def main():    
    instructions();
    
    answer=wordlist();
    
    attempt = 4;
    while attempt >= 1 :
        guess=passentry(attempt);
        if guess==answer+"       ":
            print("User login successful");
            attempt = 0;         
        else:
            if attempt == 1:
                print("User login unsuccessful");
            else:
                letters=check(guess,answer);
                print("Password incorrect","\n",str(letters)+"/7 correct");        
            attempt -= 1;

main();