/*
 * File: 13-is_palindrome.c
 * Auth: Mbah Nkemdinma
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of a list to reverse.
 *
 * Return: A pointer to a head of a reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *next_nd, *prev = NULL;

	while (current)
	{
		next_nd = current->next;
		current->next = prev;
		prev = current;
		current = next_nd;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if singly linked list is the palindrome.
 * @head: A pointer to the head of linked list.
 *
 * Return: If the linked list is not palindrome - 0.
 *         If the linked list is palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}

