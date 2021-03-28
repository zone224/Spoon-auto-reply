""" 変数・命名規約がてきとう  """"
import random
from selenium import webdriver
from time import sleep
from kaiji import Animation
import datetime

driver = webdriver.Chrome('C:/driver/chromedriver')

driver.get('https://www.spooncast.net/jp/')
# driver.maximize_window()
sleep(3)
def main():
    try:
        login_button = driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[3]/button[2]/div')
        login_button.click()
        sleep(5)
    except:
        login_button = driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[3]/button[2]/div')
        login_button.click()
        sleep(5)

    try:
        login_google_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div[2]/ul/li[2]/button/div[2]')
        login_google_button.click()
    except:
        login_google_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div/div[2]/ul/li[2]/button/div[2]')
        login_google_button.click()

    sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    enter_gmail = driver.find_element_by_xpath('//*[@id="identifierId"]')
    enter_gmail.send_keys('自分のGoogleのGmail')
    sleep(1)
    login_google = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
    login_google.click()
    sleep(3)
    enter_pw = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    enter_pw.send_keys('自分のパスワード')
    sleep(1)
    login_pw = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
    login_pw.click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    input_channel = driver.find_element_by_tag_name("input")

    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    """ ここで検索 """
    input_channel.send_keys('ここに検索したいユーザー名')
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー
    # ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー


    sleep(1)
    search_chanel_clicked = driver.find_element_by_xpath('//*[@id="root"]/div/header/div/div[2]/div/div[1]/button/div/img')
    search_chanel_clicked.click()
    sleep(5)
    channel_click = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div/ul/li[1]/div/div/figure/a[1]')
    channel_click.click()
    sleep(2)
    load_click = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[1]/button/div/img')
    load_click.click()
    try:
        textarea = '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/textarea'
        button = '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[2]/div[2]/button[2]/div'
    except:
        textarea = '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[3]/div[2]/textarea'
        button = '//*[@id="root"]/div/main/div/div/div[1]/div/div[2]/div[3]/div[2]/button[2]/div'

    def break_comment():
        break_comment_input = driver.find_element_by_xpath(textarea)
        break_comment_input.send_keys('----------------------------')
        break_comment_click = driver.find_element_by_xpath(button)
        break_comment_click.click()
    

    # 放送時間
    def stream_time(get_time):
        # print(get_time.text)

        if get_time.text == '5:00': 
            send_time_input = driver.find_element_by_xpath(textarea)
            send_time_input.send_keys('配信5分経過したよ～!')
            send_time_click = driver.find_element_by_xpath(button)
            send_time_click.click()
            sleep(1)
        if get_time.text == '10:00': 
            send_time_input = driver.find_element_by_xpath(textarea)
            send_time_input.send_keys('配信10分経過したよ～!')
            send_time_click = driver.find_element_by_xpath(button)
            send_time_click.click()
            sleep(1)
        if get_time.text == '30:00': 
            send_time_input = driver.find_element_by_xpath(textarea)
            send_time_input.send_keys('配信30分経過したよ～!')
            send_time_click = driver.find_element_by_xpath(button)
            send_time_click.click()
            sleep(1)
        if get_time.text == '60:00': 
            send_time_input = driver.find_element_by_xpath(textarea)
            send_time_input.send_keys('配信1時間経過したよ～!')
            send_time_click = driver.find_element_by_xpath(button)
            send_time_click.click()
            sleep(1)
        if get_time.text == '01:30:00': 
            send_time_input = driver.find_element_by_xpath(textarea)
            send_time_input.send_keys('配信1時間30分経過したよ～!')
            send_time_click = driver.find_element_by_xpath(button)
            send_time_click.click()
            sleep(1)
        if get_time.text == '01:55:00': 
            send_time_input = driver.find_element_by_xpath(textarea)
            send_time_input.send_keys('配信終了5分前だよ～!')
            send_time_click = driver.find_element_by_xpath(button)
            send_time_click.click()
            sleep(1)


    def janken(spoon_comment):
        """ じゃんけんの説明を送信 """"
        send_hello_input = driver.find_element_by_xpath(textarea)
        send_hello_input.send_keys('「グー」「チョキ」「パー」のどれかだしてね！')
        send_hello_click = driver.find_element_by_xpath(button)
        send_hello_click.click()
        sleep(1)
        send_hello_input = driver.find_element_by_xpath(textarea)
        send_hello_input.send_keys('じゃーんけーん')
        send_hello_click = driver.find_element_by_xpath(button)
        send_hello_click.click()
        sleep(1)
        send_hello_input = driver.find_element_by_xpath(textarea)
        send_hello_input.send_keys('ぽん')
        send_hello_click = driver.find_element_by_xpath(button)
        send_hello_click.click()

    def janken_result(spoon_comment, m):
        """ コメントでじゃんけんの手を取得したとき、結果を送信"""
        hands = ["グー", "チョキ", "パー"]
        rules = ["あいこだよ～", "あなたの負けだよ～", "あなたの勝ちだよ～"]
        userhuns = {"グー": 0,"チョキ": 1, "パー":2}

        # if spoon_comment in hands:
        sleep(2)

        win_or_lose = (userhuns[spoon_comment] - m) % 3
        if 0 <= win_or_lose < 3: 
            send_hello_input = driver.find_element_by_xpath(textarea)
            send_hello_input.send_keys(f"「{hands[m]}」をだしたよ！")
            send_hello_input.send_keys(f"{rules[win_or_lose]}")
            send_hello_click = driver.find_element_by_xpath(button)
            send_hello_click.click()
            sleep(1)

    def omikuji():
        """ 等確率のランダムでおみくじの結果を送信 """
        i = random.randint(0, 10)
        break_comment()
        omikuji_list = ['大吉', '中吉', '小吉', '吉', '半吉', '末小吉', '凶', '小凶', '半凶', '末凶', '大凶']
        send_omikuji_input = driver.find_element_by_xpath(textarea)
        send_omikuji_input.send_keys(f'{omikuji_list[i]}でした！\n')
        send_omikuji_click = driver.find_element_by_xpath(button)
        send_omikuji_click.click()
        break_comment()

    def saikoro():
        """ サイコロをランダムで送信 """
        me = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
        i = random.randint(1,6)
        send_saikoro_input = driver.find_element_by_xpath(textarea)
        send_saikoro_input.send_keys(f'{me[i-1]}    {i}')
        send_saikoro_click = driver.find_element_by_xpath(button)
        send_saikoro_click.click()
    
    def ochiru():
        """ 「おちる」「落ちる」というコメントに対して、「もう来るなよ」と送信　"""
        send_kuruna_input = driver.find_element_by_xpath(textarea)
        send_kuruna_input.send_keys('もう来るなよ')
        send_kuruna_click = driver.find_element_by_xpath(button)
        send_kuruna_click.click()
    
    def goodby():
        """ 「おつかれー」に対して、同じように返信する　"""
        send_goodby_input = driver.find_element_by_xpath(textarea)
        send_goodby_input.send_keys('おつかれー')
        send_goodby_click = driver.find_element_by_xpath(button)
        send_goodby_click.click()
        break_comment()
    
    def ransuu():
        """ 1~100までの乱数を送信 """
        i = random.randint(1,100)
        send_saikoro_input = driver.find_element_by_xpath(textarea)
        send_saikoro_input.send_keys(f'結果:{i}')
        send_saikoro_click = driver.find_element_by_xpath(button)
        send_saikoro_click.click()

    def msg_text(text):
        """ 送りたい文章を引数で受け取り、送信 """
        send_goodby_input = driver.find_element_by_xpath(textarea)
        send_goodby_input.send_keys(text)
        send_goodby_click = driver.find_element_by_xpath(button)
        send_goodby_click.click()



# ======================================================================================================================================================


    sleep(3)

    send_hello_input = driver.find_element_by_xpath(textarea)
    send_hello_input.send_keys('こんばんは！みなさん')
    send_hello_click = driver.find_element_by_xpath(button)
    send_hello_click.click()
    while True:
        sleep(1)
        get_comment = driver.find_elements_by_class_name('comment-text')
        get_name = driver.find_elements_by_css_selector('p.comment-name.text-box')
        spoon_comment = get_comment[-1].text
        spoon_name = get_name[-1].text

        print(spoon_comment)
        print(spoon_name)

        get_time = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[1]/div/div[1]/div[2]/div/ul/li[5]/button/div/span')
        stream_time(get_time)
        print(get_time.text)

        hello_msg = 'こんばんは！'
        hello_msg_list = [ 'こんにちは～', 'こんばんは～', 'Hello', '初見です！', '初見です']
        if spoon_comment in hello_msg_list:
            send_hello = spoon_name + 'さん' + hello_msg
            print(send_hello)
            send_hello_input = driver.find_element_by_xpath(textarea)
            send_hello_input.send_keys(send_hello)
            send_hello_click = driver.find_element_by_xpath(button)
            send_hello_click.click()
            break_comment()

        if ((spoon_comment[-6:] == 'こんばんは~') ) or (spoon_comment[-6:] == 'こんばんは！') or (spoon_comment[-5:] == 'こんばんは'):
            print(spoon_comment[5:])
            send_hello = spoon_name + 'さん' + hello_msg
            print(send_hello)
            send_hello_input = driver.find_element_by_xpath(textarea)
            send_hello_input.send_keys(send_hello)
            send_hello_click = driver.find_element_by_xpath(button)
            send_hello_click.click()
            break_comment()

        if spoon_comment == 'じゃんけん':
            janken(spoon_comment)

        hands = ["グー", "チョキ", "パー"]
        m = random.randint(0, 2)
        if spoon_comment in hands:
            janken_result(spoon_comment, m)

        if spoon_comment == 'おみくじ':
            omikuji()
        
        if spoon_comment == 'サイコロ':
            saikoro()

        if spoon_comment == '乱数':
            ransuu()

        if spoon_comment == '落ちる' or spoon_comment == 'おちる': 
            ochiru()   

        if spoon_comment == 'おつかれー':
            goodby()
            
        # 映画・漫画「カイジ」の主人公の名言を送信(ランダム)
        if spoon_comment == 'カイジ':
            kaji_text = Animation().kaiji()
            msg_text(kaji_text)

        # 映画・漫画「カイジ」の利根川の名言を送信(ランダム)
        if spoon_comment == '利根川':
            tonegawa_text = Animation().tonegawa()
            msg_text(tonegawa_text)

        if spoon_comment == '乗算':
            setumei = '乗算を計算をします。(例:「12 9」のように入力してください！)'
            msg_text(setumei)

        s_blank = spoon_comment
        s_blank_list = s_blank.split()
        try:
            if type(int(s_blank_list[0])) == int and  type(int(s_blank_list[-1])) == int:
                msg1 = int(s_blank_list[0])
                msg2 = int(s_blank_list[-1])
                result = msg1 * msg2
                print(result)
                sent_message = f'計算結果⇒{result}'
                msg_text(sent_message)
        except ValueError:
            pass

        if spoon_comment == "現在日時":
            dt_now = datetime.datetime.now()
            now_ydt = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
            print(now_ydt)
            msg_text('現在 |' + now_ydt)

if __name__ == '__main__':
    main()