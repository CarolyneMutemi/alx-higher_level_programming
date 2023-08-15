#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: Python Object list.
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
    int len, allocated, i;
    PyObject *item;

    len = Py_SIZE(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", len);
    printf("[*] Allocated = %d\n", allocated);

    for (i = 0; i < len; i++)
    {
        printf("Element %d: ", i);

        item = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(item)->tp_name);
    }
}
