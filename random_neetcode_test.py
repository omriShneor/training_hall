import csv
from random import sample
import webbrowser

CSV_FILE = "NeetCode150.csv"
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

class RandomTest:
    def __init__(self, testcases=2):
        self._testcases = 2

    def generate_test(self):
        with open(CSV_FILE, "r") as file:
            reader = csv.DictReader(file)
            questions_and_links = [(row["Question"], row["Link"]) for row in reader]
            test_cases = sample(questions_and_links, self._testcases)
            for i, (question, link) in enumerate(test_cases):
                print(f"Question No. {i+1}: {question}")
                webbrowser.get(chrome_path).open(link)
            
