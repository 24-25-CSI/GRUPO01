import java.util.Scanner;

public class Pregunta2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leer el valor de n
        System.out.print("Ingrese el valor de n: ");
        int n = scanner.nextInt();
        scanner.nextLine(); // Consumir la nueva línea

        // Leer el mensaje
        System.out.print("Ingrese el mensaje: ");
        String mensaje = scanner.nextLine().replace(" ", ""); // Eliminar espacios

        // Verificar que la longitud del mensaje sea menor o igual a n * n
        if (mensaje.length() > n * n) {
            System.out.println("El mensaje es demasiado largo para la matriz de cifrado.");
            return;
        }

        // Crear la matriz de cifrado
        char[][] matriz = new char[n][n];
        int index = 0;

        // Llenar la matriz con los caracteres del mensaje
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (index < mensaje.length()) {
                    matriz[i][j] = mensaje.charAt(index++);
                } else {
                    matriz[i][j] = '*'; // Llenar con '*'
                }
            }
        }

        // Imprimir la matriz de cifrado
        System.out.println("Matriz de cifrado:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }

        // Leer la matriz por filas para obtener el mensaje cifrado
        StringBuilder mensajeCifrado = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                mensajeCifrado.append(matriz[i][j]);
            }
        }

        // Imprimir el mensaje original y el mensaje cifrado
        System.out.println("Mensaje original: " + mensaje);
        System.out.println("Mensaje cifrado: " + mensajeCifrado.toString());

        scanner.close();
    }
}