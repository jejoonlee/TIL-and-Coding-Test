<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="DBData.DataInput" %>

<html>
<head>
    <title>와이파이 정보 구하기</title>
</head>
<body>
    <%
        request.setCharacterEncoding("UTF-8");
        String bId = request.getParameter("bId");
        String wifiMngNum = request.getParameter("wifiMngNum");

        boolean success = DataInput.addWifiIntoBookmark(wifiMngNum, bId);

        if (success) {
            out.write("<p>Success</p>");
        } else {
            out.write("<p>Fail</p>");
        }
    %>
</body>

<script>
    const isSuccess = document.querySelector("p");

    if (isSuccess.textContent == "Fail") {
        alert("이미 해당 와이파이 정보가 즐겨찾기 그룹에 추가가 되어 있습니다");
    } else if (isSuccess.textContent == "Success") {
        alert("해당 화이파이 정보를 즐겨찾기 그룹에 성공적으로 추가했습니다");
        location.href="http://localhost:8080/show-bookmark.jsp";
    } else {
        alert("다른 문제가 발생했습니다.\n관리자에게 해당 문제를 알려주세요");
    }
</script>
</html>
