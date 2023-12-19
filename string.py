#Q3.문자열처리함수,탈출문자를 이용하여 사이트 비번만들기 프로그램을 만드시오
#조건 예)https://naver.com
#규칙1. https://부분은 제외 -> naver.com
#규칙2. .이후 부분 제외 -> naver
#규칙3. 남은 글자중 처음세자리+글자개수+글자내'e'개수+!를 출력
print("주소를 입력하시오: ")
address = input()
address = address.replace('https://','')
address = address.replace('.','')
fir = address[:3]
sec = len(address)
thi = address.count('e')
print(f'{fir}{sec}{thi}!')