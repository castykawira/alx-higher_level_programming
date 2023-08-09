#include "lists.h"

/**
 * insert_node - Inserts a new node with the given number 
 * into a sorted linked list.
 * @head: Pointer to the pointer to the head node of the list.
 * @number: The value to be inserted into the list.
 * Return: NULL on failure and pointer to the new node if otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
