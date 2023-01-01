

def get_average(marks):
    total =0
    for subject in marks:


        total += marks[subject]



    l_average = total / len(marks)
    return l_average

marks = {  '국어': 90, "영어": 80,"수학": 80}
average = get_average(marks)
print('평균은 {}점입니다. '.format(average))