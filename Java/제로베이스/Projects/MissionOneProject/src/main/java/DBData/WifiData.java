package DBData;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.math.BigDecimal;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.*;

public class WifiData {
    private static String key = "777a4e78696a656a37344256594177";
    public static ArrayList<HashMap<String, String>> allData = new ArrayList<>();

    public static Long getDataCount(){
        /*URL*/
        StringBuilder urlBuilder = new StringBuilder("http://openapi.seoul.go.kr:8088");

        try {
            urlBuilder.append("/" + URLEncoder.encode(key, "UTF-8"));
            urlBuilder.append("/" + URLEncoder.encode("json", "UTF-8"));
            urlBuilder.append("/" + URLEncoder.encode("TbPublicWifiInfo", "UTF-8"));
            urlBuilder.append("/" + URLEncoder.encode("1", "UTF-8"));
            urlBuilder.append("/" + URLEncoder.encode("1", "UTF-8"));
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }

        StringBuilder sb = new StringBuilder();
        try {
            URL url = new URL(urlBuilder.toString());

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-type", "application/json");

            System.out.println("Response code: " + conn.getResponseCode()); /* 연결 자체에 대한 확인이 필요하므로 추가합니다.*/

            BufferedReader rd;

            // 서비스코드가 정상이면 200~300사이의 숫자가 나옵니다.
            if (conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
                rd = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
            } else {
                rd = new BufferedReader(new InputStreamReader(conn.getErrorStream(), "UTF-8"));
            }

            String line;
            while ((line = rd.readLine()) != null) {
                sb.append(line);
            }
            rd.close();
            conn.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }


        JSONObject result = null;
        try {
            result = (JSONObject) new JSONParser().parse(sb.toString());
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }


        JSONObject data = (JSONObject) result.get("TbPublicWifiInfo");

        JSONArray rowData = (JSONArray) data.get("row");

        return (Long) data.get("list_total_count");
    }

    public static void getData(int start, int end) {

        StringBuilder urlBuilder = new StringBuilder("http://openapi.seoul.go.kr:8088");

        try {
            urlBuilder.append("/" + URLEncoder.encode(key, "UTF-8"));
            urlBuilder.append("/" + URLEncoder.encode("json", "UTF-8"));
            urlBuilder.append("/" + URLEncoder.encode("TbPublicWifiInfo", "UTF-8"));
            urlBuilder.append("/" + URLEncoder.encode(String.format("%d", start), "UTF-8"));
            urlBuilder.append("/" + URLEncoder.encode(String.format("%d", end), "UTF-8"));
        } catch (UnsupportedEncodingException e) {
            throw new RuntimeException(e);
        }

        StringBuilder sb = new StringBuilder();
        try {
            URL url = new URL(urlBuilder.toString());

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-type", "application/json");

            System.out.println("Response code: " + conn.getResponseCode()); /* 연결 자체에 대한 확인이 필요하므로 추가합니다.*/

            BufferedReader rd;

            if (conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
                rd = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
            } else {
                rd = new BufferedReader(new InputStreamReader(conn.getErrorStream(), "UTF-8"));
            }

            String line;
            while ((line = rd.readLine()) != null) {
                sb.append(line);
            }
            rd.close();
            conn.disconnect();
        } catch (Exception e) {
            e.printStackTrace();
        }


        JSONObject result = null;
        try {
            result = (JSONObject) new JSONParser().parse(sb.toString());
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }

        JSONObject data = (JSONObject) result.get("TbPublicWifiInfo");

        JSONArray rowData = (JSONArray) data.get("row");

        for (int i = 0; i < rowData.size(); i ++) {
            JSONObject spec = (JSONObject) rowData.get(i);

            HashMap<String, String> map = new HashMap<>();

            map.put("X_SWIFI_MGR_NO", spec.get("X_SWIFI_MGR_NO").toString()); // manage_num, string
            map.put("X_SWIFI_WRDOFC", spec.get("X_SWIFI_WRDOFC").toString()); // Gu, string
            map.put("X_SWIFI_MAIN_NM", spec.get("X_SWIFI_MAIN_NM").toString()); // wifi_name, string
            map.put("X_SWIFI_ADRES1", spec.get("X_SWIFI_ADRES1").toString()); // address1, string
            map.put("X_SWIFI_ADRES2", spec.get("X_SWIFI_ADRES2").toString()); // address2, string
            map.put("X_SWIFI_INSTL_FLOOR", spec.get("X_SWIFI_INSTL_FLOOR").toString()); // building_floor, integer
            map.put("X_SWIFI_INSTL_TY", spec.get("X_SWIFI_INSTL_TY").toString()); // install_type, string
            map.put("X_SWIFI_INSTL_TY", spec.get("X_SWIFI_INSTL_TY").toString()); // install_company, string
            map.put("X_SWIFI_SVC_SE", spec.get("X_SWIFI_SVC_SE").toString()); // service_type, string
            map.put("X_SWIFI_CMCWR", spec.get("X_SWIFI_CMCWR").toString()); // connection_type, string
            map.put("X_SWIFI_CNSTC_YEAR", spec.get("X_SWIFI_CNSTC_YEAR").toString()); // install_year, integer
            map.put("X_SWIFI_INOUT_DOOR", spec.get("X_SWIFI_INOUT_DOOR").toString()); // in_or_out, string
            map.put("X_SWIFI_REMARS3", spec.get("X_SWIFI_REMARS3").toString()); // wifi_con, string
            map.put("LAT", spec.get("LAT").toString()); // lat, integer
            map.put("LNT", spec.get("LNT").toString()); // long, Integer
            map.put("WORK_DTTM", spec.get("WORK_DTTM").toString()); // worktime, datetime

            allData.add(map);
        }
    }

    public static ArrayList<HashMap<String,String>> getAllData(){
        allData = new ArrayList<>();

        int dataCount = getDataCount().intValue();

        int s = 1;
        for (int i = 1000; i <= dataCount; i += 1000) {
            getData(s, i);
            s = i + 1;
        }

        getData((dataCount / 1000) * 1000 + 1, dataCount);

        return allData;
    }
}

