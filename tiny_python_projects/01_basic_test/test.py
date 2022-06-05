### pytest를 이용한 테스트 코드 ###
# 테스트용 모든 명령을 자동으로 실행해 주며, 몇 개의 테스트를 진행해서 몇 개가 성공했는지 알려준다.
# -v 옵션을 사용하면 상세한 테스트 결과를 보여준다.
# 처음 몇 줄은 테스트 결과이고, 이후 줄들은 테스트 실패 시의 상세 내용을 보여준다.

# -x 옵션을 사용하면 테스트가 실패한 시점에 바로 중단한다.
# -xv 혹은 -vx 처럼 사용할 수 있다.

import os
from subprocess import getstatusoutput, getoutput

prg = './hello.py'

# exists
def test_exists():
    assert os.path.isfile(prg)

# runs using python
def test_runnable():
    out = getoutput(f'python {prg}')
    assert out.strip() == 'Hello, World!'

# says 'Hello, World' by default
def test_executable():
    out = getoutput(f'python {prg}')
    assert out.strip() == 'Hello, World!'

# usage
def test_usage():
    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'python {prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')

# test for input
def test_input():
    for val in ['Beartoad', 'Honeybadger']:
        for option in ['-n', '--name']:
            rv, out = getstatusoutput(f'python {prg} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'
