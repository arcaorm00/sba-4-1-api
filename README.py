'''
뉴런(n) = bool
퍼셉트론(pn) = 뉴런 + 활성화함수(x)
아달린(adalin) = 뉴런 + 활성화함수(x)

nn = bool + actfn
ann = bool + actfn + cost
dnn = ann + ann + ...

cnn = dnn + convolution => image classification
rnn = dnn + recurrent   => order => context => nlp
lstm = rnn + time       => sequential => prediction

상황에 따른 최적(bast practice)의 선택을 할 수 있어야 한다.

플라스크 개발환경
template을 리턴 => SOUP 방식
JSON을 리턴 => restful 방식 => API 서버

wsgi 방식으로 전환
1. RESTful로 번환
2. setup.py 생성, setuptools를 활용한 설정
3. root-folder를 생성
    - package: __init__.py 존재
    - directory: __init__.py 비존재


시퀀스 데이터는 정의 자체가 순서를 고려한 데이터이다.
(앞선 결과가 향후 결과에 영향을 준다.) => 조건부 확률 (베이지안)
=> 시리얼 데이터 => 타임라인

MLP와 CNN과 같은 기본적 신경망 모델은 입력 샘플의 순서를 다루지 못 한다.
이전에 본 샘플을 기억하지 못 함.
반면 RNN은 시퀀스 모델링을 위해 고안되었다. 
지난 정보를 기억하고 이를 기반으로 새로운 이벤트를 처리한다.

시퀀스 모델링의 종류
다대일 / 일대다 / 다대다
'''