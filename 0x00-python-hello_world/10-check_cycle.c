#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - function in C that checks if a singly linked list has a cycle in it
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *current = list, *check = list;

while (check && check->next)
{
current = current->next;
check = check->next->next;
if (current == check)
return (1);
}
return (0);
}
