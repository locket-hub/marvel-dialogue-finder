running = True

def userOptions(text_number):
    switcher = {
        1: 'Ant-Man.And.The.Wasp.txt',
        2: 'Ant-Man.txt',
        3: 'Avengers.Age.of.Ultron.txt',
        4: 'Avengers.Endgame.txt',
        5: 'Avengers.Infinity.War.txt',
        6: 'Avengers.txt',
        7: 'Black.Panther.txt',
        8: 'Captain.America.Civil.War.txt',
        9: 'Captain.America.The.First.Avenger.txt',
        10: 'Captain.America.The.Winter.Soldier.txt',
        11: 'Captain.Marvel.txt',
        12: 'Doctor.Strange.txt',
        13: 'Guardians.of.the.Galaxy.txt',
        14: 'Guardians.of.the.Galaxy.Vol. 2.txt',
        15: 'Iron-Man.2.txt',
        16: 'Iron-Man.3.txt',
        17: 'Iron-Man.txt',
        18: 'Spider-Man.Far.From.Home.txt',
        19: 'Spider-Man.Homecoming.txt',
        20: 'The.Incredible.Hulk.txt',
        21: 'Thor.Ragnarok.txt',
        22: 'Thor.The.Dark.World.txt',
        23: 'Thor.txt'
    }
    return switcher.get(text_number, 'Nothing')


def general_reader():
    options = '1) Ant-Man And The Wasp\n' \
              '2) Ant-Man\n' \
              '3) Avengers Age of Ultron\n' \
              '4) Avengers Endgame\n' \
              '5) Avengers Infinity War\n' \
              '6) Avengers\n' \
              '7) Black Panther\n' \
              '8) Captain America Civil War\n' \
              '9) Captain America The First Avenger\n' \
              '10) Captain America The Winter Soldier\n' \
              '11) Captain Marvel\n' \
              '12) Doctor Strange\n' \
              '13) Guardians of the Galaxy\n' \
              '14) Guardians of the Galaxy Vol 2\n' \
              '15) Iron-Man 2\n' \
              '16) Iron-Man 3\n' \
              '17) Iron-Man\n' \
              '18) Spider-Man Far From Home\n' \
              '19) Spider-Man Homecoming\n' \
              '20) The Incredible Hulk\n' \
              '21) Thor Ragnarok\n' \
              '22) Thor The Dark World\n' \
              '23) Thor\n'

    print(options)
    text_number = int(input('Choose a title: '))
    text = userOptions(text_number)

    directory = '/Users/escalators/Documents/Stuff/friendly-doodle/MCUDialogue/MCUDialogueTexts/' + text
    with open(directory, 'rb') as fp:
        line = fp.readline()
        line_string = line.decode()  # Can decode in "utf-8" if needed
        cnt = 1
        while line:
            line_string = "Line " + str(cnt) + ": " + line_string
            print(line_string)
            line = fp.readline()
            line_string = line.decode()
            cnt += 1
    print()


def line_finder():
    word = str(input("Insert line to search for: "))
    tally = 0
    for i in range(22):
        i += 1
        text = userOptions(i)
        directory = '/Users/escalators/Documents/Stuff/friendly-doodle/MCUDialogue/MCUDialogueTexts/' + text
        with open(directory, 'rb') as fp:
            line = fp.readline()
            line_string = line.decode()
            while line:
                if line_string.casefold().__contains__(word):
                    formatted = 'Here is a line from ' + text + " that contains " + word + ": " + line_string
                    print(formatted)
                    tally += 1
                line = fp.readline()
                line_string = line.decode()
    tally_string = "Line Tally: " + str(tally)
    print(tally_string)


def menu():
    print("Dialogue from every MCU movie up until Far From Home")
    user_input = int(input("What do you wish to do with it? \n1) Line Finder \n2) General Reader \n"))
    if user_input == 1:
        line_finder()
    if user_input == 2:
        general_reader()


class MCUReader:
    pass  # placeholder for future code


if __name__ == '__main__':
    while running:
        menu()
        continue_on = str(input("Would you like to continue? Y or N\n"))
        if continue_on == 'N' or continue_on == 'n':
            print("Quiting...")
            running = False
