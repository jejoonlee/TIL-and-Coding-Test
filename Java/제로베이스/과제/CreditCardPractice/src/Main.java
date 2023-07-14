// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        CreditCard myCard = new CreditCard("이제준");
        myCard.setCardNum(1234_5678_1234_1234L);

        System.out.println("==============");
        myCard.getCardNum();
        System.out.println(myCard.cardOwner);
        myCard.getBalance();
        myCard.getPoint();

        myCard.use(8000);
        myCard.use(12000);
        myCard.use(21000);
        myCard.paybill(30000);

        System.out.println("==============");
        myCard.getCardNum();
        System.out.println(myCard.cardOwner);
        myCard.getBalance();
        myCard.getPoint();
    }
}