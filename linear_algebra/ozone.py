import pandas as pd

class Solution(object):
    def __init__(self):
        url = "https://raw.githubusercontent.com/reisanar/datasets/master/ozone.data.csv"
        c = pd.read_csv(url)
        print(c)


if __name__ == '__main__':
    Solution()