class practica4 {
    double area(double radio) {
        return Math.PI * radio * radio;//círculo
    }
    double area(double base, double altura) {
        return base * altura; //rectángulo
    }
    double area(int base, int altura) {
        return (base * altura) / 2;//triángulo rectángulo
    }
    double area(double baseM, double baseMe, double altura) {
        return ((baseM + baseMe) * altura) / 2;//trapecio
    }
    double area(float lado, float apotema) {
        return (5 * lado * apotema) / 2;//pentagono
    }
    public static void main(String[] args) {
        practica4 f1 = new practica4();
        System.out.println("círculo: " + f1.area(5));
        System.out.println(" rectángulo: " + f1.area(4, 6));
        System.out.println("triángulo rectángulo: " + f1.area(6, 6));
        System.out.println("trapecio: " + f1.area(8, 4, 5));
        System.out.println("pentágono: " + f1.area(6f, 4f));
    }
}
