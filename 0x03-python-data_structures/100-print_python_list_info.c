#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -  function that outputs basic information about Python lists
 * @p: python list
 */

void print_python_list_info(PyObject *p)

{
	int value;
	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (value = 0; elem < Py_SIZE(p); value++)
		printf("Value %d: %s\n", value, Py_TYPE(PyList_GetItem(p, value))->tp_name);

}
