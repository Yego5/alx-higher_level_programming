#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))


if (*nw_head == NULL || (*nw_head)->next == NULL)
    return (1);

tmp = *nw_head;
while (tmp)
{
    size++;
    tmp = tmp->next;
}

tmp = *nw_head;
for (i = 0; i < (size / 2) - 1; i++)
    tmp = tmp->next;

if ((size % 2) == 0 && tmp->n != tmp->next->n)
    return (0);

tmp = tmp->next->next;
rev = reverse_listint(&tmp);
mid = rev;

tmp = *nw_head;
while (rev)
{
    if (tmp->n != rev->n)
   	 return (0);
    tmp = tmp->next;
    rev = rev->next;
}
reverse_listint(&mid);

return (1);
