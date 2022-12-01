#include <stdio.h>
#include <string.h>
typedef struct
{
    char name[4];
    int moves;
    int visited;
} Command;

int main()
{
    FILE *fin = fopen("day08.txt", "r");
    int i = 0, index = 0, accumulator = 0, t;
    Command com[611];

    while (!feof(fin))
    {
        fscanf(fin, "%s %d", &com[i].name, &com[i].moves);
        com[i].visited = 0;
        i++;
    }

    //task 1
    while (!com[index].visited)
    {
        com[index].visited++;
        if (!strcmp(com[index].name, "nop"))
        {
            index++;
        }
        else if (!strcmp(com[index].name, "acc"))
        {
            accumulator += com[index].moves;
            index++;
        }
        else if (!strcmp(com[index].name, "jmp"))
        {
            index += com[index].moves;
        }
    }
    printf("Task1: %d \n", accumulator);

    // task 2
    for (i = 0; i <= 610; i++)
    {
        if (!strcmp(com[i].name, "nop"))
            strcpy(com[i].name, "jmp");
        else if (!strcmp(com[i].name, "jmp"))
            strcpy(com[i].name, "nop");
        t = 0;
        index = 0;
        accumulator = 0;
        while ((index != 610) && (t < 2020))
        {
            t++;
            if (!strcmp(com[index].name, "nop"))
            {
                index++;
            }
            else if (!strcmp(com[index].name, "acc"))
            {
                accumulator += com[index].moves;
                index++;
            }
            else if (!strcmp(com[index].name, "jmp"))
            {
                index += com[index].moves;
            }
            if (index == 610)
            {
                if (!strcmp(com[index].name, "acc"))
                    printf("Task2: %d \n", accumulator + com[index].moves);
                else
                    printf("Task2: %d \n", accumulator);
            }
        }
        if (!strcmp(com[i].name, "nop"))
            strcpy(com[i].name, "jmp");
        else if (!strcmp(com[i].name, "jmp"))
            strcpy(com[i].name, "nop");
    }
}