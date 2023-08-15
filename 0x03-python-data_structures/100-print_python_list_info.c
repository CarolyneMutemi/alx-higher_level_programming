#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: Python Object List.
 * Return: Nothing.
 */

void print_python_list_info(PyObject *p)
{
	int index = 0;
	PyObject *item;
	int len = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", ((PyListObject *)(p))->allocated);

	while (index < len)
	{
		item = PyList_GetItem(p, index);
		printf("Element %d: %s\n", index, Py_TYPE(item)->tp_name);
		index++;
	}
}

