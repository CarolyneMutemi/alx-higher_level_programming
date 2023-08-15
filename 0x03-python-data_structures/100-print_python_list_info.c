#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: Python Object List.
 * Return: Null
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t index = 0;
	PyObject *item;
	Py_ssize_t len = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)(p))->allocated);

	while (index < len)
	{
		item = PyList_GetItem(p, index);
		printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
		index++;
	}
}

