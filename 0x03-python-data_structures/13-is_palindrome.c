#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome - Check for a palindrome
  * @head: The 1st head 
  * Return: 0 for fail, 1 for success
  */
int is_palindrome(listint_t **head)
{
    listint_t *first = NULL, *last = NULL;
    unsigned int i = 0, len = 0, cycle = 0, _list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    first = *head;
    len = listint_len(first);
    cycle = len * 2;
    _list = cycle - 2;
    last = *head;

    for (; i < cycle; i = i + 2)
    {
        if (first[i].n != last[_list].n)
            return (0);

        _list = _list - 2;
    }

    return (1);
}

/**
  * get_nodeint_at_index - Gets a node
  * @head:  head of the list
  * @index: index 
  * Return: The node
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *now = head;
	unsigned int _iter = 0;

	if (head)
	{
		while (now != NULL)
		{
			if (_iter == index)
				return (now);

			now = now->next;
			++_iter;
		}
	}

	return (NULL);
}

/**
  * slistint_len - to count the number of elements
  * @h: linked list
  * Return: integer
  */
size_t listint_len(const listint_t *h)
{
	int i = 0;

	while (h != NULL)
	{
		++i;
		h = h->next;
	}

	return (i);
}
