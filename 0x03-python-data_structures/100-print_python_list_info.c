#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: Python Object list.
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
    int len, index;
    PyObject *item;

    len = Py_SIZE(p);

    printf("[*] Size of the Python List = %d\n", len);
    printf("[*] Allocated = %d\n", ((PyListObject *)(p))->allocated);

    for (index = 0; index < len; index++)
    {
        item = PyList_GetItem(p, index);
        printf("Element %d: %s\n", index, Py_TYPE(item)->tp_name);
    }
}
