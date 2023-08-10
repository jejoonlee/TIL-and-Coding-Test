package DBData;

import java.math.BigDecimal;

public class Main {
    public static void main(String[] args) {
//        DataInput.dataAllDelete();
//
//        DataInput.dataInsert();


        BigDecimal latitude = new BigDecimal("37.2072");
        BigDecimal longitude = new BigDecimal("126.8168");
        DataInput.getCloseWifi(latitude, longitude);
//        WifiData.getAllData();
    }
}
