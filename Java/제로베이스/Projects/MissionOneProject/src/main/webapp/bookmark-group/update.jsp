
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="DBData.DataInput" %>

<html>
<head>
    <title>와이파이 정보 구하기</title>
</head>
<body>
<%
    String bookmarkId = request.getParameter("id");
    String bOrder = request.getParameter("bOrder");
    String bName = request.getParameter("bName");

    System.out.println(bookmarkId + " " + bOrder + " " + bName);
    boolean success = DataInput.updateBookmark(bookmarkId, bName, bOrder);

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
    } else {
        alert("다른 문제가 발생했습니다.\n관리자에게 해당 문제를 알려주세요");
    }
    location.href="http://localhost:8080/bookmark-group.jsp";
</script>
</html>
