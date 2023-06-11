#include <Python.h>

/**
 * print_python_list_info - datas about Python lists.
 * @p: A PyObject 
 */
void print_python_list_info(PyObject *p)
{
	pyobject *o;
	int num, memory, counter;

	num = Py_SIZE(p);
	memory = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", num);
	printf("[*] Allocated = %d\n", memory);

	for (counter = 0; counter < num; counter++)
	{
		printf("Element %d: ", counter);
		o = PyList_GetItem(p, counter);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
