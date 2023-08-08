#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the singly linked list
 * Return: 1 if it is a palindrome, or 0 if it is not.
 */

int is_palindrome(listint_t **head)
{
	int indx = 0, counter = 0, num, digit;
	listint_t *tmp = *head, *nodecheck = *head;

	if (head == NULL || *head == NULL)
		return (1);

	while (nodecheck != NULL)
	{
		nodecheck = nodecheck->next;
		counter++;
	}

	digit = counter;
	while (indx < counter / 2)
	{
		nodecheck = *head;
		num = 1;
		while (num < digit)
		{
			nodecheck = nodecheck->next;
			num++;
		}

		if (nodecheck->n != tmp->n)
			return (0);

		tmp = tmp->next;
		digit--;
		indx++;
	}

	return (1);
}
