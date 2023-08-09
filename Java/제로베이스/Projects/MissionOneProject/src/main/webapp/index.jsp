<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>

<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        th {
            font-size: small;
            font-weight: bold;
            text-align: center;
        }

        th, td {
            border: 1px solid black;
        }
    </style>
</head>

<body>
<h1 style="text-align: center;">와이파이 정보 구하기</h1>
<section style="display: flex;align-items: center;justify-content: center;">
    <a href="">홈</a>
    <p style="margin: 0 10px;"> | </p>
    <a href="">위치 히스토리 목록</a>
    <p style="margin: 0 10px;"> | </p>
    <a class="update-data" href="http://localhost:8080/wifiConfirm.jsp">Open API 와이파이 정보 가져오기</a>
</section>

<section class="my_loc" style="display: flex;align-items: center;justify-content: center; margin: 20px 0;">
    <form action="http://localhost:8080" method="post">
        <input class="lati" type="text" name="latitude" value="0.0">
        <input class="long" type="text" name="longitude" value="0.0">
        <input class="btn btn-primary" style="padding: 3px 10px;" type="submit" value="근처 WiFI 정보 보기">
    </form>
    <button class="find-my-loc btn btn-success" style="padding: 3px 10px;margin-left:20px">내 위치 가져오기</button>
</section>
<table class="table">
    <thead>
    <tr>
        <th scope="col" style="background-color: #0d6efd;color: white;">거리(Km)</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">관리번호</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">자치구</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">와이파이명</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">도로명주소</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">상세주소</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">설치위치(층)</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">설치유형</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">설치기관</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">서비스구분</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">망종류</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">설치년도</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">실내외구분</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">WIFI 접속환경</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">X좌표</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">Y좌표</th>
        <th scope="col" style="background-color: #0d6efd;color: white;">작업일자</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <%
            String lng = request.getParameter("longitude");
            String lati = request.getParameter("latitude");

            if (lng == null && lati == null) {
                out.write("<td colspan='17' style='text-align: center'>" + "위치 정보를 입력한 후에 조회해 주세요"+ "</td>");
            } else if (lng.equals("0.0") && lati.equals("0.0")) {
                out.write("<td colspan='17' style='text-align: center'>" + "위치 정보를 입력한 후에 조회해 주세요"+ "</td>");
            } else {
                out.write("<p>" + lng + lati + "좌표 있음" + "</p>");
            }
        %>

    </tr>
    </tbody>
</table>
</body>
<script type="text/javascript" src="findLoc.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
</html>