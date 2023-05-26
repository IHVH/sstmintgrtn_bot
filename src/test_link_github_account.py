import unittest
from bot_func_dictionary import BOT_FUNCTIONS_2, BOT_FUNCTIONS
import requests
import time

class TestGithubLink(unittest.TestCase):
    
    #@unittest.skip("skipping test_github_account_link_bot_functions_2")
    def test_github_account_link_bot_functions_2(self):
        for bf_key, bf_value in BOT_FUNCTIONS_2.items():
            for authr in bf_value.authors:
                url = f"https://github.com/{authr}"
                response = requests.get(url)
                self.assertEqual(response.status_code, 200, msg=f"{bf_key} {authr} The author's name must match the github account name to be able to generate a link!")
                time.sleep(1)

    #@unittest.skip("skipping test_github_account_link_old_bot_functions")
    def test_github_account_link_old_bot_functions(self):
        for bf_key, bf_value in BOT_FUNCTIONS.items():
            for authr in bf_value.authors:
                url = f"https://github.com/{authr}"
                response = requests.get(url)
                self.assertEqual(response.status_code, 200, msg=f"{bf_key} {authr} The author's name must match the github account name to be able to generate a link!")
                time.sleep(1)

if __name__ == '__main__':
    unittest.main()