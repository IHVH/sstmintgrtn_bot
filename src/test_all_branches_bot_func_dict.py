import unittest
from bot_func_dictionary import BOT_FUNCTIONS_2, BOT_FUNCTIONS
from bot_func_abc import BotFunctionABC

class TestTeleBot(unittest.TestCase):
    
    def test_class_inherit_for_bot_functions_2(self):
        for bf_key, bf_value in BOT_FUNCTIONS_2.items():
            if not bf_value.state:
                continue
            c = type(bf_value.bot_function)
            self.assertIs(type(bf_value.bot_function).__base__, BotFunctionABC, msg=f"{c} {bf_key} Function class must be inherited from BotFunctionABC !!!")
            
    def test_fields_bot_functions_2(self):
        for bf_key, bf_value in BOT_FUNCTIONS_2.items():
            if not bf_value.state:
                continue
            self.assertGreaterEqual(len(bf_value.commands), 1, msg=f"{bf_key} There must be at least one command!!!")
            self.assertGreaterEqual(len(bf_value.authors), 1, msg=f"{bf_key} At least one author must be specified!")
            self.assertGreaterEqual(len(bf_value.about), 10, msg=f"{bf_key} About text is too short!")
            self.assertGreaterEqual(len(bf_value.description), 10, msg=f"{bf_key} Description text is too short!")

    def test_fields_old_bot_functions_dict(self):
        for bf_key, bf_value in BOT_FUNCTIONS.items():
            self.assertGreaterEqual(len(bf_value.commands), 1, msg=f"{bf_key} There must be at least one command!!!")
            self.assertGreaterEqual(len(bf_value.authors), 1, msg=f"{bf_key} At least one author must be specified!")
            self.assertGreaterEqual(len(bf_value.about), 10, msg=f"{bf_key} About text is too short!")
            self.assertGreaterEqual(len(bf_value.description), 10, msg=f"{bf_key} Description text is too short!")            
            
    def test_duplicate_command(self):
        commands = []
        for bf_key, bf_value in BOT_FUNCTIONS_2.items():
            for cmnd in bf_value.commands:
                self.assertFalse(cmnd in commands, msg=f"{bf_key} Added duplicate command '{cmnd}'! ")
                commands.append(cmnd)

        for bf_key, bf_value in BOT_FUNCTIONS.items():
            for cmnd in bf_value.commands:
                self.assertFalse(cmnd in commands, msg=f"{bf_key} Added duplicate command '{cmnd}'! ")
                commands.append(cmnd)

if __name__ == '__main__':
    unittest.main()