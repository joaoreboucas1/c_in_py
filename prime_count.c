#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_prime(int n)
{
    for (int i = 2; i < (int) sqrtf((float) n) + 1; i++) {
        if (n%i == 0) return false;
    }
    return true;
}

int prime_count(float x)
{
    int count = 0;
    for (int i = 2; i < (int) x; i++) {
        if (is_prime(i)) count += 1;
    }
    return count;
}

int main()
{
    int n = 1000000;
    printf("Prime count of %d: %d\n", n, prime_count(n));
    return 0;    
}