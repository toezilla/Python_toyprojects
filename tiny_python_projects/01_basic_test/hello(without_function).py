# 프로그램에 인수를 전달(parse)하기 위한 모듈
import argparse

if __name__ == "__main__":
    # test_executable 오류 해결 위해 shebang 추가
    # shebang은 이 코드를 실행할 때 어떤 프로그램을 사용할지 OS에게 알려줌
    # !/usr/bin/env python

    # 프로그램의 용도를 문서화하는 주석
    # Purpose: Say hello

    # 이 parser가 모든 내용을 인지한다. description 안에 있는 내용이 도움말로 표시된다.
    parser = argparse.ArgumentParser(description='Say hello')
    # 1) 인사 대상이 될 사람의 이름을 인수로 전달한다고 parser에게 알려 준다
    # 2) 만약, 인수명을 --name으로 변경하면 인수를 선택적으로 사용하게 만들 수 있다
    # 이전 프로그램이랑 다른 점은 -n과 -name을 각각 축약형(short)와 일반형(long)인수명으로 추가한 것이다.
    # 또한, 기본값을 명시했으며 metaver에 인수로 사용할 변수를 표시하고 있다.
    # parser.add_argument('name', help='Name to greet') # 1)
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')

    # 인수를 프로그램에게 전달하라고 parser에게 지시한다.
    args = parser.parse_args()
    # args.name 값을 사용해서 인사 메시지를 출력한다.
    # print('Hello, World!')
    print('Hello, '+ args.name + '!')

