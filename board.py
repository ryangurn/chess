class Board:

    def __init__(self):
        self.board = []

        for i in range(8):
            self.board.append([None] * 8)

    def __str__(self):
        retStr = ""
        retStr += self.rowLetters()
        for val, row in enumerate(self.board):
            val = val + 1
            retStr += str(val) + " "

            for cell in row:
                # todo: use columnValue rather than string "None |"
                retStr += "| None "

            retStr += "| "+str(val)+" \n"
        retStr += self.rowLetters()
        return retStr

    def rowLetters(self):
        retStr = ""
        rowLetters = ["H", "G", "F", "E", "D", "C", "B", "A"]

        for letter in rowLetters:
            retStr += "      " + str(letter)
        retStr += "\n"

        return retStr