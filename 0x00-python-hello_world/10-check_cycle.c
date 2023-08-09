#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: A pointer to the head of the linked list
 * Return: 0 if no cycle is detected, 1 if a cycle is found
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
