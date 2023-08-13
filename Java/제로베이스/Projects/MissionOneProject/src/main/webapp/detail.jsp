<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="DBData.DataInput"%>
<%@ page import="java.util.*" %>

<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <title>와이파이 정보 구하기</title>
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

        .bookmark-sec{
            display: flex;
            justify-content: center;
        }

        .bm{
            display: flex;
            flex-direction: column;
            justify-content: center;
            width: 500px;
            margin: 30px 0;
        }

        .fs{
            margin-right: 20px;
            padding: 5px 20px;
        }
    </style>
</head>
<body>
<h1 style="text-align: center; margin-top:70px;">와이파이 정보 구하기</h1>
<section style="display: flex;align-items: center;justify-content: center;">
    <a href="http://localhost:8080">홈</a>
    <p style="margin: 0 10px;"> | </p>
    <a href="http://localhost:8080/history.jsp">위치 히스토리 목록</a>
    <p style="margin: 0 10px;"> | </p>
    <a class="update-data" href="http://localhost:8080/wifiConfirm.jsp">Open API 와이파이 정보 가져오기</a>
    <p style="margin: 0 10px;"> | </p>
    <a class="update-data" href="http://localhost:8080/show-bookmark.jsp">즐겨 찾기 보기</a>
    <p style="margin: 0 10px;"> | </p>
    <a class="update-data" href="http://localhost:8080/bookmark-group.jsp">즐겨 찾기 그룹 관리</a>
</section>

<div class="bookmark-sec">
    <form class="bm" action="http://localhost:8080/show-bookmark/insert.jsp" method="post">
        <input value="<% out.write(request.getParameter("wifi")); %>" name="wifiMngNum" style="visibility: hidden; width:0; height:0;">
        <div style="display: flex">
            <select class="fs form-select" name="bId" aria-label="Default select example">
                <option selected>북마크 그룹 이름 선택</option>
                <%
                    ArrayList<HashMap<String, String>> data = DataInput.bookmarkShow();

                    for (HashMap<String, String> rowData : data) {
                        String id = rowData.get("bookmarkId");
                        String name = rowData.get("bName");

                        out.write("<option value=\""+ id +"\">" + name + "</option>");
                    }
                %>
            </select>
            <input class="btn btn-success" type="submit" value="즐겨찾기 추가하기">
        </div>
    </form>
</div>

<%
    HashMap<String, String> details = DataInput.getDetailData(request.getParameter("wifi"));
%>


<table style="display:flex; justify-content: center; margin-bottom:30px">
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
