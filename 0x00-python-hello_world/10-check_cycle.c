#include "lists.h"
/**
 * check_cycle - function that checks if a single list has a cycle.
 * @list: linked list to check.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *p, *c;

	if (!list)
		return (0);

	p = list;
	c = list;
	while (p && c)
	{
		p = p->next;
		c = c->next->next;
		if (c == p || c == list)
			return (1);
	}
	return (0);
}
