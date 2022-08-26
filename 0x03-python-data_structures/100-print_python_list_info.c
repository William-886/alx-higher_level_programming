#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @c: A PyObject list.
 */
void print_python_list_info(PyObject *c)
{
	int size, alloc, a;
	PyObject *obj;

	size = Py_SIZE(c);
	alloc = ((PyListObject *)c)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (a = 0; a < size; a++)
	{
		printf("Element %d: ", a);

		obj = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
