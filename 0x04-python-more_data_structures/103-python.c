#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - check the code
 * @p: Python Obj
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int s, i, j;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		j = 10;
	else
		j = s + 1;
	printf("  first %ld bytes:", j);
	for (i = 0; i < j; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	printf("\n");
}

/**
 * print_python_list - check the code
 * @p: Python Object
 */
void print_python_list(PyObject *p)
{
	long int s, i;
	PyListObject *list;
	PyObject *object;

	s = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < s; i++)
	{
		object = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(object);
	}
}
