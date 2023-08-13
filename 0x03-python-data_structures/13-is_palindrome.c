#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	listint_t *p = *head;
	int len = 0;
	int index = 0;
	int *array = malloc(sizeof(int));
	listint_t *pointer = *head;
        listint_t *previous = NULL;
        listint_t *current = NULL;
	if (*head == NULL)
		return (1);

	while (p != NULL)
	{
		array[index] = p->n;
		index++;
		p = p->next;
		len++;
		array = realloc(array, sizeof(int) * len+1);
	}

	while (pointer != NULL)
	{
		current = pointer;
		pointer = pointer->next;
		current->next = previous;
		previous = current;
		*head = current;
	}
	pointer = *head;
	index = 0;

	while (pointer != NULL)
        {
		if (array[index] != pointer->n)
			return (0);
                index++;
                pointer = pointer->next;
        }
	free(array);
	return (1);
}
