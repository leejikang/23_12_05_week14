#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201848 이름 : 이지강

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
    # 1 ≤ my_string 의 길이 ≤ 100, 1 ≤ target 의 길이 ≤ 100
    if not(1 <= len(my_string) <= 100) or not(1 <= len(target) <= 100):
        raise ValueError("입력 길이는 1 이상 100 이하이어야 합니다.") #raise를 통해 예외처리
    # 문자열 my_string에서 target이 부분 문자열인지 확인, target이 문자열 my_string의 부분 문자열이라면 1을,아니라면 0을 return  
    if target in my_string:
        return 1
    else:
        return 0
# 사용자로부터 문자열 입력 받기
my_string = input("문자열을 입력하세요: ")
target = input("탐색할 부분 문자열을 입력하세요: ")
#입력값을 함수를 통해 result값 받아 출력
result = solution(my_string, target)
print(result)

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    #letter의 입력길이 제한
    if not(1<=len(letter)<=1000):
      raise ValueError("입력 길이는 1 이상 1000 이하이어야 합니다.")
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z','----':' '}
    #letter의 모스부호를 공백으로 나눈 부분
    morse_words = letter.split(' ')
    #모스 부호를 해독하여 영어 문자열로 변환하는 부분
    answer = ''.join([morse[word] for word in morse_words])
    
    return answer

#테스트
morse_code = ".-.. . --. . -. -.. ... ---- -. . ...- . .-. ---- -.. .. ."
result = solution(morse_code)
print(result)


# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    if not (1<= age <=1000):
      raise ValueError("age는 자연수이고 1000 이하이어야 합니다.")
    # 알파벳과 해당 숫자 매핑
    alphabet_to_number = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
    
    # 역매핑 생성
    number_to_alphabet = {str(value): key for key, value in alphabet_to_number.items()}

    # 나이를 문자열로 변환하여 한 글자씩 처리
    age_str = str(age)
    answer = 'PROGRAMMER-857'
    for char in age_str:
        # 알파벳인 경우 변환하여 answer에 추가
        if char.isalpha():
            answer += str(alphabet_to_number[char])
        # 숫자인 경우 해당 알파벳을 역매핑하여 answer에 추가
        else:
            answer += number_to_alphabet[char]

    return answer

# 테스트 예제
age_example = 42
result = solution(age_example)
print(result)

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항     
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1,r2):
    #각 정수 좌표의 개수 초기화
    count1 = 0
    count2 = 0
    r1=int(r1)
    r2=int(r2)
    #작은 원 반지름에 큰 원 반지름보다 큰 값이 입력되었을 때 출력
    if(r1>r2):
      return "잘못된 입력입니다(작은 원>큰 원)"
    #작은 원 안에 들어가는 정수 좌표의 개수(원의 경계 제외)
    for x in range(-r1, r1 + 1):
        for y in range(-r1, r1 + 1):
            if x**2 + y**2 < r1**2:
                count1 += 1
    #큰 원 안에 들어가는 정수 좌표의 개수(원의 경계 포함)
    for x in range(-r2, r2 + 1):
        for y in range(-r2, r2 + 1):
            if x**2 + y**2 <= r2**2:
                count2 += 1
    #큰 원과 작은 원 사이 공간의 정수 좌표 계산
    answer = count2-count1
    return answer
#사용자로부터 각 원의 반지름 값을 받음
r1 = input("작은 원의 반지름을 입력하시요: ")
r2 = input("큰 원의 반지름을 입력하시요: ")
result = solution(r1,r2)
print(result)

# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    # 숫자를 문자열로 변환하여 정렬
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)  # x*3을 기준으로 정렬
    
    # 정렬된 숫자들을 이어붙여 가장 큰 수 생성
    answer = ''.join(numbers)
    
    # 예외 처리: 모든 숫자가 0인 경우
    if answer[0] == '0':
        return '0'
    
    return answer
# 문제
numbers_example = [8, 30, 17, 2, 23]
result = solution(numbers_example)
print(result)