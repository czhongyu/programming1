#include <stdio.h>
#include <cs50.h>

bool check_sum(long long int credit)
{
    long long int i, mod, c, sum = 0;

    for(i = 0, mod = 10; i < 8; i++, mod = mod * 100)
    {
        c = (credit / mod) % 10 * 2;
        c = c / 10 + c % 10;
        sum += c;
    }

    for(i = 0, mod = 1; i < 8; i++, mod = mod * 100)
    {
        c = (credit / mod) % 10;
        sum += c;
    }

    if(sum % 10)
        return false;
    else
        return true;
}

bool is_visa(long long int credit)
{
    long long int c13, c16;

    c13 = credit / 1000000000000;
    c16 = credit / 1000000000000000;
    if(c13 == 4)
        return true;
    else
        if(c16 == 4)
            return true;
        else
            return false;
}

bool is_amex(long long int credit)
{
    long long int c = credit / 10000000000000;

    if(c == 34 || c == 37)
        return true;
    else
        return false;
}

bool is_mastercard(long long int credit)
{
    long long int c = credit / 100000000000000;

    if(c >= 51 && c <= 55)
        return true;
    else
        return false;
}

int main()
{
    long long int credit;

    //get credit card number
    do
    {
        credit = get_long_long("Number: ");
    } while(credit <= 0);

    //print result
    if(check_sum(credit))//valid?
        if(is_visa(credit))
            printf("VISA\n");
        else
            if(is_amex(credit))
                printf("AMEX\n");
            else
                if(is_mastercard(credit))
                    printf("MASTERCARD\n");
                else
                    printf("INVALID\n");
    else
        printf("INVALID\n");

    return 0;
}