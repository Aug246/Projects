import java.util.Scanner;
/*
 Reads array elements from the user (including negative and positive numbers)
  and counts the number of negative array elements.
*/

public class NegativeElementCounterActivity {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("How many elements? ");
        int arraySize = scanner.nextInt();
        int negNum = 0;
         
        if (arraySize > 0){
            double[] objects = new double[arraySize];
            for (int i = 0; i < arraySize; i++){
                objects[i] = scanner.nextDouble();
                if (objects[i] < 0){negNum += 1;}
            }
        }
        else{System.out.println("Enter a positive interger please!");}

        System.out.println("You entered " + negNum + " negative numbers!");

    }
}
