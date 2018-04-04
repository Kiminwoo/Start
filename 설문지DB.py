
import pymysql 

print("Test Start!!")

AGE = input("나이를 입력해 주세요  :") 

gender = input("성별을 입력해 주세요 :\n1번:남자 \n2번:여자 \n")

department = input("학과를 입력해 주세요 : \n1번:성서학과 \n2번:간호학과 \n3번:컴퓨터소프트웨어학과  \n4번:영유아보육학과 \n5번:사회복지학과 \n6번:(그 외의 과이시면 과를 입력해주세요 )\n")

WakeUp = input("오늘 기상 시간을 입력해 주세요  :  \n1번 : 06시 이전 \n2번 : 06시 ~ 06시 30분 \n3번 : 06시 30분 ~ 07시 \n4번 : 07시 ~ 07시 30분 \n5번 : 07시 30분 ~ 08시 \n6번 : 08시 ~ 08시30분 \n7번 : 08시 30분 ~ 09시 \n8번 : 09시 ~ 09시30분 \n9번 : 09시 30분 ~ 10시 \n10번 : 10시 이후\n" )

Sleep = input("오늘 숙면 시간을 입력해주세요 : \n1번 : 04시간 미만 \n2번 : 4시간 ~ 5시간\n3번 : 5시간 ~ 6시간 \n4번 : 6시간 ~ 7시간 \n5번 : 7시간 ~ 8시간 \n6번 : 8시간 ~ 9시간 \n7번 : 9시간 이상\n")

breakfirst = input("오늘 아침밥 먹었나요 ?? \n1번:예 \n2번:아니요 \n" )

Feel = input("지금 기분 어떄요 ?? \n1번:좋다\n2번:싫다\n3번:그저 그렇다 \n")

Shouwer = input("어제 자기전에 샤워 했어요 ?? 꿀짬 ??\n1번:예 \n2번:아니요 \n")

Satisfaction = input("지금의 만족도를 1~100으로 표현하면??\n(숫자를 입력해 주세요 )\n")

HomeWork = input ("오늘 과제가 생겼나요 ??\n1번:네\n2번:아니요 \n")

Moring = input("오늘 아침에 수업이 있나요 ??\n1번:1교시\n2번:2교시 \n3번:1교시+2교시(연강)\n4번:없었다 \n")

Working = input("현재 알바를 하고 있나요 ??\n1번:네 \n2번:아니요 \n")

Abundance = input("지금 돈이 풍족하신가요 ??\n1번:네 \n2번:가난해요\n3번:버틸만 하다  \n")

Couple = input("연애를 하고 있나요  ??\n1번:네\n2번:아니요 \n")

Exercise = input("오늘 운동은 하셨나요 ??\n1번:네 \n2번:아니요 \n")

Strees = input("평소에 스트레스를 어떻게 푸시나요 ??\n1번:운동 \n2번:밥먹기 \n3번:친구 만나기 \n4번:노래 \n5번:쇼핑\n6번:혼자 있기 \n7번:없다  \n")

Friendship = input ( "현재 친구 관계는 만족스러운가요 ??\n1번:네 \n2번:아니요 \n")

school = input ("통학은 뭘로 하시나요 ?? \n1번:버스\n2번:지하철\n3번:버스+지하철 \n4번:걸어서\n5번:자가용 \n")

schoolTime = input("통학하는데 시간이 얼마나 걸리나요 ?? \n1번:30분 미만 \n2번:30분 ~ 1시간 \n3번:1시간~ 1시간30분\n4번:1시간30분~2시간\n5번:2시간이상\n")
 


connection = pymysql.connect(host ="localhost", user = "root", passwd="rladlsdn", db = "sch")

cursor=connection.cursor()  

sql=("INSERT INTO `search` (`AGE`, `gender`, `department`,`WakeUp`,`Sleep`,`breakfirst`,`Feel`,`Shouwer`,`Satisfaction`,`HomeWork`,`Moring`,`Working`,`Abundance`,`Couple`,`Exercise`,`Strees`,`Friendship`,`school`,`schoolTime`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s' )" )%(AGE,gender,department,WakeUp,Sleep,breakfirst,Feel,Shouwer,Satisfaction,HomeWork,Moring,Working,Abundance,Couple,Exercise,Strees,Friendship,school,schoolTime)

cursor.execute(sql.encode('utf8')) 

connection.commit() 

data=cursor.fetchall()  

print(data)

