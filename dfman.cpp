#include <stdlib.h>
#include <iostream>
using namespace std;
int main()
{
	//string fname = argv[1];

	//MODIFY THIS SO THAT THE PATH IS THE PATH FOR YOUR DFMAN.PY FILE
	string string_cmd = "python \"C:\\Users\\jjara\\OneDrive\\Desktop\\Programming\\dfman\\dfman.py\"";
	/////////
	
	const char *cmd = string_cmd.c_str();
	system(cmd);
	return 0;
}
