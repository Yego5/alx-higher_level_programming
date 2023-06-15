#include <stdio.h>
#include "lists.h"

size_t print_dlistint(const dlistint_t *hd)
{
    size_t cnt = 0;

    while (hd != NULL)
    {
        printf("%d\n", hd->n);
        hd = hd->next;
        cnt++;
    }

    return cnt;
}
