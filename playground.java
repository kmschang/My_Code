public class playground {

    public static void main(String[] args) {

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                System.out.print(i + "" + j + " ");
            }
        }

    }


}


class circle {

    double radius = 5;
    static double pi = 3.14;

    circle() {}

    circle(double radius) {
        this.radius = radius;
    }

    double area() {
        return pi * radius * radius;
    }

    double circumference() {
        return 2 * pi * radius;
    }

    public static void main(String[] args) {
        circle c1 = new circle();
        circle c2 = new circle(10);
        System.out.println(c1.area());
        System.out.println(c2.area());
    }



}
