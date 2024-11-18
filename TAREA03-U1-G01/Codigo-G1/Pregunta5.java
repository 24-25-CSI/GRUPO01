import java.util.Scanner;

public class Pregunta5 {

    public static String encrypt(String texto, String clave) {
        StringBuilder resultado = new StringBuilder();

        // Convertir el texto y la clave a mayúsculas para simplificar el cifrado
        texto = texto.toUpperCase();
        clave = clave.toUpperCase();

        // Generar una clave que se repite tantas veces como sea necesario para cubrir
        // la longitud del texto
        StringBuilder repClave = new StringBuilder(clave);
        while (repClave.length() < texto.length()) {
            repClave.append(clave);
        }
        clave = repClave.toString();

        // Cifrar cada carácter de la cadena
        for (int i = 0; i < texto.length(); i++) {
            char caracter = texto.charAt(i);
            if (Character.isLetter(caracter)) {
                // Fórmula de cifrado Vigenère: Ci = (Pi + Ki) % 26
                char carEncrip = (char) ((caracter + clave.charAt(i) - 2 * 'A') % 26 + 'A');
                resultado.append(carEncrip);
            } else {
                // Si no es una letra (como espacios o signos de puntuación), se mantiene sin
                // cambios
                resultado.append(caracter);
            }
        }

        return resultado.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Leer la cadena de texto a cifrar
        System.out.print("Ingresa la cadena de caracteres: ");
        String texto = scanner.nextLine();

        // Leer la clave de cifrado
        System.out.print("Ingresa la clave de cifrado: ");
        String clave = scanner.nextLine();

        // Cifrar el texto
        String textoEncriptado = encrypt(texto, clave);

        // Mostrar resultados
        System.out.println("Cadena de caracteres ingresada: " + texto);
        System.out.println("Clave de cifrado: " + clave);
        System.out.println("Cadena de caracteres cifrada: " + textoEncriptado);
    }
}
