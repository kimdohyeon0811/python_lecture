#Q2.랜덤함수를 이용하여 코딩스터디모임 날짜를 출력하시오.
#조건 4~28사이 랜덤한 숫자를 출력하시오
#randiant(a,b):a이상 b이하의 임의의 정수반환 
#randrage(b): 0부터 b까지 임의의 정수반환

import random
random_num = random.randint(4,28)
print(f'매달 {random_num}일이 선정되었습니다')