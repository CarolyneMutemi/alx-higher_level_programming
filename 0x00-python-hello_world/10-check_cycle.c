#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head pointer to the list.
 * Return: 0 if there's no cycle, 1 if there is.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL && fast != NULL)
	{
		slow = slow->next;
		if (fast->next != NULL)
			fast = fast->next->next;
		if (slow == fast)
		{
			return (1);
		}
	}

	return (0);
}

