#include <stdio.h>
//procedure grouping the description of the problem
void challenge1_inherances(){
    /*Reto 1.
Descripción del problema: 
Herencias. En una tribu ganadera se ha establecido que cuando los padres tengan 3 hijos, 
el ganado heredado por cada hijo se determinará de la siguiente manera. 
- El hijo mayor recibe el triple que el hijo menor.
- El hijo del medio recibe el doble que el hijo menor.
- El hijo menor recibe una cantidad X.
Usted ha sido escogido para crear una solución a través de software. 
Construya un algoritmo, el cual dado un valor numérico (entero) que corresponde a la 
cantidad total de ganado que heredaran los tres hijos, arroje un resultado de la siguiente 
forma:
Total: [Total ganado ingresado]
Hijo mayor: [Número de ganado correspondiente] 
Hijo del medio: [Número de ganado correspondiente]
Hijo menor: [Número de ganado correspondiente] 

Pruebas y consideraciones:
- El algoritmo debe estar contenido en una función la cual será llamada para 
ejecutarse. Use el siguiente nombre calcular_herencia()
- Los datos numéricos en las respuestas deben mostrar solo la parte entera del 
número.
- El número total de ganado que heredan los hermanos debe ser un múltiplo de 6
Ejemplos de salidas:
Compara las respuestas del algoritmo realizado con los siguientes casos para comprobar
que está bien

Entradas            Resultados en consola
total_ganado=180    Ingresa la cantidad de ganado que heredaran 180
                    Total: 180
                    Hijo mayor: 90
                    Hijo del medio: 60
                    Hijo menor: 30
*************************************************************************
total_ganado=6      Ingresa la cantidad de ganado que heredaran 9
                    Total: 6
                    Hijo mayor: 3
                    Hijo del medio: 2
                    Hijo menor: 1
*************************************************************************
total_ganado=18     Ingresa la cantidad de ganado que heredaran 180
                    Total: 18
                    Hijo mayor: 9
                    Hijo del medio: 6
                    Hijo menor: 3
*/
}
/*Procedure that, given an integer number of head 
of cattle, calculates the corresponding number for each 
child and prints on the screen the total and the number 
of each child in the requested format.*/
void calculate_inheritance(int t){
    int eldest_son, middle_child, youngest_child;
    youngest_child = t / 6;
    middle_child = youngest_child * 2;
    eldest_son = youngest_child * 3;
    printf("Total: %d\nHijo mayor: %d\nHijo del medio: %d\nHijo menor: %d", t, eldest_son, middle_child, youngest_child);    
}

int main(){
    //We declare the variables
    int total_livestock; 
    //We validate if the total number of livestock is a multiple of 6
    do{
       //Read the input 
       printf("Enter the total livestock this must be an integer multiple of 6: ");
       scanf("%d", &total_livestock);
       //When the total number of livestock is a multiple of 6 we start running the program
       if(total_livestock % 6 == 0) calculate_inheritance(total_livestock);   
       
    }while(total_livestock % 6 != 0);
    return 0;
}