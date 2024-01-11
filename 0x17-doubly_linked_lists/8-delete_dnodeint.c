#include "lists.h"

/**
 * delete_dnodeint_at_index - deletes the node at index of a
 * dlistint_t linked list
 *
 * @head: head of the list
 * @index: index of the new node
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *g1;
	dlistint_t *g2;
	unsigned int j;

	g1 = *head;

	if (g1 != NULL)
		while (g1->prev != NULL)
			g1 = h1->prev;

	j = 0;

	while (g1 != NULL)
	{
		if (j == index)
		{
			if (j == 0)
			{
				*head = g1->next;
				if (*head != NULL)
					(*head)->prev = NULL;
			}
			else
			{
				g2->next = g1->next;

				if (g1->next != NULL)
					g1->next->prev = g2;
			}

			free(g1);
			return (1);
		}
		g2 = g1;
		g1 = g1->next;
		j++;
	}

	return (-1);
}
