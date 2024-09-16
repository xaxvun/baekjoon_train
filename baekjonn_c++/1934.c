#include<stdio.h>
/*최대 공약수*/
int Max(int a, int b){
    int result1 = 0;
    int min = (a<b)?a:b;

    for (int c = 1; c<= min; c++){
        if((a%c == 0)&&(b%c==0)){
            result1 = c;
            if(result1 < c){
                result1 = c;
            }
        }
    }
    return result1;
}
/*최소 공배수*/
int Min(int a, int b){
    return a*b/Max(a,b);
}
int main(void){
    int num, a, b;
    scanf("%d", &num);

    for (int i = 0; i<num; i++){
        scanf("%d %d", &a, &b);
        printf("%d\n", Min(a,b));
    }
}