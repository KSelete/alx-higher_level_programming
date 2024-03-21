#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *element;

    size = PyList_Size(p);
    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);
    for (i = 0; i < size; ++i) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        }
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    unsigned char *str;

    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = (unsigned char *)PyBytes_AsString(p);

    printf("[.] bytes object info\n  size: %ld\n  trying string: %s\n", size, str);

    printf("  first %ld bytes:", (size < 10 ? size : 10));
    for (i = 0; i < (size < 10 ? size : 10); ++i) {
        printf(" %.2x", str[i]);
    }
    printf("\n");
}
