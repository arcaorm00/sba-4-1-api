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
'''