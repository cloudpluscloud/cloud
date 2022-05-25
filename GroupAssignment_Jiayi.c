#include <stdio.h>
#include <stdlib.h>
#include <time.h> 

int main(int argc, char **argv){
    //Step 1: download file
    //Step 2: compile by running following commands on terminal:
    //gcc GroupAssignment_Jiayi.c -o GroupAssignment
    //./GroupAssignment
    //Note: once you compile with gcc, you can call ./GroupAssignment many times
    srand(time(NULL));
    char *a[5] = {"Jiayi", "Muaz", "Genevieve", "Emily", "Marisol"};
    char *b[5];
    int index = 0;
    int random1 = rand() % 4;
    int random2 = rand() % 4;

    while (random2 == random1){
        random2 = rand() % 4;
    }

    for (int i = 0; i<5; i++){
        if(i != random1 && i!= random2){
            b[index] = a[i];
            index++;
        }
    }

    printf("\n");
    printf("Here are your groups for the week. Bona fortuna!\n");
    printf("Group 1: ");
    printf("%s, %s\n", a[random1], a[random2]);
    printf("Group 2: ");
    printf("%s, %s, %s\n", b[0], b[1], b[2]);
    printf("Re-run program if you don't like the assignment.\n");
    printf("\n");
    
    return (EXIT_SUCCESS);       
}