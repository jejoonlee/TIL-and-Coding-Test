package DBData;

import org.json.simple.JSONObject;
import org.json.simple.parser.ParseException;

import java.math.BigDecimal;
import java.sql.*;
import java.util.*;

public class DataInput {

    public static void dataInsert() {

        ArrayList<JSONObject> data = WifiData.getAllData();

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

    public static int dataUpdate() {
        ArrayList<JSONObject> data = WifiData.getAllData();

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

                // 데이터를 아예 업데이트 할 떄에는 insert or replace으로
                String sql =
                        "insert or ignore into wifiInfo (manage_num, Gu, wifi_name, address1, address2, building_floor, install_type, install_company, service_type, connection_type, install_year, in_or_out, wifi_con, lat, long, work_time)" +
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

        return data.size();
    }

    public static void dataAllDelete() {

        Connection con = null;

        try {
            // SQLite JDBC 체크
            Class.forName("org.sqlite.JDBC");

            // SQLite 데이터베이스 파일에 연결
            String dbFile = "C:\\Users\\ADMIN\\OneDrive\\Desktop\\TIL\\Java\\제로베이스\\Projects\\MissionOne\\MissionOneProject\\seoulWifi.db";
            con = DriverManager.getConnection("jdbc:sqlite:" + dbFile);


            Statement stat = con.createStatement();

            // 데이터를 아예 업데이트 할 떄에는 insert or replace으로
            String sql =
                    "delete from wifiInfo";

            PreparedStatement statement = con.prepareStatement(sql);
            statement.executeUpdate();


        }catch(Exception e) {
            e.printStackTrace();
        }finally {
            if(con != null) {
                try {con.close();}catch(Exception e) {}
            }
        }
    }
}
