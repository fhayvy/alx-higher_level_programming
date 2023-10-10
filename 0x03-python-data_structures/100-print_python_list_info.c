#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>


/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: A pointer to an object
 */
void print_python_list_info(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);

		Py_ssize_t allocated = ((PyListObject *)p)->allocated;

		for(Py_ssize_t i = 0; i < size; i++)
		{
			PyObject *element = PyList_GetItem(p, i)
		}
