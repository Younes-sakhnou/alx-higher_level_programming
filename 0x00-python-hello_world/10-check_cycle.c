#include "lists.h"
/**
 * check_cycle - function that checks if a single list has a cycle.
 * @list: linked list to check.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *p, *t;

	if (!list)
		return (0);

	p = list;
	t = list;
	while (p && t)
	{
		p = p->next;
		t = t->next->next;
		if (t == p || t = list)
			return (1);
	}
	return (0);
}
