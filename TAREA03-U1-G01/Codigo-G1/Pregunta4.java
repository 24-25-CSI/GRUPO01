import java.util.Scanner;

public class Pregunta4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Alfabeto original
        String alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // Ingresamos la cadena y el desplazamiento
        System.out.print("Ingrese la cadena a cifrar: ");
        String cadena = scanner.nextLine().toUpperCase();

        System.out.print("Ingrese el valor de n (desplazamiento): ");
        int n = scanner.nextInt();

        // Ajustamos el desplazamiento al tamaño del alfabeto
        int longitud = alfabeto.length();
        n = n % longitud; // Esto evita desplazamientos mayores al tamaño del alfabeto

        // Creamos alfabeto cifrado
        String alfabetoCifrado = alfabeto.substring(n) + alfabeto.substring(0, n);

        // Ciframos la cadena ingresada
        StringBuilder cadenaCifrada = new StringBuilder();
        for (int i = 0; i < cadena.length(); i++) {
            char c = cadena.charAt(i);
            int index = alfabeto.indexOf(c);
            if (index != -1) {
                cadenaCifrada.append(alfabetoCifrado.charAt(index));
            } else {
                cadenaCifrada.append(c); // Si no está en el alfabeto, se mantiene igual
            }
        }

        // Imprimimos resultados
        System.out.println("Alfabeto original: " + alfabeto);
        System.out.println("Alfabeto cifrado : " + alfabetoCifrado);
        System.out.println("Cadena original  : " + cadena);
        System.out.println("Cadena cifrada   : " + cadenaCifrada.toString());
    }
}