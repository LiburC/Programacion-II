package Juego1;
import java.util.Scanner;

public class Aplicacion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); 

        JuegoAdivinaNumero juegoNormal = new JuegoAdivinaNumero(3);
        JuegoAdivinaPar juegoPar = new JuegoAdivinaPar(3);
        JuegoAdivinaImpar juegoImpar = new JuegoAdivinaImpar(3);

        System.out.println("JUEGO 'ADIVINA UN NÚMERO'");
        juegoNormal.juega(scanner);

        System.out.println("\nJUEGO 'ADIVINA UN NÚMERO PAR'");
        juegoPar.juega(scanner);

        System.out.println("\nJUEGO 'ADIVINA UN NÚMERO IMPAR'");
        juegoImpar.juega(scanner);

        scanner.close(); 
    }
}
