### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.
#having trouble
def welcome_assignment_answers(question):

    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = ""
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = ""
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = ""
    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code -":
        answer = ""
    elif "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = ""
    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = ""
    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = ""
    else: 
        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
        answer = "This is not my beautifu l wife! This is not my beautiful car! How did I get here?"
    return(answer)


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
