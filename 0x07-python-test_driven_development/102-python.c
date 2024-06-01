#include <Python.h>
#include <stdio.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    Py_UCS4 *unicode = PyUnicode_AsUCS4Copy(p);

    if (unicode == NULL) {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    printf("[.] string object info\n");
    printf("  type: compact unicode object\n");
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", unicode);

    PyMem_Free(unicode);
}

