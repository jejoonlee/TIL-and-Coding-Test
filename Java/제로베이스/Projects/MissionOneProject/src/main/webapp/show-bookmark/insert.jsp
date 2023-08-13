<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="DBData.DataInput" %>

<html>
<head>
    <title>Title</title>
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
        alert("바꾸려는 즐겨찾기 이름이 이미 존재합니다\n또는, 해당 즐겨찾기 그룹이 존재하지 않을 수 있습니다");
    } else if (isSuccess.textContent == "Success") {
        alert("즐겨찾기 그룹 정보를 성공적으로 수정했습니다");
        location.href="http://localhost:8080/show-bookmark.jsp";
    } else {
        alert("다른 문제가 발생했습니다.\n관리자에게 해당 문제를 알려주세요");
    }
</script>
</html>
