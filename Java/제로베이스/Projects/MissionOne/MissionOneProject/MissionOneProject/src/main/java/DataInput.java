import org.json.simple.JSONObject;
import org.json.simple.parser.ParseException;

import java.io.IOException;
import java.math.BigDecimal;
import java.sql.*;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.Date;

public class DataInput {

    public static void dataInsert(ArrayList<JSONObject> data) {
        Connection con = null;

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";
            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile);

            for (JSONObject jsonData : data) {
                // SQL 수행
                Statement stat = con.createStatement();

                String sql =
                        "insert into wifiInfo (manage_num, Gu, wifi_name, address1, address2, building_floor, install_type, install_company, service_type, connection_type, install_year, in_or_out, wifi_con, lat, long, work_time)" +
                                "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

                PreparedStatement statement = con.prepareStatement(sql);

                String manageNum = (String) jsonData.get("X_SWIFI_MGR_NO");
                statement.setString(1, manageNum); // manage_num, string

                statement.setString(2, (String) jsonData.get("X_SWIFI_WRDOFC")); // Gu, string
                statement.setString(3, (String) jsonData.get("X_SWIFI_MAIN_NM")); // wifi_name, string
                statement.setString(4, (String) jsonData.get("X_SWIFI_ADRES1")); // address1, string
                statement.setString(5, (String) jsonData.get("X_SWIFI_ADRES2")); // address2, string
                statement.setString(6, (String) jsonData.get("X_SWIFI_INSTL_FLOOR")); // building_floor, integer
                statement.setString(7, (String) jsonData.get("X_SWIFI_INSTL_TY")); // install_type, string
                statement.setString(8, (String) jsonData.get("X_SWIFI_INSTL_MBY")); // install_company, string
                statement.setString(9, (String) jsonData.get("X_SWIFI_SVC_SE")); // service_type, string
                statement.setString(10, (String) jsonData.get("X_SWIFI_CMCWR")); // connection_type, string

                int year = Integer.parseInt((String)jsonData.get("X_SWIFI_CNSTC_YEAR"));
                statement.setInt(11, year); // install_year, integer
                statement.setString(12, (String) jsonData.get("X_SWIFI_INOUT_DOOR")); // in_or_out, string
                statement.setString(13, (String) jsonData.get("X_SWIFI_REMARS3")); // wifi_con, string

                BigDecimal latitude = new BigDecimal((String) jsonData.get("LAT"));
                statement.setBigDecimal(14, latitude); // lat, integer

                BigDecimal Longitude = new BigDecimal((String) jsonData.get("LNT"));
                statement.setBigDecimal(15, Longitude); // long, Integer

                statement.setString(16, (String) jsonData.get("WORK_DTTM")); // worktime, datetime

                int affected = statement.executeUpdate();
                if (affected > 0) System.out.println(manageNum + ": success");
                else System.out.println("fail");

            }

        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {}
            }
        }
    }

    public static void main(String[] args) throws IOException, ParseException {
//        int dataCount = WifiData.getDataCount().intValue();
//        System.out.println(dataCount);
//
//        // 한번에 최대 1000개의 데이터를 받아올 수 있다
//        int s = 1;
//        for (int i = 1000; i <= dataCount; i += 1000) {
//            WifiData.getData(s, i);
//            s = i + 1;
//        }
//
//        WifiData.getData((dataCount / 1000) * 1000 + 1, dataCount);
//
//        ArrayList<JSONObject> data = WifiData.allData;

        // 와이파이 데이터 새로 추가하기
//        dataInsert(data);



    }

}
