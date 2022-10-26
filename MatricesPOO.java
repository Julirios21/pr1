import java.util.Scanner;
import java.util.Random;
class matricesPOO{
    private Scanner sc;
    private int numero1 = 4;
    private int numero2 = 4;

    public static int[][] crear(int numero1,int numero2){
        int matriz[][] = new int[numero1][numero2];
        Random r = new Random();
        Scanner sc = new Scanner(System.in);
        for (int i=0; i<matriz.length; i++){
            for (int e=0; e<matriz[0].length; e++){
                // System.out.print("llene la matriz: ");
                // matriz[i][e] = sc.nextInt();
                int n = r.nextInt(2);
                matriz[i][e] = n;
            }
        }
        return matriz;
    }
    public static void mostrar(int matriz[][]){
            for (int i=0 ; i<matriz.length; i++ ){
                System.out.println("");
                for (int e=0; e<matriz[0].length; e++){
                    System.out.print(matriz[i][e]+" ");
            }
        }
    }

    public static void main(String[] args) {
        int matriz[][] = crear(3,4);
        mostrar(matriz);   
    }
}