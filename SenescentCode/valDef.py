# Character definition for Val

from delve_character import *


class Val(CharacterClass):

    def chapter_open(self, chapter_number, chapter_title='untitled'):
        open_html(self, f'html/c{chapter_number:03d}_val.html', f'c{chapter_number:03d}_val')
        self.cprint(f"\n\nChapter {chapter_number:03d}: {chapter_title} ##############################################\n\n")

    def chapter_101(self, en_output=True):
        self.en_output = en_output

        self.chapter_open(101)

        # Character initialization for Val as of chapter 101

        self.chclass = "Wouldn't you like to know?"  # todo working title

        self.level = 8  # todo function to calculate total required experience for a specific level and class rarity (could have sworn I wrote that already)
        self.cap = 8  # You think these are the real numbers, huh?

        # todo skill definitions
        # todo transfer stats, skills, etc from spreadsheet

        self.print_attributes()
        self.print_statistics()
        self.print_skills()

        self.chapter_close()
