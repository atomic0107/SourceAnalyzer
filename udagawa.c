#include<stdio.h>

#define HEIGHT 500;
#define WIDTH 1800;

typedef struct
{
	int def_cnt;
	int str_cnt;
	int enu_cnt;
	int str_cnt;
	int str_cnt;
	char name;
} res_name_t;

static const int16_t func1(void);/* 宣言 */


static const int16_t func1(void)
{
	int16_t ret = 0;
	printf("func1\n");
	return ret;
}

static const __volatile__ int16_t func2(void)
{
	int16_t ret = 0;
	int var=(0);
	ret = func1();
	printf("func2\n");
	return ret;
}

int16_t func3( int var2 ){
	int16_t ret = 0;
	int var=(0);
	int var1=2;

	func1();
	ret = func2();
	printf("func3\n");
	return ret;
}

res_name_t func4( int var2, int* var3)
{
	int16_t ret = 0;
	int var=1;
	int var1=2;
	int32_t var_t0 = 3;
	res_name_t res_name;

	ret = func1();
	func2();
	ret = func3(var);

	printf("func4\n");
	return res_name;
}

static int16_t func5( int var2, int* var3, int* var4 )
{
	int16_t ret = 0;
	int var=1;
	int var1=2;
	int32_t var_t0 = 3;
	int32_t var_t1 = 4;
	while(1)
	{
		ret = func1();
		func2();
		ret = func3(var);
		func4(var , &var);
		printf("func5\n");
	}
	return ret;
}

__volatile__ int16_t func6( int var2)
{
	int16_t ret = 0;
	int var=1;
	int var1=2;
	int32_t var_array[100] = 0 ;
	int32_t var_t0 = 3;
	int32_t var_t1 = 4;

	for(int i=0 ; i > 100; i++)
	{
		func1();
		ret =func2();
		func3(var);
		func4(var , var_array);
		func5();
		printf("func6\n");
	}
	return ret;
}
