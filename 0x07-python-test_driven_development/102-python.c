/*
 * File: 102-python.c
 */

#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @string_object: A PyObject string object.
 */
void print_python_string(PyObject *string_object)
{
    long int string_length;

    fflush(stdout);

    printf("[.] string object info\n");
    if (strcmp(string_object->ob_type->tp_name, "str") != 0)
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    string_length = ((PyASCIIObject *)(string_object))->length;

    if (PyUnicode_IS_COMPACT_ASCII(string_object))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");
    printf("  length: %ld\n", string_length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(string_object, &string_length));
}
