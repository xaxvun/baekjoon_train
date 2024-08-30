// #include<stdio.h>

// int main(){
//     int a, b;
//     scanf("%d %d", &a, &b);
//     while(a != 0 && b != 0){
//         if(a<b){
//             if(b%a==0){
//                 printf("factor\n");
//             }
//             else{
//             printf("neither\n");
//             }
//         } else {
//             if (a % b == 0) {
//                 printf("multiple\n");
//             } else {
//                 printf("neither\n");
//             }
//         }
//         scanf("%d %d", &a, &b);
//     }

//     return 0;
// }

#include<stdio.h>

int main(){
    int a[1000], b[1000];
    int count=0;

    while(1){
        scanf("%d %d", &a[count], &b[count]);
        if (a[count] == 0 && b[count]==0){
            break;
        }
        count ++;
    }

    for (int i = 0; i<count; i++){
        if(a[i]<b[i]){
            if(b[i] % a[i] == 0){
                printf("factor\n");
            }else{
                printf("neither\n");
            }
        }else{
            if(a[i]%b[i]==0){
                printf("multiple\n");
            }else{
                printf("neither\n");
            }
        }
    }
    return 0;

}