import random


class Animation():

    def kaiji(self):

        kaiji_msg = [
            'カイジ「勝たなきゃ誰かの養分…」',
            'カイジ「信じるべきは オレの力……！」',
            'カイジ「キンキンに冷えてやがる！」',
            'カイジ「三度は転ばない…！出尽くした…！」',
            'カイジ「あろうことか…祈ってしまった…！」',
            'カイジ「次は勝てる…絶対にね…！」',
            'カイジ「無理…たぶん無理…っていうか不可能…」',
            'カイジ「耐えることなくして勝利はないんだっ…！」',
            'カイジ「迷ったら…望みだろ…！」',
            'カイジ「苦しく難しい決断に投げちまってそれを他人に預ける」',
            'カイジ「勝つべくして勝つ…！」',
            'カイジ「漕ぎ出せっ……！勝負の大海へっ……！」'
            ]
        i = random.randint(0, len(kaiji_msg))
        return kaiji_msg[i]

    def tonegawa(self):

        tonegawa_msg = [
            '利根川「ぶち殺すぞゴミめら！」',
            '利根川「甘えを捨てろ！」',
            '利根川「今まで生きてきた全てが丸ごと「本物」だった事を･･･」',
            '利根川「失い続けるんだ……貴重なチャンスを…」',
            '利根川「金はな……命より重いんだっ……！」',
            '利根川「ギャンブルで生き残るための心構え」',
            '利根川「勝たなきゃゴミ」'
        ]
        i = random.randint(0, len(tonegawa_msg))
        return tonegawa_msg[i]

# def main():
#     item = {'peach': '4', 'melon': '4', 'Cherry': '1', 'orange': '3', 'Grape': '4', 'persimmon': '3', 'strawberry': '3',
#             'watermelon': '7', 'pear': '4', 'grapefruit': '3', 'banana': '2', 'Apple': '5', 'pineapple': '6'}
#     fruit, val = random.choice(list(item.items()))
#     print(fruit, val)


# if __name__ == '__main__':
#     main()