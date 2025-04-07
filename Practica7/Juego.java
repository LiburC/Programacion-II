package Juego1;

public class Juego {
    protected int numeroDeVidas;
    protected int record;

    public Juego(int numeroDeVidas) {
        this.numeroDeVidas = numeroDeVidas;
        this.record = 0;
    }

    public void reiniciaPartida() {
        System.out.println("Reiniciando partida.");
    }

    public void actualizaRecord(int intentos) {
        if (record == 0 || intentos < record) {
            record = intentos;
            System.out.println("Nuevo récord: " + record );
        } else {
            System.out.println("GANASTE, pero no superaste el récord de " + record );
        }
    }

    public boolean quitaVida() {
        numeroDeVidas--;
        return numeroDeVidas > 0;
    }
}

