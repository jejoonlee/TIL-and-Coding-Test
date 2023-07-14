
public class CreditCard {
    private long cardNum;
    public String cardOwner;
    private long balance;
    private long point;

    CreditCard(String cardOwner) {
        this.cardOwner = cardOwner;
    }

    public void setCardNum(long cardNum) {
        this.cardNum = cardNum;
    }

    public void getCardNum() {
        System.out.println(this.cardNum);
    }

    public void getBalance() {
        System.out.println(this.balance);
    }

    public void getPoint() {
        System.out.println(this.point);
    }

    public void use(int amount) {
        this.balance += amount;
    }

    public void paybill(int amount) {
        this.balance -= amount;
        addPoint(amount / 1000);
    }

    private void addPoint(int amount) {
        this.point += amount;
    }
}
