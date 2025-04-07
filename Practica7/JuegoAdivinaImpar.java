package Juego1;
import java.util.Random;
import java.util.Scanner;

public class JuegoAdivinaImpar extends JuegoAdivinaNumero {

    public JuegoAdivinaImpar(int numeroDeVidas) {
        super(numeroDeVidas);
    }

    public boolean validaNumero(int numero) {
        if (numero >= 0 && numero <= 10) {
            if (numero % 2 != 0)
                return true;
            System.out.println("ERROR: el número debe ser IMPAR.");
        } else {
            System.out.println("ERROR: número fuera de rango ");
        }
        return false;
    }

    public void juega(Scanner leer) {
        reiniciaPartida();
        Random rand = new Random();
        do {
            numeroaAdivinar = rand.nextInt(11);
        } while (numeroaAdivinar % 2 == 0);

        int intentos = 0;

        while (true) {
            System.out.print("Adivina un número IMPAR entre 0 y 10: ");
            int intento = leer.nextInt();
            if (!validaNumero(intento)) continue;
            intentos++;

            if (intento == numeroaAdivinar) {
                System.out.println("Acertaste!!");
                actualizaRecord(intentos);
                break;
            } else {
                if (quitaVida()) {
                    if (intento < numeroaAdivinar) {
                        System.out.println("El número es mayor. Inténtalo de nuevo.");
                    } else {
                        System.out.println("El número es menor. Inténtalo de nuevo.");
                    }
                    System.out.println("Te quedan " + numeroDeVidas + " vidas");
                } else {
                    System.out.println("PERDISTE, el número era: " + numeroaAdivinar);
                    break;
                }
            }
        }
    }
}
