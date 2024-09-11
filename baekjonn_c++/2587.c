#include<stdio.h>
int main(){
    int arr[5]={0,};
    int sum=0,temp=0;
    for(int i=0;i<5;i++){
        scanf("%d",&arr[i]);
        sum += arr[i];
    }
    printf("%d\n",sum/5);
    
    for(int i =0; i<4; i++){
        for (int j=0; j<4-i; j++){
            if(arr[j]>arr[j+1]){
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    printf("%d",arr[2]);
}