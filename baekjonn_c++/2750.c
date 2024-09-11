#include<stdio.h>
int main(){
   int n;
   int arr[1000];
   int temp;
   scanf("%d", &n);

   for(int i=0;i<n; i++){
    scanf("%d", &arr[i]);
   }
   //버블정렬 사용함
   for(int j=0;j<n-1; j++){
    for(int i=0;i<n-j-1; i++){
        if(arr[i]>arr[i+1]){
        temp = arr[i];
        arr[i]=arr[i+1];
        arr[i+1]=temp;
        }
    }

    }
    

    for(int k=0; k<n;k++){
        printf("%d\n",arr[k]);
    }
    return 0;

}