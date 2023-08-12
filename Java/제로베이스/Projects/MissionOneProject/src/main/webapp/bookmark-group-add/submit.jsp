
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="DBData.DataInput" %>

<html>
<head>
    <title>와이파이 정보 구하기</title>
</head>
<body>
    <%
        String bName = request.getParameter("bName");
        String bOrder = request.getParameter("bOrder");

        boolean success = DataInput.bookmarkAdd(bName, bOrder);

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
        alert("이미 즐겨찾기 그룹 이름이 존재합니다.\n다시 입력해주세요")
        location.href="http://localhost:8080/bookmark-group-add.jsp";
    } else if (isSuccess.textContent == "Success") {
        alert("즐겨찾기 그룹 정보를 추가하였습니다")
        location.href="http://localhost:8080/bookmark-group.jsp";
    } else {
        alert("다른 문제가 발생했습니다.\n관리자에게 해당 문제를 알려주세요");
        location.href="http://localhost:8080/bookmark-group-add.jsp";
    }
</script>

</html>
