#include <stdio.h>
int main(void) {
    int T, C;
    int Q, D, N, P;

    scanf("%d", &T);

    for (int i = 0; i < T; i++){
        scanf("%d", &C);
        if (C >= 1 && C <= 500){
            Q = C/25;
            D = C%25/10;
            N = C%25%10/5;
            P = C%25%10%5/1;
            printf("%d %d %d %d", Q, D, N, P);
            printf("\n");
        }
        else{
            break;
        }
    }

    return 0;
}