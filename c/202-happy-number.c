// 0ms, 100.00%

#include <stdio.h>
#include <math.h>


bool isHappy(int n){
    int total = 0;
    while (n != 0) {
        total += pow((double)(n % 10), (double) 2);
        n = n / 10;
    }
    if (total == 1) {
        return true;
    } else if (total == 4) {
        return false;
    } else {
        return isHappy(total);
    }
}