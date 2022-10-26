#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int rotation(int);
int k;

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    k = atoi(argv[1]);
    int add = rotation(k);
    printf("%i\n", add);

    string pass = get_string("plaintext:  ");

    for(int j = 0; j < strlen(pass); j++)
    {
        if (isupper(pass[j]))
        {
            pass[j] = ((int)pass[j] - 65 + add) % 26 + 65;
        }
        else if (islower(pass[j]))
        {
            pass[j] = ((int)pass[j] - 97 + add) % 26 + 97;
        }
    }

    printf("ciphertext: %s\n", pass);

}

int rotation(int a)
{
    while (a > 26)
    {
        a = a % 26;
    }
    return a;
}

