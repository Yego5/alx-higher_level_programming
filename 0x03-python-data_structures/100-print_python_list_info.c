printf("[*] Size of the Python List = %ld\n", new_size);
printf("[*] Allocated = %ld\n", new_allocated);

for (new_e = 0; new_e < new_size; new_e++)
{
	new_itemObj = PyList_GetItem(new_p, new_e);
	new_itemType = Py_TYPE(new_itemObj)->tp_name;
	printf("Element %ld: %s\n", new_e, new_itemType);
}
