import java.util.Scanner;

public class Circulo {
    public static void main(String args[]){
        double pi = 3.1416;
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese el valor para el radio: ");
        int n = sc.nextInt();

        System.out.print(Math.pow(n,2) * pi);
    }
}
