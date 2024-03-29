#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**

 * print_python_list_info -  function that outputs some basic

 *  info about Python lists

 * @p: python list

 */

void print_python_list_info(PyObject *p)
{

        int e;


        printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));

        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

        for (e = 0; e < Py_SIZE(p); e++)

                printf("Element %d: %s\n", e, Py_TYPE(PyList_GetItem(p, e))->tp_name);
}
