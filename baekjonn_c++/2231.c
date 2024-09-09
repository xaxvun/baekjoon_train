#include<stdio.h>
int main(){
    int N,M;
    int a, b, c, d, e, f, g;
    scanf("%d",&N);

    for( M=1; M<N; M++){
        a = M%10;
        b = (M/10)%10;
        c = (M/100)%10;
        d = (M/1000)%10;
        e = (M/10000)%10;
        f = (M/100000)%10;
        g = (M/1000000)%10;

        if(N == M+a+b+c+d+e+f+g){
            printf("%d",M);
            break;
        }
        
    }
    if(N != M+a+b+c+d+e+f ){
        printf("0");
    }
    return 0;


}