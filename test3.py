room_numbers = { "['Freddie', 'Jen']": 403, "['Ned', 'Keith']": 391, "['Kristin', 'Jazzmyne']": 411, "['Eugene', 'Zach']": 395 }
ans_to_question_1 = "The absence of quotation on each key makes the code wrong"

ans_to_question_2 = "The first key is: ['Freddie', 'Jen'] "

jp_population_rank = {'3': 'osaka', '1': 'tokyo', '2': 'kanagawa'}
print(jp_population_rank.keys())
ans_to_question_3 = "dict_keys(['3', '1', '2'])"

ans_to_question_4 = "ans below"
details = ("Abdullahi", "bawo road", "Tarauni LGA", "Kano State")
(name, street, local_government, state ) = details
print("My name is", name , "living at",local_government, state )
output = "My name is Abdullahi living at Tarauni LGA Kano State"

ans_to_question_5 = "ans below"
names = ["Garcia", "O'Kelly", "Davis"]
(name1,name2,name3) =names
print(name1, "-", name2, "-", name3)
output = "Garcia - O'Kelly - Davis"

ans_to_question_6 = "ans below"
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003', 'March 29, 2006', 'August 1, 2008',
                 'July 22, 2009', 'July 11, 2010', 'November 13, 2012', 'March 20, 2015', 'March 9, 2016']
print(eclipse_dates[7:10])
output = "['November 13, 2012', 'March 20, 2015', 'March 9, 2016']"

ans_to_question_7 = "ans below"
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
print(months[6:9])
output = "['July', 'August', 'September']"

ans_to_question_8 = "ans below"
def days(days):
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
print(days(5))
output = "0 week(s) and 5 day(s)"

ans_to_question_9 = "ans below"
def to_cal_vol_of_cylinder(r,h):
    pi = 3.14
    volume = 2 * pi * r * h
    return volume
print(to_cal_vol_of_cylinder(6,8))
output = 301.44