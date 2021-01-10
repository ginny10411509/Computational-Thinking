print ("哈囉～我是晚餐機器人很高興為你服務！貼心服務讓你一次滿足")
hobby = "由於設計者愛吃海底撈火鍋所以主要為此設計的喔！最近天氣好冷喔～你有想吃什麼晚餐嗎？你想吃火鍋嗎！我也推薦你吃火鍋暖暖身體喔～"
print(hobby)

name=input("你好,請問大名是?:")
print(name,"很高興認識你!")

choose=input("想要吃哪一家的火鍋呢？！:")
print()

print("你想吃海底撈是嗎是嗎～我也很喜歡吃海底撈呢！特別是他的服務和湯底，真懂吃～")

soup_list=["蕃茄湯底","三鮮湯底","麻辣湯底"]
print("湯底選項",soup_list)

choose2=input("那你的湯底想要選哪種呢?:")
print(soup_list[0],"：愛吃番茄的人真的是必吃啊啊啊！健康又補血喔～")
print(soup_list[1],"：口感鮮香濃郁呢～不想要太膩這款最剛好喔～")
print(soup_list[2],"：愛吃辣的人就是要選這款啊！保證辣到你～")


meat_list=["牛肉","豬肉","羊肉"]
print("肉類選項",meat_list)

choose3=input("今天想要搭配哪種肉呢？")
print()

print(meat_list[0],"：建議你放下去8秒鐘就可以拿起來囉！")
print(meat_list[1],"：建議你煮久一點才不會拉肚子喔！")
print(meat_list[2],"：議你煮久一點，我們家的羊肉不太會有羊騷味喔～很好吃的")

staplefood_list=["白飯","撈麵"]
print("主食選項",staplefood_list)

choose4=input("那今天主食想要吃什麼呢?~")
print()

print(staplefood_list[0],"：香甜可口的一粒粒米絕對是你最好的選擇！")
print(staplefood_list[1],"：我們家的招牌之一呢！還可以把麵DIY做餃子吃喔～")


full_list=["吃得好飽喔～","還沒吃飽"]
print("飽了沒",full_list)

choose5=input("吃了這麼多你吃飽了嗎？！")
print()

print(full_list[0],"吃得好飽喔～快要睡著了請幫我買單吧！")
print(full_list[1],"這些才小case啦我還能吃很多很多挑戰極限喔～")

print("今天的服務還滿意嗎~,很開心認識你喔!期待你的下次光臨")