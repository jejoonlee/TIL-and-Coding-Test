<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="DBData.DataInput"%>
<%@ page import="java.util.*" %>

<html>
<head>
    <title>와이파이 정보 상세 페이지</title>
    <meta charset="UTF-8">
    <style>
        .names{
            background-color: #0d6efd;
            color: white;
            text-align: center;
        }
        .names, .info{
            padding: 10px 70px;
            border: solid #cecece 1px;
            border-radius : 5%;
        }
    </style>
</head>
<body>
<h1 style="text-align: center;">와이파이 정보 구하기</h1>
<section style="display: flex;align-items: center;justify-content: center;">
    <a href="http://localhost:8080">홈</a>
    <p style="margin: 0 10px;"> | </p>
    <a href="http://localhost:8080/history.jsp">위치 히스토리 목록</a>
    <p style="margin: 0 10px;"> | </p>
    <a class="update-data" href="http://localhost:8080/wifiConfirm.jsp">Open API 와이파이 정보 가져오기</a>
</section>
<%
    String code = request.getParameter("wifi");
    code = new String(code.getBytes("ISO-8859-1"), "UTF-8");
    HashMap<String, String> details = DataInput.getDetailData(code);
    System.out.println(request.getParameter("wifi"));
    System.out.println(code);
%>


<table style="display:flex; justify-content: center; margin:30px 0;">
    <tbody>
        <tr>
            <td class="names">거리(KM)</td>
            <% out.write("<td class=\"info\">"+ request.getParameter("dist") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">관리번호</td>
            <% out.write("<td class=\"info\">"+ details.get("manage_num") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">자치구</td>
            <% out.write("<td class=\"info\">"+ details.get("gu") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">와이파이명</td>
            <% out.write("<td class=\"info\">"+ details.get("wifi_name") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">도로명주소</td>
            <% out.write("<td class=\"info\">"+ details.get("address1") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">상세주소</td>
            <% out.write("<td class=\"info\">"+ details.get("address2") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">설치위층(층)</td>
            <% out.write("<td class=\"info\">"+ details.get("building_floor") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">설치유형</td>
            <% out.write("<td class=\"info\">"+ details.get("install_type") + "</td>"); %>
        </tr>
        <tr>
            <%
                String installCom = details.get("install_company");
                if(installCom == null) installCom = "";
            %>
            <td class="names">설치기관</td>
            <% out.write("<td class=\"info\">"+ installCom + "</td>"); %>
        </tr>
        <tr>
            <td class="names">서비스구분</td>
            <% out.write("<td class=\"info\">"+ details.get("service_type") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">망종류</td>
            <% out.write("<td class=\"info\">"+ details.get("connection_type") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">설치년도</td>
            <% out.write("<td class=\"info\">"+ details.get("install_year") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">실내외구분</td>
            <% out.write("<td class=\"info\">"+ details.get("in_or_out") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">WIFI접속환경</td>
            <% out.write("<td class=\"info\">"+ details.get("wifi_con") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">경도 (Latitude)</td>
            <% out.write("<td class=\"info\">"+ details.get("lat") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">위도 (Longitude)</td>
            <% out.write("<td class=\"info\">"+ details.get("long") + "</td>"); %>
        </tr>
        <tr>
            <td class="names">작업일자</td>
            <% out.write("<td class=\"info\">"+ details.get("work_time") + "</td>"); %>
        </tr>
    </tbody>
</table>
</body>
</html>
