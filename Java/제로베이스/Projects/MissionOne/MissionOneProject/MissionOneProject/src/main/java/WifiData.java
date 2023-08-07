
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.*;

public class WifiData {
    private static String key = "777a4e78696a656a37344256594177";
    public static ArrayList<JSONObject> allData = new ArrayList<>();

    public static Long getDataCount() throws IOException, ParseException {
        /*URL*/
        StringBuilder urlBuilder = new StringBuilder("http://openapi.seoul.go.kr:8088");

        urlBuilder.append("/" + URLEncoder.encode(key,"UTF-8") ); /*인증키 (sample사용시에는 호출시 제한됩니다.)*/

        urlBuilder.append("/" + URLEncoder.encode("json","UTF-8") ); /*요청파일타입 (xml,xmlf,xls,json) */

        urlBuilder.append("/" + URLEncoder.encode("TbPublicWifiInfo","UTF-8"));

        /*서비스명 (대소문자 구분 필수입니다.)*/
        urlBuilder.append("/" + URLEncoder.encode("1000","UTF-8")); /*요청시작위치 (sample인증키 사용시 5이내 숫자)*/

        urlBuilder.append("/" + URLEncoder.encode("1001","UTF-8"));
        /*요청종료위치(sample인증키 사용시 5이상 숫자 선택 안 됨)*/

        // 상위 5개는 필수적으로 순서바꾸지 않고 호출해야 합니다.
        // 서비스별 추가 요청 인자이며 자세한 내용은 각 서비스별 '요청인자'부분에 자세히 나와 있습니다.
//        urlBuilder.append("/" + URLEncoder.encode("20220301","UTF-8")); /* 서비스별 추가 요청인자들*/

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
                rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            } else {
                rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
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


        JSONObject result = (JSONObject) new JSONParser().parse(sb.toString());

        JSONObject data = (JSONObject) result.get("TbPublicWifiInfo");

        JSONArray rowData = (JSONArray) data.get("row");

        return (Long) data.get("list_total_count");
    }

    public static void getData(int start, int end) throws IOException, ParseException {
        /*URL*/
        StringBuilder urlBuilder = new StringBuilder("http://openapi.seoul.go.kr:8088");

        urlBuilder = new StringBuilder("http://openapi.seoul.go.kr:8088");

        urlBuilder.append("/" + URLEncoder.encode(key ,"UTF-8") ); /*인증키 (sample사용시에는 호출시 제한됩니다.)*/

        urlBuilder.append("/" + URLEncoder.encode("json","UTF-8") ); /*요청파일타입 (xml,xmlf,xls,json) */

        urlBuilder.append("/" + URLEncoder.encode("TbPublicWifiInfo","UTF-8"));

        urlBuilder.append("/" + URLEncoder.encode(String.format("%d", start),"UTF-8"));

        urlBuilder.append("/" + URLEncoder.encode(String.format("%d", end),"UTF-8"));

        StringBuilder sb = new StringBuilder();
        try {
            URL url = new URL(urlBuilder.toString());

            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Content-type", "application/json");

            System.out.println("Response code: " + conn.getResponseCode()); /* 연결 자체에 대한 확인이 필요하므로 추가합니다.*/

            BufferedReader rd;

            if (conn.getResponseCode() >= 200 && conn.getResponseCode() <= 300) {
                rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            } else {
                rd = new BufferedReader(new InputStreamReader(conn.getErrorStream()));
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


        JSONObject result = (JSONObject) new JSONParser().parse(sb.toString());

        JSONObject data = (JSONObject) result.get("TbPublicWifiInfo");

        JSONArray rowData = (JSONArray) data.get("row");

        for (int i = 0; i < rowData.size(); i ++) {
            allData.add((JSONObject) rowData.get(i));
        }
    }

    public static void main(String[] args) throws IOException, ParseException {

        int dataCount = getDataCount().intValue();
        System.out.println(dataCount);

        // 한번에 최대 1000개의 데이터를 받아올 수 있다
        int s = 1;
        for (int i = 1000; i <= dataCount; i += 1000) {
            getData(s, i);
            s = i + 1;
        }

        getData((dataCount / 1000) * 1000 + 1, dataCount);

        System.out.println(allData.size() + " " + dataCount);

        System.out.println("관리번호: " + allData.get(0).get("X_SWIFI_MGR_NO") + " " + allData.get(0).get("X_SWIFI_MGR_NO").getClass());
        System.out.println("자치구: " + allData.get(0).get("X_SWIFI_WRDOFC") + " " + allData.get(0).get("X_SWIFI_WRDOFC").getClass());
        System.out.println("와이파이명: " + allData.get(0).get("X_SWIFI_MAIN_NM") + " " + allData.get(0).get("X_SWIFI_MAIN_NM").getClass());
        System.out.println("도로명주소: " + allData.get(0).get("X_SWIFI_ADRES1") + " " + allData.get(0).get("X_SWIFI_ADRES1").getClass());
        System.out.println("상세주소: " + allData.get(0).get("X_SWIFI_ADRES2") + " " + allData.get(0).get("X_SWIFI_ADRES2").getClass());
        System.out.println("설치위치(층): " + allData.get(0).get("X_SWIFI_INSTL_FLOOR") + " " + allData.get(0).get("X_SWIFI_INSTL_FLOOR").getClass());
        System.out.println("설치유형: " + allData.get(0).get("X_SWIFI_INSTL_TY") + " " + allData.get(0).get("X_SWIFI_INSTL_TY").getClass());
        System.out.println("설치기관: " + allData.get(0).get("X_SWIFI_INSTL_MBY") + " " + allData.get(0).get("X_SWIFI_INSTL_MBY").getClass());
        System.out.println("서비스구분: " + allData.get(0).get("X_SWIFI_SVC_SE") + " " + allData.get(0).get("X_SWIFI_SVC_SE").getClass());
        System.out.println("망종류: " + allData.get(0).get("X_SWIFI_CMCWR") + " " + allData.get(0).get("X_SWIFI_CMCWR").getClass());
        System.out.println("설치년도: " + allData.get(0).get("X_SWIFI_CNSTC_YEAR") + " " + allData.get(0).get("X_SWIFI_CNSTC_YEAR").getClass());
        System.out.println("실내외구분: " + allData.get(0).get("X_SWIFI_INOUT_DOOR") + " " + allData.get(0).get("X_SWIFI_INOUT_DOOR").getClass());
        System.out.println("wifi접속환경: " + allData.get(0).get("X_SWIFI_REMARS3") + " " + allData.get(0).get("X_SWIFI_REMARS3").getClass());
        System.out.println("Y좌표: " + allData.get(0).get("LAT") + " " + allData.get(0).get("LAT").getClass());
        System.out.println("X좌표: " + allData.get(0).get("LNT") + " " + allData.get(0).get("LNT").getClass());
        System.out.println("작업일자: " + allData.get(0).get("WORK_DTTM") + " " + allData.get(0).get("WORK_DTTM").getClass());

    }
}
