# yahooコメント欄からコメント、ユーザー名、日付、賛成数、反対数を取得するコード
# end と url を標準入力から受け取る

import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

class YahooNewsCommentScraping:
    
    comment_boxes = []
    comments = []
    names = []
    dates = []
    agrees = []
    disagrees = []

    start = 1
    cou = 0
    
    def __init__(self, end, url):
        self.end = end
        self.url = url

    # コメント取得
    def get_comment(self, comment_box):
        elem_comment = comment_box.find_element_by_class_name("cmtBody")
        comment = "".join(elem_comment.text.split("\n"))
        self.comments.append(comment)
        print(comment)
    
    # ユーザー名取得
    def get_user_name(self, comment_box):
        elem_name = comment_box.find_element_by_class_name("rapidnofollow")
        name = elem_name.text
        self.names.append(name)

    # 日付取得
    def get_user_date(self, comment_box):
        elem_date = comment_box.find_element_by_class_name("date")
        date = elem_date.text
        self.dates.append(date)

    # good数取得
    def get_good_count(self, comment_box):
        agree_box = comment_box.find_element_by_class_name("good")
        elem_agree = agree_box.find_element_by_class_name("userNum")
        agree = elem_agree.text
        self.agrees.append(agree)

    # bad数取得
    def get_bad_count(self, comment_box):
        disagree_box = comment_box.find_element_by_class_name("bad")
        elem_disagree = disagree_box.find_element_by_class_name("userNum")
        disagree = elem_disagree.text
        self.disagrees.append(disagree)
    
    # csvファイルとして出力    
    def file_process(self):
        print(self.cou)   
        with open('tes.csv', 'a') as f:
            writer = csv.writer(f)
            for i in range(self.cou):
                print(i)
                writer.writerow([self.comments[i], self.names[i], self.dates[i], self.agrees[i], self.disagrees[i]])

    def scrape(self):
        # ブラウザのオプションを格納する変数をもらってきます。
        options = webdriver.ChromeOptions() 
        options.add_argument('headless') 
        driver = webdriver.Chrome(options=options) 
        for page in range(self.start, self.end):
            
            #self.url = self.url + "&s=lost_points&o=desc&t=t&p={}".format(page)
            #self.url = self.url + "{}".format(page)
            driver.get(self.url + str(page))
            time.sleep(5)
            iframe = driver.find_element_by_class_name("news-comment-plguin-iframe")
            driver.switch_to.frame(iframe)

            self.comment_boxes = driver.find_elements_by_class_name("root")
    
            for comment_box in self.comment_boxes:
                self.get_comment(comment_box)        
                self.get_user_name(comment_box)
                self.get_user_date(comment_box)
                self.get_good_count(comment_box)
                self.get_bad_count(comment_box)

                self.cou+=1 # for debug
        self.file_process()

def main():
    input_end = int(input())
    input_url = input()
    obj = YahooNewsCommentScraping(input_end, input_url)
    obj.scrape()

if __name__ == "__main__":
    main()

# ex.
# url = "https://headlines.yahoo.co.jp/cm/main?d=20200428-00050198-yom-soci"
