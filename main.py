import os
import string

# A function that takes the name of the text file to be analyzed from the user and successfully opens the file.
def open_file():
    user_input = False
    while not user_input:
        file_name = input("Please enter the path of the file you want to perform the collocation query on:")
        # If such a file truly exists, let's open it; otherwise, let's ask for the input again.
        if os.path.exists(file_name):
            fp = open(file_name, "r")
            user_input = True
    return fp

# A function that processes the file line by line and creates the necessary data structure for the words in the file.
def read_data(fp):
    # We will maintain a dictionary where the key is a word and the value is a list.
    # This list will contain the numbers of the lines where the word appears.
    dict = {}
    line_number = 0
    for line in fp:
        line_number += 1
        # Here, we get rid of the punctuation and spaces at the beginning and end of the line.
        stripped_line = line.strip(string.punctuation+string.whitespace)
        for word in stripped_line.split():
            word = word.lower()
            # Here, we also get rid of the punctuation within the line.
            word = word.strip(string.punctuation)
            # In these three lines, we eliminate the -, _, and ' characters occurring within words.
            word = word.replace("-","")
            word = word.replace("'", "")
            word = word.replace("_", "")
            # We take action based on whether it currently exists in our dictionary.
            if word in dict:
                # If it is in the dictionary, we add another entry to the list of line numbers where this word appears.
                dict[word].append(line_number)
            else:
                # If it's not in the dictionary, it means this word appears for the first time on this line.
                dict[word] = [line_number]
    return dict

# A function that calculates collocation for the query words entered by the user and finds the result.
def find_cooccurance(S, inp_str):
    list_of_inputs = inp_str.split()
    number_of_lines = 0
    for word in S:
        number_of_lines = max(number_of_lines, max(S[word]))

    output_list_of_lines = []
    for line in range(number_of_lines):
        lline = line + 1
        this_line = True
        for input in list_of_inputs:
            if input in S and lline in S[input]:
                continue
            else:
                this_line = False
                break
        if this_line:
            output_list_of_lines.append(lline)

    return output_list_of_lines


# Main function.
def main():
    fp = open_file()
    S = read_data(fp)
    print(S)
    print ("Please enter your query sentence, leaving a space between each word.")
    print ("To exit the program, type 'Exit'.")
    query_sentence = input()
    while not query_sentence=="Exit":
        ll = find_cooccurance(S, query_sentence)
        if len(ll) > 0:
            print ("The lines where all the words in your query appear:")
            for l in ll:
                print ("    Line : {}".format(l), end= "...")
            print()
        else:
            print("There is no line in your file where all the words in your query appear.")
        print("Please enter a new query sentence, leaving a space between each word.")
        query_sentence = input()

# The function that calls the main function.
if __name__ == "__main__":
    main()

