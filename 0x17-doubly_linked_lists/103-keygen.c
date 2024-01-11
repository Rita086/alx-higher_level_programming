#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * main - generate a key depending on a username for crackme5
 * @argc: number of arguments passed
 * @argv: arguments passed to main
 *
 * Return: 0 on success, 1 on error
 */
int main(int argc, char *argv[])
{
	unsigned int g, h;
	size_t len, add;
	char *l = "A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk";
	char p[7] = "      ";

	if (argc != 2)
	{
		printf("Correct usage: ./keygen5 username\n");
		return (1);
	}
	len = strlen(argv[1]);
	p[0] = l[(len ^ 59) & 63];
	for (g = 0, add = 0; g < len; g++)
		add += argv[1][g];
	p[1] = l[(add ^ 79) & 63];
	for (g = 0, h = 1; g < len; g++)
		h *= argv[1][g];
	p[2] = l[(h ^ 85) & 63];
	for (h = argv[1][0], g = 0; g < len; g++)
		if ((char)h <= argv[1][g])
			h = argv[1][g];
	srand(h ^ 14);
	p[3] = l[rand() & 63];
	for (h = 0, g = 0; g < len; g++)
		h += argv[1][g] * argv[1][g];
	p[4] = l[(h ^ 239) & 63];
	for (h = 0, g = 0; (char)g < argv[1][0]; g++)
		h = rand();
	p[5] = l[(h ^ 229) & 63];
	printf("%s\n", p);
	return (0);
}
