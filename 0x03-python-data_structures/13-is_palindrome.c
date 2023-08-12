#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * *is_pal - function to recursively check values of head and tail in a linked list
 * @head: double pointer of listint_t type to head of linked list
 * @tail: single pointer of listint_t type to tail of linked list
 * Return: 1 if palidrome or 0 if not
 */
int is_pal(listint_t **head, listint_t *tail)
{
	/* check if tail of list is NULL*/
	if (tail == NULL)
		return (1);
	/*Call function to recursively check head and tail of list */
	if (is_pal(head, tail->next) && (*head)->n == tail->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - function to check if singly linked list is a palidrome
 * @head: double pointer of listint_t type to head of list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	/*check if head and next is NULL, null means Palindrome */
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	return(is_pal(head, *head));
}
	/**{
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
	while (indx < ((counter >> 1)))
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
*/

