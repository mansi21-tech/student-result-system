public class ResultCalculator {

    public static void main(String[] args) {

        double maths = Double.parseDouble(args[0]);
        double science = Double.parseDouble(args[1]);
        double english = Double.parseDouble(args[2]);
        double computer = Double.parseDouble(args[3]);

        double total = maths + science + english + computer;
        double percentage = total / 4;

        String result;

        if (maths >= 35 &&
            science >= 35 &&
            english >= 35 &&
            computer >= 35) {

            result = "PASS";

        } else {

            result = "FAIL";
        }

        System.out.println(total + "|" + percentage + "|" + result);
    }
}