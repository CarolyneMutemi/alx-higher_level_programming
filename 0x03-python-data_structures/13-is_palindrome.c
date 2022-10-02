#include "lists.h"

/**
* is_palindrome - function in C that checks if a singly linked list is a
* palindrome.
* @head: head of the list.
* Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/

int is_palindrome(listint_t **head)
{
	listint_t *traverse_list = *head;
	int list_length, split_list, to_compare;
	int save_list_content[4096];

	if (!head)
		return (1);

	while (traverse_list)
	{
		save_list_content[list_length] = traverse_list->n;
		traverse_list = traverse_list->next;
		list_length++;
	}

	list_length--;
	split_list = list_length / 2;

	for (to_compare = 0; to_compare <= split_list; list_length--, to_compare++)
	{
		if (save_list_content[to_compare] != save_list_content[list_length])
			return (0);
	}

	return (1);
}
