#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: A pointer pointing to the head pointer
 * @number: The data of the new node
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *current = NULL, *temp = NULL;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head)
	{
		current = *head;
		if (number <= current->n)
		{
			new_node->next = current;
			*head = new_node;
		}
		else
		{
			while (current->next)
			{
				if (number <= current->next->n)
				{
					temp = current->next;
					current->next = new_node;
					new_node->next = temp;
					return (*head);
				}
				current = current->next;
			}
			temp = current->next;
			current->next = new_node;
			new_node->next = temp;
		}
		return (*head);
	}
	new_node->next = NULL;
	*head = new_node;
	return (*head);
}
