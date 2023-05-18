# store [name] in name_holder
name_holder = "[name]"

with open("./Input/Names/invited_names.txt") as txt_name:
    # readlines() return the list of laa the names in invited_names.txt
    name_list = txt_name.readlines()

# reading the content of letter by using read function
with open("./Input/Letters/starting_letter.txt") as letter_text:
    letter_content = letter_text.read()

    # first remove the extra spaces from the name_list and change the [name] to invited_names
    for n in name_list:
        # removing spaces from names of names_list
        stripped_name = n.strip()
        # replacing the [name] from names of names_list
        new_name = letter_content.replace(name_holder, stripped_name)
        # creating new txt files by writing mode
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}.txt",mode="w") as completed:
            completed.write(new_name)

