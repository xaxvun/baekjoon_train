#include<stdio.h>
int main(){
    int n, sum;
    int a, b;

    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d %d", &a, &b);
        sum = a+b;
        printf("%d\n", sum);
    }
    return 0;
}