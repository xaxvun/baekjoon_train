#include<stdio.h>
int main(){
    int x, y, w, h;
    int min = 1000;
    int cnt = -1;

    scanf("%d %d %d %d", &x, &y, &w, &h);

    if(x<w/2){
        int arr[3];
        arr[0]=x;
        arr[1]=h-y;
        arr[2]=y;
        for(int i=0;i<3;i++){
            if(arr[i]<min){
                min = arr[i];
                cnt=i;
            }
        }
        printf("%d", arr[cnt]);
        
    }else if(x>w/2){
        int arr[3];
        arr[0]=w-x;
        arr[1]=h-y;
        arr[2]=y;
        for(int i=0;i<3;i++){
            if(arr[i]<min){
                min = arr[i];
                cnt=i;
            }
        }
        printf("%d", arr[cnt]);

    }else{
        int arr[4];
        arr[0]=x;
        arr[1]=2*x;
        arr[2]=h-y;
        arr[3]=y;
        for(int i=0;i<4;i++){
            if(arr[i]<min){
                min = arr[i];
                cnt=i;
            }
        }
        printf("%d", arr[cnt]);

    }
    return 0;
}