#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @py_lst: A PyObject list.
 */
void print_python_list_info(PyObject *py_lst)
{
    int lst_size, lst_alloc, i;
    PyObject *lst_item;

    lst_size = Py_SIZE(py_lst);
    lst_alloc = ((PyListObject *)py_lst)->allocated;

    printf("[*] Size of the Python List = %d\n", lst_size);
    printf("[*] Allocated = %d\n", lst_alloc);

    for (i = 0; i < lst_size; i++)
    {
        printf("Element %d: ", i);

        lst_item = PyList_GetItem(py_lst, i);
        printf("%s\n", Py_TYPE(lst_item)->tp_name);
    }
}
