import java.util.Scanner;

public class Pregunta6 {

    // Definir la tabla de cifrado como una matriz
    private static final char[][] tablaCifrado = {
            { '*', 'A', 'S', 'D', 'F', 'G' },
            { 'Q', 'a', 'b', 'c', 'd', 'e' },
            { 'W', 'f', 'g', 'h', 'i', 'j' },
            { 'E', 'k', 'l', 'm', 'n', 'o' },
            { 'R', 'p', 'q', 'r', 's', 't' },
            { 'T', 'u', 'v', 'w', 'x', 'y' }
    };

    // Método para obtener la posición de un carácter en la primera fila o columna
    private static int obtenerPosicion(char caracter, char[] filaColumna) {
        for (int i = 0; i < filaColumna.length; i++) {
            if (filaColumna[i] == caracter) {
                return i;
            }
        }
        return -1;
    }

    // Método para cifrar una cadena utilizando la tabla de cifrado
    public static String cifrarTexto(String texto, String clave) {
        StringBuilder resultado = new StringBuilder();
        char[] primeraFila = { '*', 'A', 'S', 'D', 'F', 'G' };
        char[] primeraColumna = { '*', 'Q', 'W', 'E', 'R', 'T' };

        // Repetir la clave para que coincida con la longitud del texto
        StringBuilder claveExtendida = new StringBuilder(clave);
        while (claveExtendida.length() < texto.length()) {
            claveExtendida.append(clave);
        }
        clave = claveExtendida.toString();

        // Cifrar cada carácter del texto
        for (int i = 0; i < texto.length(); i++) {
            char caracterTexto = texto.charAt(i);
            char caracterClave = clave.charAt(i);

            int fila = obtenerPosicion(caracterClave, primeraColumna);
            int columna = obtenerPosicion(caracterTexto, primeraFila);

            if (fila != -1 && columna != -1) {
                // Agregar el carácter cifrado
                resultado.append(tablaCifrado[fila][columna]);
            } else {
                // Si el carácter no se encuentra en la tabla, agrega "**"
                resultado.append("**");
            }
        }

        return resultado.toString();
    }

    // Método para mostrar la matriz de cifrado
    public static void mostrarMatrizCifrado() {
        System.out.println("Matriz de Cifrado:");
        for (char[] fila : tablaCifrado) {
            for (char c : fila) {
                System.out.print(c + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leer el texto y la clave del usuario
        System.out.print("Ingresa la cadena de caracteres: ");
        String texto = scanner.nextLine().toUpperCase();

        System.out.print("Ingresa la clave de cifrado: ");
        String clave = scanner.nextLine().toUpperCase();

        // Mostrar la matriz de cifrado
        mostrarMatrizCifrado();

        // Cifrar el texto
        String textoCifrado = cifrarTexto(texto, clave);

        // Mostrar los resultados
        System.out.println("Cadena de caracteres ingresada: " + texto);
        System.out.println("Clave de cifrado: " + clave);
        System.out.println("Cadena de caracteres cifrada: " + textoCifrado);
    }
}
