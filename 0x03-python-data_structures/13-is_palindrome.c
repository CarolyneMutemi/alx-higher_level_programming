#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	listint_t *p = *head;
	int len = 0;
	int index = 0;
	int mid = 0;
	int beg = 0;
	int end = 0;
	int *array = malloc(sizeof(int));
	/*listint_t *pointer = *head;
        listint_t *previous = NULL;
        listint_t *current = NULL;*/
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
	end = len - 1;

	if (len % 2 == 0)
		mid = (len/2) - 1;
	if (len % 2 == 0)
		mid = (len/2);
	while (beg <= mid)
	{
		if (array[beg] != array[end])
			return (0);
		beg++;
		end--;
	}
	return (1);
}
