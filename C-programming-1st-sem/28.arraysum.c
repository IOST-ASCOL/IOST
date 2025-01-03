/* Write a program that defines a function that takes an array of integers as a parameter.
The function should print the sum of the elements in the array to the console.
Call the function with an array of your choice*/
#include <stdio.h>

int sumByValue(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(arr[0]);
    int sum =sumByValue(arr, size);// Passing the array by value
    printf("Sum is %d",sum);
    printf("--Your Name--")
    return 0;
}
