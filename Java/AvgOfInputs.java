import java.util.Scanner;

public class AvgOfInputs {
    public static void main(String[] args) {

        Scanner keyboard = new Scanner(System.in);
        float input1, input2, input3, average;
        
        System.out.print("Enter input 1:\t");
        input1 = keyboard.nextFloat();
        
        System.out.print("Enter input 2:\t");
        input2 = keyboard.nextFloat();

        System.out.print("Enter input 3:\t");
        input3 = keyboard.nextFloat();

        average = (input1 + input2 + input3)/3;

        System.out.print("The average of the inputs is " + average);
            

        keyboard.close();
    }
}

    