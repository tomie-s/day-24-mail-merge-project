PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as name_file:
    invited_guests = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in invited_guests:
        guest_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, guest_name)
        with open(f"Output/ReadyToSend/letter_for_{guest_name}.txt", mode='w') as file:
            file.write(new_letter)
