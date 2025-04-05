#include <stdio.h>

int main()
{
    printf("Hello World!\n");

    return 0;
}

'''
main, printf 뒤 괄호가 붙은 단어를 함수(function)이라고 한다.
헬로 월드 끝에 붙은 '\n'은 제어 문자라고 한다. 화면에 직접 표시 되지는 않지만 문자열을 다음 줄에 출력되도록 만들며 엔터 키의 역할과 같다.

소스 코드의 첫째 줄엔 '#include'가 있는데 이것은 헤더 파일을 퐇마하는 문법이며 printf 함수를 사용하려면 stdion.h 헤더 파일이 필요하다.

main 함수는 c언어로 프로그램을 만들었을 때 가장 처음에 실해오디는 특별한 함수이다. 우리는 main함수를 채워 넣으면서 프로그래밍을 하게 된다.
만약 소스에서 main함수가 없으면 컴파일 되지 않는다.

