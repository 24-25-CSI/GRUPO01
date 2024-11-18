import java.util.Scanner;

public class Pregunta3 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n;
        String mensaje;

        while (true) {
            // Leer el valor de n
            System.out.print("Ingrese el valor de n (filas y columnas): ");
            n = scanner.nextInt();
            scanner.nextLine(); // Consumir la nueva línea

            // Leer el mensaje
            System.out.print("Ingrese el mensaje: ");
            mensaje = scanner.nextLine().replace(" ", "");

            // Verificar que la longitud del mensaje sea menor o igual a n * n
            if (mensaje.length() <= n * n) {
                break;
            } else {
                System.out.println(
                        "El mensaje es demasiado largo para la matriz de cifrado. Por favor, ingrese un nuevo valor de n.");
            }
        }

        // Crear la matriz de cifrado y llenarla con el mensaje
        char[][] matriz = new char[n][n];
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (index < mensaje.length()) {
                    matriz[i][j] = mensaje.charAt(index++);
                } else {
                    matriz[i][j] = '*';
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

        // Realizar la permutación de columnas para cifrar el mensaje
        StringBuilder mensajeCifrado = new StringBuilder();
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                mensajeCifrado.append(matriz[i][j]);
            }
        }

        // Imprimir el mensaje original y el mensaje cifrado
        System.out.println("Mensaje original: " + mensaje);
        System.out.println("Mensaje cifrado: " + mensajeCifrado.toString());

        scanner.close();
    }
}