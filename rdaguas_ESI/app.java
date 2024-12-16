
import java.util.Scanner;

public class app {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("*******************Ejercicio 2*******************");
        System.out.println("Realizado por:" + " " + "Roberto Aguas");
        System.out.println(" ");
        System.out.println(" ");
        System.out.print("Ingrese el mensaje a cifrar:");
        String mensaje = scanner.nextLine();
        scanner.close();

        try {
            String mensajeOriginal = mensaje.replace(" ", "#");
            int columnas = 5;
            int filas = (int) Math.ceil((double) mensajeOriginal.length() / columnas);
            filas = Math.max(filas, 3); // Garantizar al menos 3 filas

            char[][] matrizCifrado = new char[filas][columnas];
            int indice = 0;

            // Llenar la matriz de cifrado
            for (int i = 0; i < filas; i++) {
                for (int j = 0; j < columnas; j++) {
                    if (indice < mensajeOriginal.length()) {
                        matrizCifrado[i][j] = mensajeOriginal.charAt(indice);
                    } else {
                        matrizCifrado[i][j] = '_';
                    }
                    indice++;
                }
            }
            // muestra el mensaje original ingresado
            System.out.println("Mensaje original: " + mensaje);
            // muestra la matriz de cifrado generada
            System.out.println("Matriz de cifrado:");
            for (int i = 0; i < filas; i++) {
                for (int j = 0; j < columnas; j++) {
                    System.out.print(matrizCifrado[i][j] + " ");
                }
                System.out.println();
            }
            // generar el mensaje cifrado a partir de la matriz
            StringBuilder mensajeCifrado = new StringBuilder();
            for (int j = 0; j < columnas; j++) {
                for (int i = 0; i < filas; i++) {
                    mensajeCifrado.append(matrizCifrado[i][j]);
                }
            }
            // muestra el mensaje cifrado
            System.out.println("Mensaje cifrado: " + mensajeCifrado.toString());
        } catch (Exception e) {
            System.out.println("Se produjo un error en la ejecución: " + e.getMessage());
        }
    }
}