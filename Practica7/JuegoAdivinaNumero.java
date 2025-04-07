package Practica7;
import java.util.Random;
import java.util.Scanner;

public class JuegoAdivinaNumero extends Juego {
    protected int numeroaAdivinar;

    public JuegoAdivinaNumero(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    public boolean validaNumero(int numero) {
        return numero >= 0 && numero <= 10;
    }

    public void juega(Scanner leer) {
        reiniciaPartida();
        Random rand = new Random();
        numeroaAdivinar = rand.nextInt(11);
        int intentos = 0;

        while (true) {
            System.out.print("Adivina un número entre 0 y 10: ");
            int intento = leer.nextInt();
            intentos++;

            if (intento == numeroaAdivinar) {
                System.out.println("Acertaste!!");
                actualizaRecord(intentos);
                break;
            } else {
                if (quitaVida()) {
                    if (intento < numeroaAdivinar) {
                        System.out.println(" El número es mayor. Inténtalo de nuevo.");
                    } else {
                        System.out.println("El número es menor. Inténtalo de nuevo.");
                    }
                    System.out.println("Te quedan  " + numeroDeVidas + " vidas");
                } else {
                    System.out.println("PERDISTE, el número era: " + numeroaAdivinar);
                    break;
                }
            }
        }
    }
}
