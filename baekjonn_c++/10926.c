#include<stdio.h>

int main(){
    char words[50];             // 1. 크기가 50인 char형 배열 선언
    scanf("%s", &words);        // 2. 입력받은 문자열을 words에 저장
    printf("%s?\?!", words);    // 3. 입력받은 words와 "??!"를 붙여서 출력
                                //    (문자열을 출력하므로 서식문자는 %s 사용)
                                //    ("??!"는 삼중자이므로 물음표 사이에 이스케이프문자 삽입)
    return 0;
}