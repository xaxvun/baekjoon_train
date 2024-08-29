//2566
#include<stdio.h>


int main() {
    int arr[100][100];
    int i, j;
    
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            scanf("%d", &arr[i][j]);
        }
    }

    int max = -1;
    int x = 0, y = 0;  

    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            if (max < arr[i][j]) {
                max = arr[i][j];
                x = i;
                y = j;
            }
        }
    }

 
    printf("%d\n", max);
    printf("%d %d\n", x + 1, y + 1);  
    return 0;
}