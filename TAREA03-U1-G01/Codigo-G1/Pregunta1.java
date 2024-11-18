import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Pregunta1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leer la palabra
        System.out.print("Ingrese la palabra: ");
        String palabra = scanner.nextLine();

        // Generar todas las permutaciones
        List<String> permutaciones = new ArrayList<>();
        generarPermutaciones("", palabra, permutaciones);

        // Ordenar las permutaciones alfabéticamente
        Collections.sort(permutaciones);

        // Mostrar el número total de permutaciones
        System.out.println("Número total de permutaciones: " + permutaciones.size());

        // Mostrar las primeras 10 permutaciones ordenadas alfabéticamente
        System.out.println("Las primeras 10 permutaciones ordenadas alfabéticamente son:");
        for (int i = 0; i < Math.min(10, permutaciones.size()); i++) {
            System.out.println(permutaciones.get(i));
        }

        scanner.close();
    }

    // Método para generar todas las permutaciones de una palabra
    private static void generarPermutaciones(String prefijo, String palabra, List<String> permutaciones) {
        int n = palabra.length();
        if (n == 0) {
            permutaciones.add(prefijo);
        } else {
            for (int i = 0; i < n; i++) {
                generarPermutaciones(prefijo + palabra.charAt(i), palabra.substring(0, i) + palabra.substring(i + 1, n),
                        permutaciones);
            }
        }
    }
}